from kivymd.uix.screen import MDScreen
from pyModbusTCP.client import ModbusClient
from kivymd.uix.snackbar import Snackbar
class MyWidget(MDScreen):
    def __init__(self,**kw):
        super().__init__(**kw)
        self._scan_time = 1000
        #TODO: pensar se usaremos coneccao sera feita por pop up(semana 13_14 linhas 22 a 27 mainWidget) ou nao
        self._modbusClient = ModbusClient()
        

    def connect(self):
        """
        Conexao com Servidor modbus
        """
        if self.ids.bt_con.text =='CONECTAR':
            self.ids.bt_con.text = "DESCONECTAR"
            try:
                self._modbusClient.host = self.ids.hostname.text
                self._modbusClient.port = int(self.ids.port.text)
                self._modbusClient.open()
                Snackbar(text = "Conexao realizada com sucesso",bg_color=(0,1,0,1)).open()
                # print("Tensao: ",self._modbusClient.read_holding_registers(801,1)[0])  #linha para teste de conexao com o servidor
            except Exception as e:
                print("Erro: ",e.args)
        else:
            self.ids.bt_con.text = "CONECTAR"
            self._modbusClient.close()
            Snackbar(text="Cliente desconectado",bg_color=(1,0,0,1)).open()

    def startDataRead(self,ip,port):
        """
        Metodo utilixado para a configuracao do IP e porta do servidor MODBUS e
        inicializar uma thread para a leitura dos dados e atualizacao da interface
        """
        pass

    def updater(self):
        """
        Invoca leitura de dados, atualizacao da interface e insercao de dados na DB
        """
        pass

    def readData(self):
        """
        Metodo para a leitura dos dados por meio do protocolo MODBUS
        """
        pass

    def updateGUI(self):
        """
        Atualizacao da inteface de usuario
        """
        pass

