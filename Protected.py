class ProVar:
    def __init__(self):
        self._provar = 10
        self.__privar = 20

    def printprovar(self):
        print(self._provar)

    def printprivar(self):
        print(self.__privar)

    def setprovar(self, prot):
        self._provar = prot

    def setprivar(self, priv):
        self.__privar = priv

obj = ProVar()
obj.printprovar()
obj.printprivar()
obj.setprovar(25)
obj.setprivar(55)
obj.printprovar()
obj.printprivar()
