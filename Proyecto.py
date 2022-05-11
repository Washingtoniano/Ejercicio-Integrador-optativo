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
    def obtener_puntaje(self,integrantes,Director,CategoriaDIR,Codirector,CategoriaCO):
        puntos=0
        if integrantes>=3:
            puntos=puntos+10
        else:
            puntos=puntos-20
            print ("El proyecto debe tener como minimo 3 integrantes\n")
        if Director==True:
            if (CategoriaDIR==True):
                puntos=puntos+10
            else:
                puntos=puntos-5
                print ("El Director del Proyecto debe tener categoría I o II")
        else:
                print ("El proyecto debe tener un director\n")
        if Codirector==True:
            if(CategoriaCO==True):
                puntos=puntos+10
            else:
                puntos =puntos-5
                print ("El Codirector del Proyecto debe tener como mínimo categoría III")
        else:
            print ("El proyecto debe tener un codirector\n")
        if (Codirector==False and Director==False):
            puntos=puntos-10
        self.__puntaje=self.__puntaje+puntos
    def id(self):
        return self.__ide
    def puntaje(self):
        return self.__puntaje
