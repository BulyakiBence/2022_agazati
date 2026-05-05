f = open ('2022/3. feladat/tura.txt', 'r', encoding= 'utf-8')
sorok = f.readlines()
f.close

class Tura:
    def __init__(self, nev, tav, szint):
        self.nev = nev
        self.tav = float(tav)
        self.szint = int(szint)

darabok = []
for i in range(1, len(sorok)):
    darab = sorok[i].strip().split(";")
    h = Tura(darab[0], float(darab[1].replace(',', '.')),darab[2])
    darabok.append(h)



