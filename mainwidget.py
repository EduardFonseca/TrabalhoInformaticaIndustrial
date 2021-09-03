from kivymd.uix.screen import MDScreen
from pyModbusTCP.client import ModbusClient
from kivymd.uix.snackbar import Snackbar
from threading import Thread, Lock
class MyWidget(MDScreen):

    _updateThread = None
    _updateWidget = True #TODO: verificar a necissidade de transformar em false principalmente ao desconectar do servidor

    def __init__(self,**kw):
        super().__init__(**kw)
        self._scan_time = 1000
        self._lock=Lock()
        #TODO: pensar se usaremos coneccao sera feita por pop up(semana 13_14 linhas 22 a 27 mainWidget) ou nao
        self._modbusClient = ModbusClient()


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
                print("Tensao: ",self._modbusClient.read_holding_registers(801,1)[0])  #linha para teste de conexao com o servidor
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
            self.readData()
            self.updateGUI()
            self._lock.acquire()
            # TODO: Fazer o update dos dados na DB com a session
            self._lock.release()

        except Exception as e:
            print("Erro: ", e.args)


    def stopRefresh(self):
        self._updateWidget=False

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

