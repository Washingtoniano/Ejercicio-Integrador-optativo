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
        self.lista()
        for Proyecto in self.__indice:

            print(Proyecto)
    def ordenar(self):
        self.__indice.sort()
    def listar(self):
        for elemento in self.__indice:
            for elemento2 in self.__indice:
                if elemento2>elemento:
                    aux=elemento
                    elemento=elemento2
                    elemento2=aux
    def comprobar(self,arr):
        for i in range (len(self.__indice)):
            cant=0
            DirectorIoII=False
            Director=False
            Codirector=False
            CodirectorI_IIoIII=False
            for j in range(len(arr)):
                if self.__indice[i].id()==arr[j].id():
                    cant=cant+1
                    if (arr[j].rol()=='director'):
                        Director=True
                        if (arr[j].categoria())=='I' or (arr[j].categoria())=='II'or (arr[j].categoria())=='III'or (arr[j].categoria())=='IV':
                            DirectorIoII=True
                    elif (arr[j].rol()=='codirector'):
                        Codirector=True
                        if (arr[j].categoria()=='I') or (arr[j].categoria()=='II') or (arr[j].categoria()=='III')or (arr[j].categoria()=='IV'):
                            CodirectorI_IIoIII=True
            self.__indice[i].obtener_puntaje(cant,Director,DirectorIoII,Codirector,CodirectorI_IIoIII)

    def lista(self):
        return self.__indice
