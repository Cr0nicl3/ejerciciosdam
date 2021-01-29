import animal
class caja:
    staticid=0
    def __init__(self,lastid,*animales):
        self.animales= []
        for i in animales:
            animales+=i
        self.id=staticid
        staticid+=1
    
    def __str__(self):
        string=string+"Id: "+self.id        
        for i in self.animales:
            string=string+i.__str__()
        return string

    def animales_por_patas(self,numero_patas):
        lista=[]
        for i in animales:
            if(animales.patas==numero_patas)lista+=i
        return lista