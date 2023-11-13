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
    info_xarxa = []
    for interfaç in interficies:
        direccions = netifaces.ifaddresses
        ipv4 = direccions.get(netifaces.AF_INET, [{}][0].get('addr','No es pot obtenir'))
        netmask = direccions.get(netifaces.AF_INET, [{}][0].get('netmask', 'No es pot obtenir'))
        mac = direccions.get(netifaces.AF_LINK, [{}][0].get('addr', 'No es pot obtenir'))
        info_xarxa.append((interfaç, ipv4, netmask, mac))

    return info_xarxa

# Generar arxiu de test amb tota la informació
