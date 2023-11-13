import os
import sys

def crear_docker_directori(nom_directori):
    ruta_opt = '/opt'
    ruta_final = os.path.join(ruta_opt, nom_directori)

    # Comprovar si el directori opt existeix
    if not os.path.exists(ruta_opt):
        print(f"El directori {ruta_opt} no existeix.")
        return
    
    # Creació del subdirectori
    if not os.path.exists(ruta_final):
        os.makedirs(ruta_final)
        print(f"Directori {ruta_final}")
    else:
        print(f"El directori {ruta_final} ja existeix.")

    # Creació de l'arxiu docker.compose.yml
    ruta_docker_compose = os.path.join(ruta_final, 'docker-compose.yml')
    if not os.path.exists(ruta_docker_compose):
        with open(ruta_docker_compose, 'w') as arxiu:
            arxiu.write('version: "3"\nservices:\n')
            print(f'Arxiu {ruta_docker_compose} creat.')
    else:
        print(f"L'arxiu {ruta_docker_compose} ja existeix")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
         nom_dir = sys.argv[1] # Permetrà llegir un argument que vagi després del .py
    else:
        nom_dir = input("Insereix el nom del subdirectori: ")
        
    crear_docker_directori(nom_dir)
