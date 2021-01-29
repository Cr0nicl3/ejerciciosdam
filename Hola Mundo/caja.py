import animal
class caja:
    def __init__(self, *animales,lastid):
        self.animales=animal(animales)
        self.id=lastid+1
    
    def __str__(self):
        print("Id: "+self.id)
        for i in range(self.animales.__len__()):
            self.animales[i].__str__()

    def animales_por_patas(self,numero_patas):
        for i in range(self.animales.__len__()):
            if(self.animales[i].__str__())