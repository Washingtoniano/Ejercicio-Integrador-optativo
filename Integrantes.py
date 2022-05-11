class integrantes ():
    __idproyecto=0
    __ApellidoNombre=''
    __DNI=0
    __Categoria=''
    __rol=''
    def __init__ (self,id,AN,DNI,Categoria,rol):
        self.__idproyecto=id
        self.__ApellidoNombre=AN
        self.__DNI=DNI
        self.__Categoria=Categoria
        self.__rol=rol
    def __str__(self):
        return ("IdProyecto:{}-Apellido Nombre:{}-DNI:{}-Categoria:{}-Rol:{}".format(self.__idproyecto,self.__ApellidoNombre,self.__DNI,self.__Categoria,self.__rol))

    def id(self):
        return (self.__idproyecto)
    def categoria(self):
        return self.__Categoria
    def rol(self):
        return (self.__rol)
