import os
import platform
import netifaces

# Obtenir el nom de la màquina i la informació del SO
def info_sistema():
    nom_maquina = platform.node()
    sistema_operatiu = platform.system()+ " " + platform.release()
    return nom_maquina, sistema_operatiu

# Informació sobre les interfícies de xarxa (IPv4, la màscara de xarxa i l'adreça MAC)
def info_xarxa():
    interficies = netifaces.interfaces()
    informacio_xarxa = []
    for interficie in interficies:
        
        direccions = netifaces.ifaddresses(interficie)
        
        ipv4_info = direccions.get(netifaces.AF_INET, [{}])
        ipv4 = ipv4_info[0].get('addr', 'No es pot obtenir')
        
        netmask = ipv4_info[0].get('netmask', 'No es pot obtenir')
        
        mac_info = direccions.get(netifaces.AF_LINK, [{}])
        mac = mac_info[0].get('addr', 'No es pot obtenir')
        
        informacio_xarxa.append((interficie, ipv4, netmask, mac))

    return informacio_xarxa

# Generar arxiu de test amb tota la informació
def arxiu_text(nom_maquina, sistema_operatiu, info_xarxa):
    with open(f"Resultats_{nom_maquina}.txt", "w") as arxiu:
        arxiu.write(f"Nom màquina: {nom_maquina}\n")
        arxiu.write(f"Sistema Operatiu: {sistema_operatiu}\n")
        arxiu.write(f"Interfícies de xarxa:\n")
        for interficie, ipv4, netmask, mac in info_xarxa:
            arxiu.write(f"{interficie} - IP: {ipv4}, Màscara: {netmask}, MAC: {mac}\n")
        
if __name__ == "__main__":
    nom_maquina, sistema_operatiu = info_sistema()
    informacio_xarxa = info_xarxa()
    arxiu_text(nom_maquina, sistema_operatiu, informacio_xarxa)
    print(f"Text creat amb l'informació de la màquina: {nom_maquina}")
