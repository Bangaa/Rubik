# Tabla de conversion

class ConversionTable:

    def __init__(self,clave):
        self.__alf = list("abdchgefpomnijlk ?;\nyz,.xwuvqrts")
        self.__dicc = {}
        self.__clave = clave.lower()
        i = 0
        for letra in self.__alf:
            self.__dicc[letra] = i
            i += 1

        i = 0
        for letra in self.__clave:
            ilet = self.__alf[i]
            ipos = self.__dicc[ilet]

            jlet = letra
            jpos = self.__dicc[jlet]

            # cambio de posicion en alfabeto
            self.__alf[ipos] = jlet
            self.__alf[jpos] = ilet

            # cambio de posicion en diccionario
            self.__dicc[ilet] = jpos
            self.__dicc[jlet] = ipos
            i += 1
    def get(self, arg):
        tipo = type(arg)
        try:
            if tipo is str:
                return self.__dicc[arg]
            elif tipo is int:
                return self.__alf[arg]
        except:
            if tipo is str: 
                return -1
            else:
                return "~"


    def __str__(self):
        table_str = ""
        for letra in self.__alf:
            table_str += "%c : %d\n" % (letra, self.__dicc[letra])

        return table_str
