class Serie():
    def  __init__ (self, titulo="", temporadas=3, entregado=False, genero="", creador=""):
        self.titulo=titulo
        self.temporadas=temporadas
        self.entregado=entregado
        self.genero=genero
        self.creador=creador

    def __str__(self):
        return "Titulo:" + self.titulo + "Temporadas:" + str(self.temporadas) + "Genero:" + self.genero + "Creador:" + self.creador

    def getTitulo(self):
        return self.titulo

    def getTemporadas(self):
        return self.temporadas

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador

    def setTitulo(self, titulo):
         self.titulo=titulo

    def setTemporadas(self, temporadas):
        self.temporadas=temporadas

    def setGenero(self, genero):
        self.genero=genero

    def setCreador(self, creador):
        self.creador=creador


class Videojuego():
    def  __init__ (self, titulo ="", horaestimadas=10, entregado=False, genero="", compania=""):
        self.titulo=titulo
        self.horaestimadas=horaestimadas
        self.entregado=entregado
        self.genero=genero
        self.compania=compania

    def __str__(self):
        return "Titulo:"+self.titulo + "Horas estimadas:" + str(self.horaestimadas) + "Genero:" + self.genero + "Compañía:" + self.compania

    def getTitulo(self):
        return self.titulo

    def getHoraestimadas(self):
        return self.horaestimadas

    def getGenero(self):
        return self.genero

    def getCompania(self):
        return self.compania

    def setTitulo(self, titulo):
         self.titulo=titulo

    def setHoraestimadas(self, horaestimadas):
        self.horaestimadas=horaestimadas

    def setGenero(self, genero):
        self.genero=genero

    def setCompania(self, compania):
        self.compania=compania

if __name__ == "__main__":
    lserie=[]
    lvideojuego=[]

    serie1=Serie("Uno", 3, False, "amor", "pepito")
    lserie.append(serie1)
    serie2=Serie("dos", 5, False, "futbol","manolo")
    lserie.append(serie2)
    serie3=Serie("tres", 9, False, "accion", "lola")
    lserie.append(serie3)
    serie4=Serie("cuatro", 1, True, "terror", "pepe")
    lserie.append(serie4)
    serie5=Serie("cinco", 7, True, "muerte", "juan")
    lserie.append(serie5)
    videoj1=Videojuego("fifa22", 24, True, "futbol", "EaSport")
    lvideojuego.append(videoj1)
    videoj2=Videojuego("rayman", 12, False, "accion", "ppp")
    lvideojuego.append(videoj2)
    videoj3=Videojuego("sony", 14, True, "correr", "ticj")
    lvideojuego.append(videoj3)
    videoj4=Videojuego("mario", 50, False, "aventura", "nintendo")
    lvideojuego.append(videoj4)
    videoj5=Videojuego("sims", 30, False, "rollo", "aaa")
    lvideojuego.append(videoj5)
    serieMax =0
    juegoMax =0
    devuelta=0

    for i in range(0,len(lserie)):
        if lserie[i].temporadas > serieMax:
            serieMax = lserie[i].temporadas
        print(lserie[i].__str__())


    for i in range(0,len(lvideojuego)):
        if lvideojuego[i].horaestimadas > juegoMax:
            juegoMax = lvideojuego[i].horaestimadas
        print(lvideojuego[i].__str__())


    print(serieMax)
    print(juegoMax)