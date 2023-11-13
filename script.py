import os
import shutil

def borrar_cache_chrome(cache_path):
    # Comprovem si el camí de la caché existeix
    if os.path.exists(cache_path):
        try:
            # Llistem tots els fitxers dins del camí de la caché
            for nomFitxer in os.listdir(cache_path):
                # Construïm la ruta completa al fitxer
                ubicacioFitxer = os.path.join(cache_path, nomFitxer)
                # Comprovem si és un fitxer o un enllaç i l'esborrem
                if os.path.isfile(ubicacioFitxer) or os.path.islink(ubicacioFitxer):
                    # Si és un directori, l'esborrem
                    os.unlink(ubicacioFitxer)
                elif os.path.isdir(ubicacioFitxer):
                    shutil.rmtree(ubicacioFitxer)

            print(f'Caché borrat per al usuari: {usuari}')
            
        except Exception as e:
            print(f'Problema al borrar caché para {usuari}. Razón: {e}')
   
    else:
        print(f'La ruta de la caché no existe para el usuario: {usuari}')

# Ruta al directori on es troben els usuaris del sistema
directori_usuaris = r"C:\Users"

# Que estigui corrent en al moment

# Creem una llista amb tots els directoris d'usuari, excloent fitxers que no són directoris
usuaris = [u for u in os.listdir(directori_usuaris) if os.path.isdir(os.path.join(directori_usuaris, u))]

# Iterem sobre cada usuari i cridem la funció per esborrar la seva caché
for usuari in usuaris:
    # Ruta a la caché de l'usuari actual
    cache_path = os.path.join(directori_usuaris, usuari, r"AppData\Local\Google\Chrome\User Data\Default\Cache")

    borrar_cache_chrome(cache_path)
