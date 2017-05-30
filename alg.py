from math import sqrt,ceil
import numpy as np

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
        if type(arg) is str:
            return self.__dicc__[arg]
        elif type(arg) is int:
            return self.__alf__[arg]


    def __str__(self):
        table_str = ""
        for letra in self.__alf__:
            table_str += "%c : %d\n" % (letra, self.__dicc__[letra])

        return table_str


class MatEncriptor:

    def __init__(self,tablaConversion):
        self.ct = tablaConversion

    def __xor__(self, matriz):
        res = matriz[0]

        for fila in matriz[1:]:
            res = np.bitwise_xor(res, fila)

        return res

    def encriptar(self, texto):
        matriz = self.__matEnc__(texto)

        i = 0
        while i < len(matriz):
            self.__sustituir__(matriz, i)
            matriz = matriz.T
            i += 1

        lista = matriz.flatten().tolist()
        enctxt = ""

        for elem in lista:
            enctxt += self.ct.get(elem)

        return enctxt

    def desencriptar(self, texto):
        return


    def __matEnc__(self, text):
        matlen = int(ceil(sqrt(len(text))))

        enctxtlen = matlen**2

        if len(text) < matlen**2:
            text += " " * (enctxtlen - len(text))
        text = text.lower()

        mat = []

        i = 0
        while i < matlen:
            fila = list(text[i*matlen:(i+1)*matlen])

            j = 0
            while j < len(fila):
                char = fila[j]
                fila[j] = self.ct.__dicc__[char]
                j += 1
            mat.append(fila)
            i += 1 

        return np.array(mat)

    # Sustituye la fila 'index' de la matriz, con el XOR entre todas las filas 
    # de la matriz.
    def __sustituir__(self, matriz, index):

        nuevafila = self.__xor__(matriz)
        matriz[index] = nuevafila

        return matriz


txt = raw_input("Texto: ")

ct = ConversionTable("Murcielago")
ct2 = ConversionTable("qwertyuioasdfghjklzxcvbnm")

enc = MatEncriptor(ct)
enc2 = MatEncriptor(ct2)

me = enc.encriptar(txt)
me2 = enc2.encriptar(txt)
print me
print me2
