# and, or i not
# AND torna true si dos condicions son verdaderes
# OR torna true i al menos una de les condicions és verdadera
# NOT inverteix el valor boleà de la condició

resultat_final = True and False

"""
Exemple de cas:
Tenim una tenda online i volem aplicar un descompte als clients que compren més de 10 artícles
i que gasten més de 100 euros
"""
numero_de_articles = 12
total_de_compra = 120

if numero_de_articles > 10  and total_de_compra > 100:
    print("Descompte aplicat!")

else:
    print("Descompte no aplicat")

    # Comprovació de commit 2