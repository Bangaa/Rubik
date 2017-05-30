
import MatEncriptor as ME
import ConversionTable as CT
import sys

if len(sys.argv) == 1:
    filename = raw_input("Archivo entrada: ")
    clave = raw_input("Clave (key): ")
elif len(sys.argv) == 3:
    filename = sys.argv[1]
    clave = sys.argv[2]

ct = CT.ConversionTable(clave)
enc = ME.MatEncriptor(ct)

try:
    enc_txt = enc.encriptar(open(filename).read())
    print enc_txt
except IOError as ioe:
    print "ERROR: No se encuentra el archivo '%s'" % (filename)
