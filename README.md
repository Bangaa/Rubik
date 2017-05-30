# Laboratorio 3: Sistemas de comunicación

## Instalación

Solo basta con ejecutar el script de python. El programa buscará e instalará 
los módulos faltantes.


## Encriptar

Para encriptar se necesitan 3 parámetros.

1. **e**: opción para encriptar
2. **ARCHIVO**: El archivo que se quiere encriptar. Este tiene que ser 
   compuesto únicamente por carácteres ASCII.
3. **CLAVE**: Es la clave (o llave) que se usa para encriptar el archivo.

    python alg.py e ARCHIVO CLAVE
    
    # ejm

    python alg.py e mensaje.txt "qwertyuiop"


## Desencriptar

Lo único que cambia con respecto a la encriptación es la opción `e` (encriptar) 
por `d` (desencriptar)

    # ejm
    python alg.py d mensaje_encriptado.txt "qwertyuiop"
