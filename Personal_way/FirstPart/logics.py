# and, or i not
# AND torna true si dos condicions son verdaderes
# OR torna true i al menos una de les condicions és verdadera
# NOT inverteix el valor boleà de la condició

resultat_final = True and False

"""
Exemple de cas 1:
Tenim una tenda online i volem aplicar un descompte als clients que compren més de 10 artícles
i que gasten més de 100 euros.

En cas volem que la sortida sigui "Descompte aplicat" perquè ambes condicions son True
cumplint amb la condició de l'operador (and)
"""
numero_de_articles = 12
total_de_compra = 120

if numero_de_articles > 10  and total_de_compra > 100:
    print("Descompte aplicat!")

else:
    print("Descompte no aplicat")


"""
Exemples de cas 2:
Des de la base anterior, ampliar el missatge amb una felicitació si
el client es nou o ha fet una compra gran
"""

client_nou = True

if client_nou or total_de_compra >100:
    print("Felicitats! Tindràs un regal!")
else:
    print("Gràcies per la teva compra")