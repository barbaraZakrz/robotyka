from math import *

listaD = []
otwarta = []
zamknieta = []


class PierwszaKlasa:
    def __init__(self, x, y, g, rodzic):
        self.x = x
        self.y = y
        self.h = sqrt((x - 19) ** 2 + (y - 19) ** 2)
        self.g = g
        self.f = g + self.h
        self.rodzic = rodzic


# wczytanie mapy
def wczytanie():
    plik = open("grid.txt", "r")
    for i in range(0, 20, 1):
        wiersz = []
        wiersz = plik.readline()
        lista = []
        for j in range(0, 39, 2):
            lista.append(int(wiersz[j]))
        # print(lista)
        # print("----------------------------------------")
        listaD.append(lista)
    # print(listaD)
    listaD.reverse()
    #print(listaD)


# wyswietlenie mapy jako macierz
def wyswietl():
    for i in range(0, 20, 1):
        wiersz = ""
        for j in range(0, 20, 1):
            wiersz += str(listaD[i][j])
            wiersz += " "
        print(wiersz)

def dodajDoOtwarteej(doPorownania):
    flaga = 0
    for i in otwarta:
        if doPorownania.x == i.x and doPorownania.y == i.y:
            if doPorownania.f < i.f:
                i = doPorownania
            flaga = 1
    if flaga == 0:
        otwarta.append(doPorownania)


#tworzenie obiektów sąsiadujących z rodzicem
def TworzyObiekty(rodzic):
    if rodzic.x+1 >= 0 and rodzic.x+1 < 20:
        if rodzic.y >= 0 and rodzic.y < 20:
            if listaD[rodzic.x + 1][rodzic.y] == 0:
                dodajDoOtwarteej(PierwszaKlasa(rodzic.x+1, rodzic.y, rodzic.g + 1, rodzic))
    if rodzic.x >= 0 and rodzic.x< 20:
        if rodzic.y+1 >= 0 and rodzic.y+1 < 20:
            if listaD[rodzic.x][rodzic.y+1] == 0:
                dodajDoOtwarteej(PierwszaKlasa(rodzic.x, rodzic.y+1, rodzic.g + 1, rodzic))
    if rodzic.x-1 >= 0 and rodzic.x-1 < 20:
        if rodzic.y >= 0 and rodzic.y < 20:
            if listaD[rodzic.x - 1][rodzic.y] == 0:
                dodajDoOtwarteej(PierwszaKlasa(rodzic.x-1, rodzic.y, rodzic.g + 1, rodzic))
    if rodzic.x >= 0 and rodzic.x< 20:
        if rodzic.y-1 >= 0 and rodzic.y-1 < 20:
            if listaD[rodzic.x][rodzic.y-1] == 0:
                dodajDoOtwarteej(PierwszaKlasa(rodzic.x, rodzic.y-1, rodzic.g + 1, rodzic))

def minimum(lista):
    min = lista[0]
    for i in lista:
        if i.f < min.f:
            min = i
    return min

def WyswietlTrase(obiekt):
    trasa = []
    for i in range(obiekt.g):
        para = []
        para.append(obiekt.x)
        para.append(obiekt.y)
        trasa.append(para)
        obiekt = obiekt.rodzic
    trasa.reverse()
    return trasa



wczytanie()
wyswietl()
zamknieta.append(PierwszaKlasa(0, 0, 0, None))

while 1:
    TworzyObiekty(zamknieta[len(zamknieta) -1])
    doPorownania = minimum(otwarta)
    flaga = 0
    for i in zamknieta:
        if doPorownania.x == i.x and doPorownania.y == i.y:
            if doPorownania.f < i.f:
                i = doPorownania
            flaga = 1
            otwarta.remove(doPorownania)
    if flaga == 0:
        zamknieta.append(doPorownania)
        otwarta.remove(doPorownania)
    if otwarta == []:
        print("nie ma")
        break
    if zamknieta[len(zamknieta)-1].x == 19 and zamknieta[len(zamknieta)-1].y == 19:
        print(WyswietlTrase())
        break


