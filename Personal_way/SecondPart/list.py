llista = ['String', 10, 12.5, True] # list()
print(llista)

"""
Cas 1: obtenir dades per mitjà dels elements dins del llistat
També es pot llegir de dreta a esquerra, ara, les posicions canvien:
-4, -3, -2, -1
"""
llista_curs = ['Python', 'Java', 'PHP', 'HTML']
primercurs = llista_curs[0]
ultimcurs = llista_curs[-1]
print(primercurs)
print(ultimcurs)
print(llista_curs)

"""
Cas 2: actualitzar el segon curs
"""
llista_curs[1] = 'CSS'
segoncursCanviat = llista_curs[1]
print(segoncursCanviat)

"""
Cas 3: subllista 1 i subllista 2
Subllista 1
[start:end] 
[start:] -> obtimbre, els últims elements de la llista
[:end] -> obtindrem els primers elements de la llista
subllista 2
[start:end:els salts que volem que faci]
"""

subllista = llista_curs[0:2] #Vull veure del primer fins al tercer curs, Python y CSS
print(subllista)

llista_curs = ['Python', 'Java', 'PHP', 'HTML', 'CSS', 'Ruby', 'C++', 'C#', 'VBA']
subllista = llista_curs[0:8:2] #Vull veure del primer fins al tercer curs, Python y CSS
print(subllista)