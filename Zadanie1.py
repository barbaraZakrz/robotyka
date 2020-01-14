plik = open("grid.txt", "r")
listaD = []
for i in range(0, 20, 1):
    wiersz = []
    wiersz = plik.readline()
    lista = []
    for j in range(0, 39, 2):
        lista.append(int(wiersz[j]))
    #print(lista)
    print("----------------------------------------")
    listaD.append(lista)

print(listaD)
