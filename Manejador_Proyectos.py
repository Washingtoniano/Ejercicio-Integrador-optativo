import csv
from Proyecto import proyecto
class ManPro():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def leer (self):
        archivo=open("proyectos.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for Fila in reader:
            if band ==False:
                band= True
            else:
                unproyecto=proyecto(Fila[0],Fila[1],Fila[2])
                self.__indice.append(unproyecto)
        archivo.close()
    def mostrar(self):
        self.ordenar()
        ca=0
        for Proyecto in self.__indice:
            ca=ca+1
            print(Proyecto)
        return ca
    def ordenar(self):
        self.__indice.sort()
    def listar(self):
        for elemento in self.__indice:
            for elemento2 in self.__indice:
                if elemento2>elemento:
                    aux=elemento
                    elemento=elemento2
                    elemento2=aux
    def puntaje(self,integrantes,Director,CategoriaDIR,Codirector,CategoriaCO):
        for proyecto in self.__indice:
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





