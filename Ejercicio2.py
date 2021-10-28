class Electrodomestico():
    def  __init__ ( self , preciobase=100 , color="blanco" , consumo='F' , peso=5 ):
        self.preciobase=preciobase
        self.color=color
        self.consumo=consumo
        self.peso=peso

    def getPreciobase(self):
        return self.preciobase

    def getColor(self):
        return self.color

    def getConsumo(self):
        return self.consumo

    def getPeso(self):
        return self.peso

    def setPreciobase(self, preciobase):
         self.preciobase=preciobase

    def setColor(self, color):
        self.color=color

    def setConsumo(self, consumo):
        self.consumo=consumo

    def setPeso(self, peso):
        self.peso=peso

    def  precioFinal ( self ):
        if(self.consumo=='A'):
            preciobase=self.preciobase+100
        if(self.consumo=='B'):
            preciobase=self.preciobase+80
        if(self.consumo =='C'):
            preciobase=self.preciobase+60
        if(self.consumo =='D'):
            preciobase=self.preciobase+50
        if(self.consumo=='E'):
            preciobase=self.preciobase+30
        if(self.consumo =='F'):
            preciobase=self.preciobase+10

        if(0<self.peso<20):
            preciobase=self.preciobase+10
        if(20<self.peso<49):
            preciobase=self.preciobase+50
        if(50<self.peso<79):
            preciobase=self.preciobase+80
        if(self.peso<80):
            preciobase=self.preciobase+100

    def comprobarConsumoEnergetico(self, letra ):
        if(self.consumo=="A" or "B" or "C" or "D" or "E" or "F" ):
            consumo=letra
        if(self.consumo!="A" or "B" or "C" or "D" or "E" or "F"):
            consumo="F"

    def comprobarColor(self, color ):
        if(self.color=="blanco" or "negro" or "rojo" or "azul" or "gris"):
            color=color
        if(self.color!="blanco" or "negro" or "rojo" or "azul" or "gris"):
            color="blanco"

    def __str__(self):
        return "Precio:" + str(self.preciobase) + "Color:" + str(self.color) + "Consumo Energía:" + str(self.consumo) + "Peso:" + str(self.peso)


class Lavadora(Electrodomestico):
    def __init__(self, preciobase=100, color="blanco", consumo='F', peso=5, carga = 5):
        super().__init__(preciobase, color, consumo, peso)
        self.carga = carga

    def getCarga(self):
        return self.carga

    def setCarga(self, carga):
         self.carga=carga

    def precioFinal(self):
        Electrodomestico.precioFinal
        if(self.carga>30):
            preciobase =self.preciobase+50

    def __str__(self):
        return super().__str__() + " | Carga :" + str(self.carga)

class Televisión(Electrodomestico):
    def __init__(self, preciobase=100, color="blanco", consumo='F', peso=5, resolucion = 20, cuatroK =False):
        super(). __init__ (preciobase, color, consumo, peso)
        self.resolucion =resolucion
        self.cuatroK=cuatroK

    def getResolucion(self):
        return self.resolucion

    def setResolucion(self, resolucion):
         self.resolucion=resolucion
    def getCuatroK(self):
        return self.cuatrok

    def setCuatroK(self, cuatrok):
         self.cuatrok=cuatrok

    def  precioFinal ( self ):
        Electrodomestico.precioFinal
        if(self.resolucion>40):
            preciobase=self.preciobase*1.3
        if(self.cuatroK==True):
            preciobase=self.preciobase+50

    def __str__(self):
        return super().__str__() + "Resolución:" + str(self.resolucion)

if __name__ == "__main__":
    lelectro = []

    electrodomestico1 = Electrodomestico(200,"blanco",'F', 5)
    lelectro.append(electrodomestico1)
    electrodomestico2 = Electrodomestico(300, "rojo", 'A', 10)
    lelectro.append(electrodomestico2)
    electrodomestico3 = Electrodomestico(400, "azul", 'B', 15)
    lelectro.append(electrodomestico3)
    electrodomestico4 = Electrodomestico(100, "negro", 'D', 3)
    lelectro.append(electrodomestico4)
    lavadora1 = Lavadora(200, "blanco", 'F', 5,7)
    lelectro.append(lavadora1)
    lavadora2 = Lavadora(200, "azul", 'E', 15, 8)
    lelectro.append(lavadora2)
    lavadora3 = Lavadora(200, "rojo", 'D', 4, 5)
    lelectro.append(lavadora3)
    tele1 = Televisión(500, "blanco", 'F', 5, 20, True)
    lelectro.append(tele1)
    tele2 = Televisión(200, "azul", 'B', 5, 7, False)
    lelectro.append(tele2)
    tele3 = Televisión(400, "negro", 'C', 13, 5, True)
    lelectro.append(tele3)

    for x in range(0,len(lelectro)):
        print(lelectro[x])