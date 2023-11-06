import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'

print("Ruta de origen:", origen)
print("Ruta de destino:", destino)

try:
    shutil.copyfile(origen, destino)
    print('Archivo copiado')
    # Saber qué errores pueden passar
except FileNotFoundError:
    print('El archivo de origen no fue encontrado.')
except PermissionError:
    print('Problema de permisos al acceder a los archivos.')
except Exception as e:
    print('Error:', e)
