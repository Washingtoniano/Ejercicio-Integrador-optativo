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
