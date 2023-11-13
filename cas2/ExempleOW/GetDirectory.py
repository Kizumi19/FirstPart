import os

# Per saber el directori actual
dirActual = os.getcwd()
print("El directori actual és: {}".format(dirActual))

# Crear un directori si no existeix
carpeta = input("\nIntrodueix el directori a crear: ")

# Comprovar si existeix
if os.path.exists(carpeta):
    print("La carpeta {} ja existeix".format(carpeta))
else:
    # Intentar crear la carpeta
    try:
        os.mkdir(carpeta)
        print("Carpeta '{}' creada correctament.".format(carpeta))
    except OSError as error:
        print("No s'ha pogut crear la carpeta '{}'".format(carpeta))
        print("Error: {}".format(error))

    # Per veure un llistat del directori on s'ha creat la carpeta
    cpath = os.path.abspath(carpeta)
    directori_mare = os.path.dirname(cpath)
    print("Directorio mare: {}".format(directori_mare))
    llistat = os.listdir(directori_mare)
    print("Llistat dels elements de {}:".format(directori_mare))
    for element in llistat:
        print(" - {}".format(element))

exit(0)

