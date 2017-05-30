
import MatEncriptor as ME
import ConversionTable as CT

txt = raw_input("Texto: ")

ct = CT.ConversionTable("Murcielago")
ct2 = CT.ConversionTable("qwertyuioasdfghjklzxcvbnm")

enc = ME.MatEncriptor(ct)
enc2 = ME.MatEncriptor(ct2)

me = enc.encriptar(txt)
me2 = enc2.encriptar(txt)
print me
print me2
