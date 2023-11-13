import csv

# Ruta de l'arxiu /etc/passwd
passwd_path = '/etc/passwd'

# Ruta d'exportació de l'arxiu CSV
csv_path = 'usuaris.csv'

# Llegir les dades i guardar-les en un array
csv_data = []

# Llegir l'arxiu /etc/passwd
with open(passwd_path, 'r') as passwd_file:
    linies = passwd_file.readlines()

# Processar cada línia de passwd_path
for linia in linies:
    if not linia.startswith('#'):
        parts = linia.strip().split(':')
        usuari = parts[0]
        usuari_id = parts[2]
        directori_home = parts[5]
        shell = parts[6]

    # Afegir CSV
    csv_data.append([usuari,usuari_id,directori_home, shell])

# Esciure a l'arxiu CSV
with open(csv_path, 'w', newline='') as csv_file:
    escriure = csv.writer(csv_file)
    escriure.writerow(['Usuari', 'ID', 'Directori Home', 'Shell'])

    # Escriure les dades
    escriure.writerows(csv_data)

print(f'Arxiu .CSV generat en {csv_file}')
