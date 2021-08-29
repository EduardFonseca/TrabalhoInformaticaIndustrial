from kivymd.uix.screen import MDScreen
from pyModbusTCP.client import ModbusClient

class MyWidget(MDScreen):
    def __inir__(self,**kwargs):
        super.__init__()
        #TODO: Verificar como **kwargs funciona em relacao ao **kw
        self._scan_time = kwargs.get('scan_time')
        self._serverIP = kwargs.get('server_ip')
        self._port = kwargs.get('server_port')
        #TODO: pensar se usaremos coneccao sera feita por pop up(semana 13_14 linhas 22 a 27 mainWidget) ou nao
        self._modbusClient = ModbusClient(host = self._serverIP, port= self._port)

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

