# Tabla de conversion

class ConversionTable:

    def __init__(self,clave):
        self.__alf__ = list("abdchgefpomnijlk ?;\nyz,.xwuvqrts")
        self.__dicc__ = {}
        self.__clave__ = clave.lower()
        i = 0
        for letra in self.__alf__:
            self.__dicc__[letra] = i
            i += 1

        i = 0
        for letra in self.__clave__:
            ilet = self.__alf__[i]
            ipos = self.__dicc__[ilet]

            jlet = letra
            jpos = self.__dicc__[jlet]

            # cambio de posicion en alfabeto
            self.__alf__[ipos] = jlet
            self.__alf__[jpos] = ilet

            # cambio de posicion en diccionario
            self.__dicc__[ilet] = jpos
            self.__dicc__[jlet] = ipos
            i += 1
    def get(self, arg):
        tipo = type(arg)
        try:
            if tipo is str:
                return self.__dicc__[arg]
            elif tipo is int:
                return self.__alf__[arg]
        except:
            if tipo is str: 
                return -1
            else:
                return "~"


    def __str__(self):
        table_str = ""
        for letra in self.__alf__:
            table_str += "%c : %d\n" % (letra, self.__dicc__[letra])

        return table_str
