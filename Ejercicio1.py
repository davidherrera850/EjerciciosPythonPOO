import random
class Persona():
    def __init__(self,nombre="",edad=0,sexo="F", peso=0, altura=0):
        self.__nombre=nombre
        self.__edad=edad
        self.__sexo=sexo
        self.__peso=peso
        self.__altura=altura

    def calcularIMC(self):
        imc=int(self.__peso) / pow(int(self.__altura),2)
        if(imc>0 and imc<18.5):
            return -1
        if(imc>18.5 and imc<24.9):
            return 0
        if (imc > 25 and imc < 29.9):
            return 1

    def mayordedad(self):
        if(int(self.__edad)<18):
            return False
        if (int(self.__edad) >= 18):
            return True

    def introducirsexo(self):
        if(self.__sexo!= 'H' or self.__sexo !='M'):
            sexo="M"

    def __str__(self):
        return "Nombre:" + str(self.__nombre) + ", Edad:" + str(self.__edad)+ ", Sexo:" + str(self.__sexo)+  "peso: " + str(self.__peso) + ", Altura (cm):" + str(self.__altura)

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getSexo(self):
        return self.__sexo

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def setPreciobase(self, preciobase):
         self.__preciobase=preciobase

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setSexo(self,sexo):
        self.__sexo=sexo

    def setPeso(self,peso):
        self.__peso=peso

    def setAltura(self,altura):
        self.__altura=altura

    def generarDNI(self):
        numero = ""
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L',
                 'C', 'K', 'E']
        for i in range(8):
            numero += str(random.randint(0, 9))
        letra = lista[int(numero) % 23]
        dni =numero + letra
        print(dni)

if __name__ == "__main__":
    p1=Persona(nombre=input("Introduce el nombre:"),edad=input("Introduce la edad:"),sexo=input("Introduce el sexo (H / M):"),peso=input("Introduce el peso:"),altura=input("Introduce la altura:"))

    if p1.calcularIMC() == (-1):
        print("Esta por debajo de su peso")
    if p1.calcularIMC() == 0:
        print("Peso ideal")
    if p1.calcularIMC() ==1:
        print("Esta por encima de su peso")

    if not p1.mayordedad():
        print("Es menor de edad")
    if p1.mayordedad() :
        print("Es mayor de edad")
    print(p1)

    p2 = Persona(nombre=input("Introduce el nombre:"), edad=input("Introduce la edad:"),sexo=input("Introduce el sexo (H / M):"))

    if p1.calcularIMC() == (-1):
        print("Esta por debajo de su peso")
    if p1.calcularIMC() == 0:
        print("Peso ideal")
    if p1.calcularIMC() == 1:
        print("Esta por encima de su peso")

    if not p2.mayordedad():
        print("Es menor de edad")
    if p2.mayordedad():
        print("Es mayor de edad")
    print(p2)

    p3=Persona()













