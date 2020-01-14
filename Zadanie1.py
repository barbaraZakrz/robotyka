from math import *
listaD = []

class PierwszaKlasa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = sqrt((x-20)**2 + (y-20)**2)

#wczytanie mapy
def wczytanie():
    plik = open("grid.txt", "r")
    for i in range(0, 20, 1):
        wiersz = []
        wiersz = plik.readline()
        lista = []
        for j in range(0, 39, 2):
            lista.append(int(wiersz[j]))
        #print(lista)
        #print("----------------------------------------")
        listaD.append(lista)
    #print(listaD)
    listaD.reverse()
    print(listaD)

def wyswietl():
    for i in range(0, 20, 1):
        wiersz = ""
        for j in range(0,20,1):
            wiersz+=str(listaD[i][j])
            wiersz+=" "
        print(wiersz)

wczytanie()
wyswietl()


