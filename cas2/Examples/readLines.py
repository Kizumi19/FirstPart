import os.path
ruta = os.path.join(os.getcwd(), "demofile.txt")
comprovar = os.path.isfile(ruta)

def comprovacio():
    comprovar = os.path.isfile(ruta)
    if comprovar == False:
        with open(ruta, "a+") as f:
            print(f.readline())
    else:
        with open(ruta, "r") as f:
            print(f.readline())

comprovacio()