class animal:
    def __init__(self,color, numpatas,especie):
        self.color=color
        self.numpatas=numpatas
        self.__name__=especie
        
    
    def tostring(self):
        print(self.color+" "+self.numpatas+" "+self.__name__)
    