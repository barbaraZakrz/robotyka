from math import *

listaD = []


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
    print(listaD)


# wyswietlenie mapy jako macierz
def wyswietl():
    for i in range(0, 20, 1):
        wiersz = ""
        for j in range(0, 20, 1):
            wiersz += str(listaD[i][j])
            wiersz += " "
        print(wiersz)


def TworzyObiekty(rodzic):
    if rodzic.x+1 >= 0 and rodzic.x+1 < 20:
        if rodzic.y >= 0 and rodzic.y < 20:
            if listaD[rodzic.x + 1][rodzic.y] == 0:
                PierwszaKlasa(rodzic.x+1, rodzic.y, rodzic.g + 1, rodzic)
    if rodzic.x >= 0 and rodzic.x< 20:
        if rodzic.y+1 >= 0 and rodzic.y+1 < 20:
            if listaD[rodzic.x][rodzic.y+1] == 0:
                PierwszaKlasa(rodzic.x, rodzic.y+1, rodzic.g + 1, rodzic)
    if rodzic.x-1 >= 0 and rodzic.x-1 < 20:
        if rodzic.y >= 0 and rodzic.y < 20:
            if listaD[rodzic.x - 1][rodzic.y] == 0:
                PierwszaKlasa(rodzic.x-1, rodzic.y, rodzic.g + 1, rodzic)
    if rodzic.x >= 0 and rodzic.x< 20:
        if rodzic.y-1 >= 0 and rodzic.y-1 < 20:
            if listaD[rodzic.x][rodzic.y-1] == 0:
                PierwszaKlasa(rodzic.x, rodzic.y-1, rodzic.g + 1, rodzic)


wczytanie()
wyswietl()
otwarta = []
zamknieta = []
zamknieta.append(PierwszaKlasa(0, 0, 0, None))
