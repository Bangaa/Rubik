
import MatEncriptor as ME
import ConversionTable as CT
import sys

def encriptarArchivo(clave, filename):
    ct = CT.ConversionTable(clave)
    enc = ME.MatEncriptor(ct)

    archivo = open(filename, "r")
    txt = archivo.read()
    archivo.close()

    archivo = open(filename+".cif", "w")
    archivo.write(enc.encriptar(txt))
    archivo.close()

def desencriptarArchivo(clave, filename):
    ct = CT.ConversionTable(clave)
    enc = ME.MatEncriptor(ct)

    archivo = open(filename, "r")
    txt = archivo.read()
    archivo.close()

    archivo = open(filename+".des", "w")
    archivo.write(enc.desencriptar(txt))
    archivo.close()


filename = ""
clave = ""
encriptar = True

if len(sys.argv) < 4:
    filename = raw_input("Archivo entrada: ")
    clave = raw_input("Clave (key): ")
    if raw_input("Encriptar o desencriptar [e/d]: ") == "e":
        encriptar = True
    else:
        encriptar = False

else:
    if sys.argv[1] == "e":
        encriptar = True
    else:
        encriptar = False
    filename = sys.argv[2]
    clave = sys.argv[3]

try:

    if encriptar:
        encriptarArchivo(clave, filename)
    else:
        desencriptarArchivo(clave, filename)

except IOError as ioe:
    print "ERROR: No se encuentra el archivo '%s'" % (filename)
