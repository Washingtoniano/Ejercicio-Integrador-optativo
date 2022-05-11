import numpy
import numpy as np
import csv
from Integrantes import integrantes
class Man_In():
    __cantidad=0
    __dimension=0
    __incremento=1
    def __init__(self,dimension,incremento=1):
        self.__integrantes= np.empty(dimension,dtype=integrantes)
        self.__dimension=dimension
        self.__cantidad=0
    def leer (self):
        archivo=open("integrantesProyecto.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        band=False
        for Fila in reader:
            if band==False:
                band=True
            else:
                if(self.__cantidad==self.__dimension):
                    self.__dimension+=self.__incremento
                    self.__integrantes.resize(self.__dimension)
                unintegrante=integrantes(Fila[0],Fila[1],Fila[2],Fila[3],Fila[4])
                self.__integrantes[self.__cantidad]=unintegrante
                self.__cantidad+=1
        archivo.close()
    def dimension(self):
        return(self.__integrantes)
    def mostrar(self):
        for i in range (len(self.__integrantes)):
            print (self.__integrantes[i])


