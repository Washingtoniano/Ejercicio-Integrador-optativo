class proyecto():
    __idProyecto=''
    __titulo=''
    __palabaraC=''
    __puntaje=0
    def __init__(self,id,ti,pa):
        self.__ide=id
        self.__titulo=ti
        self.__palabrasC=pa
        self.__puntaje=0
    def __gt__(self, other):
        return self.__puntaje>other.__puntaje
    def __str__(self):
        return("IdProyecto:{}-Titulo:{}-PalabraClave:{}-Puntaje:{}".format(self.__ide,self.__titulo,self.__palabrasC,self.__puntaje))
    def obtener_puntaje(self,puntos):
        self.__puntaje=self.__puntaje+puntos
    def id(self):
        return self.__ide
    def puntaje(self):
        return self.__puntaje
