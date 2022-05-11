from Manejador_Integrantes import Man_In
from Manejador_Proyectos import ManPro
if __name__ == '__main__':
    maneI=Man_In(11)
    maneP=ManPro()
    maneP.leer()
    maneI.leer()
    li=maneP.lista()
    arr=maneI.dimension()
    for i in range (len(li)):
        cant=0
        DirectorIoII=False
        Director=False
        Codirector=False
        CodirectorI_IIoIII=False
        for j in range(len(arr)):
            if li[i].id()==arr[j].id():
                cant=cant+1
            if (arr[j].rol()=='director'):
                Director=True
                if (arr[j].categoria())=='I' or (arr[j].categoria())=='II':
                    DirectorIoII=True
            elif (arr[j].rol()=='codirector'):
                Codirector=True
                if (arr[j].categoria()=='I') or (arr[j].categoria()=='II') or (arr[j].categoria()=='III'):
                    CodirectorI_IIoIII=True
        li[i].obtener_puntaje(cant,Director,DirectorIoII,Codirector,CodirectorI_IIoIII)
    maneI.mostrar()
    maneP.mostrar()


