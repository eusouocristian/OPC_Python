import OpenOPC
import pywintypes

class Connection:
   
    def __init__(self):
        pywintypes.datetime = pywintypes.TimeType
        self.opc = OpenOPC.client()

        if self.opc.servers()[0]:
            self.opc.connect(self.opc.servers()[0])
            self.server = self.opc.servers()[0]
            
            print('OPC Server Conectado')
            print('Servidor: {}'.format(self.opc.servers()[0])) 
        else:
            print('Nenhum servidor encontrado')

class ReadValues(Connection):
    def __init__(self):
        super().__init__()

    def printall(self):
        lista_fancoils = ['FC01']
        lista_tags = self.opc.list(lista_fancoils[0])
        for tag in lista_tags:
            value, quality, time = self.opc.read(lista_fancoils[0]+'.'+tag+'.Value')
            print('{}.{}: {}'.format(lista_fancoils[0], tag, value))

### from ConnectOPC import ReadValues
### valores = ReadValues()
### valores.printall()
