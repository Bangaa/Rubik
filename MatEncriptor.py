from math import sqrt,ceil
import numpy as np

# Encriptador

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
        matriz = self.__matEnc__(texto)

        i = len(matriz) - 1
        while i >= 0:
            matriz = matriz.T
            self.__sustituir__(matriz, i)
            i -= 1

        lista = matriz.flatten().tolist()
        enctxt = ""

        for elem in lista:
            enctxt += self.ct.get(elem)

        return enctxt.strip()



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
                fila[j] = self.ct.get(char)
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
