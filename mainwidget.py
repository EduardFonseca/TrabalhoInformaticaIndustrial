from timeseriesgraph import TimeSeriesGraph
from kivymd.uix.screen import MDScreen
from pyModbusTCP.client import ModbusClient
from kivymd.uix.snackbar import Snackbar
from kivy_garden.graph import LinePlot
from threading import Thread, Lock
from datetime import datetime
import random
from time import sleep
from db import Session,Base, engine
from models import DadosIndustria
from kivy.uix.boxlayout import BoxLayout



class MyWidget(MDScreen):

    _updateThread = None
    _updateWidget = True #TODO: verificar a necissidade de transformar em false principalmente ao desconectar do servidor
    _tags = {}
    _max_points = 20


    def __init__(self,**kwargs):
        super().__init__()
        self._scan_time = 1000
        self._meas={}
        self._meas['timestamp'] = None
        self._meas['values'] = {}
        self._lock=Lock()
        for key,value in kwargs.get('modbus_addr').items():
            if key == 'peso_obj':
                plot_color = (0,0,0,)
                self._tags[key] = {'addr': value[0], 'multiplicador':value[1] , 'color':plot_color}
            elif key == 'cor_obj_R':
                plot_color = (1,0,0,1)
                self._tags[key] = {'addr': value[0], 'multiplicador':value[1] , 'color':plot_color}
            elif key == 'cor_obj_G': 
                plot_color = (0,1,0,1)
                self._tags[key] = {'addr': value[0], 'multiplicador':value[1] , 'color':plot_color}
            elif key == 'cor_obj_B':
                plot_color = (0,0,1,1)
                self._tags[key] = {'addr': value[0], 'multiplicador':value[1] , 'color':plot_color}
            else:
                plot_color = (random.random(),random.random(),random.random(),1)
                self._tags[key] = {'addr': value[0], 'multiplicador':value[1] , 'color':plot_color}
        self._modbusClient = ModbusClient()
        self._session = Session()
        Base.metadata.create_all(engine)
        self.graph_massa_setup()
        self.grap_RGB_setup()
        self.create_histgraph_checkbox()

    def connect(self):
        """
        Conexao com Servidor modbus
        """
        if self.ids.bt_con.text =='CONECTAR':
            try:
                self._modbusClient.host = self.ids.hostname.text
                self._modbusClient.port = int(self.ids.port.text)
                self._modbusClient.open()
                self.startDataRead()
            except Exception as e:
                print("Erro: ",e.args)
        else:
            self.ids.bt_con.text = "CONECTAR"
            self._modbusClient.close()
            Snackbar(text="Cliente desconectado",bg_color=(1,0,0,1)).open()

    def startDataRead(self):
        """
        Metodo utilixado para a configuracao do IP e porta do servidor MODBUS e
        inicializar uma thread para a leitura dos dados e atualizacao da interface
        """
        if self._modbusClient.is_open():
            self.ids.bt_con.text = "DESCONECTAR"
            Snackbar(text = "Conexao realizada com sucesso",bg_color=(0,1,0,1)).open()
            self._updateThread = Thread(target=self.updater)
            self._updateThread.start()
        else:
            Snackbar(text = "Falha ao realizar a conexao",bg_color=(1,0,0,1)).open()
            print("falha na conexao com o servidor")

    def updater(self):
        """
        Invoca leitura de dados, atualizacao da interface e insercao de dados na DB
        """
        try:
            while self._updateWidget:
                self.readData()
                self.updateGUI()
                self._lock.acquire()
                dado = DadosIndustria(**self._meas['values'])
                dado.timestamp = self._meas['timestamp']
                self._session.add(dado)
                self._session.commit()
                self._lock.release()

                sleep(self._scan_time/5000)

        except Exception as e:
            self._modbusClient.close()
            print("Erro: 1 ", e.args)

    def stopRefresh(self):
        self._updateWidget=False

    def readData(self):
        """
        Metodo para a leitura dos dados por meio do protocolo MODBUS
        """
        self._meas['timestamp'] = datetime.now()
        for key,value in self._tags.items():
            if key == 'filtro_est_1' or key == 'filtro_est_2' or key == 'filtro_est_3' or key=='estado_atuador' or key == 'bt_desliga' :
                self._meas['values'][key] = self._modbusClient.read_coils(value['addr'],1)[0]
            else:
                self._meas['values'][key] = (self._modbusClient.read_holding_registers(value['addr'],1)[0])/value['multiplicador']
        # print(self._meas)

    def updateGUI(self):
        """
        Atualizacao da inteface de usuario
        """
        self.ids.mass_graph.updateGraph((self._meas['timestamp'],self._meas['values']['peso_obj']),0)
        self.ids.RGB_graph.updateGraph((self._meas['timestamp'],self._meas['values']['cor_obj_R']),0)
        self.ids.RGB_graph.updateGraph((self._meas['timestamp'],self._meas['values']['cor_obj_G']),1)
        self.ids.RGB_graph.updateGraph((self._meas['timestamp'],self._meas['values']['cor_obj_B']),2)
        self.get_printable_info()

    def getDataDb(self):
        init_t = self.parseDTString(self.ids.txt_init_time.text)
        final_t = self.parseDTString(self.ids.txt_final_time.text)
        cols=[]
        for sensor in self.ids.sensores.children:
            if sensor.ids.checkbox.active:
                cols.append(sensor.id)
        for sensor in self.ids.sensores2.children:
            if sensor.ids.checkbox.active:
                cols.append(sensor.id)
        for sensor in self.ids.sensores3.children:
            if sensor.ids.checkbox.active:
                cols.append(sensor.id)
        if init_t is None or final_t is None or len(cols)==0:
            return
        cols.append('timestamp')
        self._lock.acquire()
        dados = self._session.query(DadosIndustria).filter(DadosIndustria.timestamp.between(init_t,final_t))
        self._lock.release()
        if dados is None:
            return
        self.ids.graph.clearPlots()
        result = [obj.get_attr_printable_list() for obj in dados]
        d=0
        for key,value in result[0].items():
            aux = []
            if key in cols:
                for i in range(len(result)):
                    if key in cols:
                        if key == 'timestamp':
                            continue
                        p = LinePlot(line_width =1.5, color = self._tags[key]['color'])
                        aux.append((i,result[i][key]))
                        p.points = aux
                        self.ids.graph.add_plot(p)
            d+=1
        self.ids.graph.xmax = len(result[d])
        timestamp = []
        for j in range(d):
            timestamp.append(datetime.strptime(result[d]['timestamp'],"%d/%m/%Y %H:%M:%S.%f"))
        self.ids.graph.update_x_labels(timestamp)
        # print(dados)

    def config_filter(self):
        self._modbusClient.write_single_coil(self._tags['filtro_est_1']['addr'],self.ids.filtro_1.active)
        self._modbusClient.write_single_coil(self._tags['filtro_est_2']['addr'],self.ids.filtro_2.active)
        self._modbusClient.write_single_coil(self._tags['filtro_est_3']['addr'],self.ids.filtro_3.active)
        
        self._modbusClient.write_single_register(self._tags['filtro_cor_r_1']['addr'],255*self.ids.filtro_r_1.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_g_1']['addr'],255*self.ids.filtro_g_1.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_b_1']['addr'],255*self.ids.filtro_b_1.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_r_2']['addr'],255*self.ids.filtro_r_2.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_g_2']['addr'],255*self.ids.filtro_g_2.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_b_2']['addr'],255*self.ids.filtro_b_2.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_r_3']['addr'],255*self.ids.filtro_r_3.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_g_3']['addr'],255*self.ids.filtro_g_3.active)
        self._modbusClient.write_single_register(self._tags['filtro_cor_b_3']['addr'],255*self.ids.filtro_b_3.active)

        self._modbusClient.write_single_register(self._tags['filtro_massa_1']['addr'],int(self.ids.filtro_massa_1.text))
        self._modbusClient.write_single_register(self._tags['filtro_massa_2']['addr'],int(self.ids.filtro_massa_2.text))
        self._modbusClient.write_single_register(self._tags['filtro_massa_3']['addr'],int(self.ids.filtro_massa_3.text))

    def config_frequencia(self):
        self._modbusClient.write_single_register(800,int(self.ids.motor_freq.text))

    def on_off(self):
        self._modbusClient.write_single_coil(802,not(self.ids.on_switch.active))

    def actuator_state(self):
        self._modbusClient.write_single_coil(801,self.ids.obj_switch.active)

    def graph_massa_setup(self):
        self.plot = LinePlot(line_width = 1.2, color = self._tags['peso_obj']['color'])
        self.ids.mass_graph.add_plot(self.plot)

    def grap_RGB_setup(self):
        self.Rplot = LinePlot(line_width = 1.2, color = self._tags['cor_obj_R']['color'])
        self.Gplot = LinePlot(line_width = 1.2, color = self._tags['cor_obj_G']['color'])
        self.Bplot = LinePlot(line_width = 1.2, color = self._tags['cor_obj_B']['color'])
        self.ids.RGB_graph.add_plot(self.Rplot)
        self.ids.RGB_graph.add_plot(self.Gplot)
        self.ids.RGB_graph.add_plot(self.Bplot)

    def get_printable_info(self):
        self.ids.tensao.text = 'Tensao: ' + str(self._meas['values']['tensao'])
        self.ids.corrente.text = 'Corrente RMS: ' + str(self._meas['values']['corrente'])
        self.ids.pot_entrada.text = 'Potencia: ' + str(self._meas['values']['pot_entrada'])
        self.ids.vel_esteira.text = 'Velocidade esteira: ' + str(self._meas['values']['vel_esteira'])
        self.ids.rotacao.text = 'Rotacao motor: ' + str(self._meas['values']['rotacao'])
        self.ids.temp_estator.text = 'Temperatura estator: ' + str(self._meas['values']['temp_estator'])

    def create_histgraph_checkbox(self):
        i=0
        for key,value in self._tags.items():
            cb = LabelCheckboxHistGraph()
            cb.ids.label.text = key
            cb.ids.label.color = value['color']
            cb.id = key
            if i<=12:
                self.ids.sensores.add_widget(cb)
            elif i>12 and i<=24:
                self.ids.sensores2.add_widget(cb)
            else:
                self.ids.sensores3.add_widget(cb)
            i+=1

    def parseDTString(self, datetime_str):
        try:
            d = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
            return d
        except Exception as e:
            print("Erro: ", e.args)
class LabelCheckboxHistGraph(BoxLayout):
    pass