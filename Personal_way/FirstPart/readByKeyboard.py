"""
Entrada de dades
"""
nom_complet= input('Si us plau, inserta el teu nom complet: ')
print(nom_complet)
print(type(nom_complet)) # Sabrem de quin tipus és el valor que ha introduit l'usuari per teclat

"""
Trasnformar tipus de dades, en aquest cas transformar la altura
que tindrà valor de str a float
"""
edat= input('Si us plau, inserta la teva edat: ')
altura= input('Si us plau, inserta la teva altura: ')
altura = float(altura)
print(type(altura))

"""
Prova de boleans, mostrar una autorització i
mostrar el resultat per pantalla
""" 
autoritzacio = input('Autoritzar el programa? (si/no)')
autoritzacio = autoritzacio == 'si'

print(autoritzacio)