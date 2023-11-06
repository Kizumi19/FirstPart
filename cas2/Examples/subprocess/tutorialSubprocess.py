import subprocess

output = subprocess.check_output(['df', '-h'])
for fich in output.decode().splitlines()[1:]:
    datos = fich.split()
    # Elimina les cadenes de la llista dades, per evitar que peti el programa
    datos = [dato for dato in datos if dato]

    # Utiliza format per imprimir els valores que volem
    print('{} - {}'.format(datos[0], datos[4]))
