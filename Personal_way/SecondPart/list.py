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