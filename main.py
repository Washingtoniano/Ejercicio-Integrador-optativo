from Manejador_Integrantes import Man_In
from Manejador_Proyectos import ManPro
if __name__ == '__main__':
    maneI=Man_In(11)
    maneP=ManPro()
    maneP.leer()
    maneI.leer()
    can=maneP.mostrar()
    for i in range (len( maneP)):
        cant=0
        DirectorIoII=False
        Director=False
        Codirector=False
        CodirectorI_IIoIII=False
        for Integra in maneI:
            if maneP[i].id()==Integra.id():
                cant=cant+1
            if (Integra.rol()=='director'):
                Director=True
                if (Integra.categoria())=='I' or (Integra.categoria())=='II':
                    DirectorIoII=True
            elif (Integra.rol()=='codirector'):
                Codirector=True
                if (Integra.categoria()=='I') or (Integra.categoria()=='II') or (Integra.categoria()=='III'):
                    CodirectorI_IIoIII=True
        maneP[i].puntaje(cant,Director,DirectorIoII,Codirector,CodirectorI_IIoIII)




