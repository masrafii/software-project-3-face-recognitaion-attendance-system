class Devices:
    def __init__(self,name):
        self.name=name
        


    def excessury(self):
        pass


class Smartphone(Devices):
    def __init__(self):
        pass

class Samsung(Smartphone):
    def __init__(self,name):
        self.__init__(name)
        


c1=Samsung("Electric")
print(c1.Samsung)
