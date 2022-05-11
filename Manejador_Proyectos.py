import csv
from Proyecto import proyecto
from Manejador_Integrantes import Man_In
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

    def lista(self):
        return self.__indice
