import os

def mostrar_menu():
    print("Comandaments disponibles, per a Ubuntu:")
    print("1: Llistar directoris (ls)")
    print("2: Veure directori actual (pwd)")
    print("3: Canviar de directori (cd)")
    print("4: Crear un directori (mkdir)")
    print("5: Sortir")

def llistar_directoris():
    os.system('ls')

def veure_directori_actual():
    print(os.getcwd())

def canviar_directori():
    nou_directori = input("Introdueix el nou directori: ")
    try:
        os.chdir(nou_directori)
        print("Directori canviat a " + os.getcwd())
    except FileNotFoundError:
        print("El directori no existeix")

def crear_directori():
    nou_directori = input("Introdueix el nom del nou directori: ")
    try:
        os.mkdir(nou_directori)
        print("Directori creat: " + nou_directori)
    except FileExistsError:
        print("El directori ja existeix")

def main():
    while True:
        mostrar_menu()
        opció = input("Introdueix el número de comandament que vols executar: ")

        if opció == '1':
            llistar_directoris()
        elif opció == '2':
            veure_directori_actual()
        elif opció == '3':
            canviar_directori()
        elif opció == '4':
            crear_directori()
        elif opció == '5':
            print("Sortint...")
            break
        else:
            print("Opció no reconeguda. Si us plau, intenta de nou.")

        input("Prem Enter per continuar...")

if __name__ == "__main__":
    main()
