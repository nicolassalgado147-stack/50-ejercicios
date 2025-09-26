# Nicolas Salgado
class tuplalista:
    def __init__(self):
        self.tupla = ("1", "2", "3", "4")

    def convertir(self):
        lista = list(self.tupla)
        print("Tupla", self.tupla)
        print("lista", lista)


obj4 = tuplalista()
obj4.convertir()
