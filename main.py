from Manejador_Integrantes import Man_In
from Manejador_Proyectos import ManPro
if __name__ == '__main__':
    maneI=Man_In(11)
    maneP=ManPro()
    maneP.leer()
    maneI.leer()
    arr=maneI.dimension()
    li=maneP.comprobar(arr)
    maneP.mostrar()
    print("\n")
    maneI.mostrar()


