import os

dirActual =os.getcwd() # Per saber el directori actual
print("El directori actual és: {}".format(dir(dirActual)))

# Crear un directori si no existeix
carpeta = str(input("\nIntrodueix el directori a crear: "))
# Comprovar si existeix
if os.path.exists(carpeta):
    print("La carpeta {} ja existeix".format(carpeta))
    exit(1)
else:
    os.system("mkdir {}".format(carpeta))
    # Per veure un llistat del directori on s'ha creat ara mateix esta carpeta
    cpath = carpeta.split("/")[0:1] #Seleccionem totes menos la creada

