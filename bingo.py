# Filename: bingo.py

"""Bingo per al Centre d'Esplai Flor de Neu by Pau Antonio Soler"""

numeros = [False] * 90
ultims = []

def nouNumero() :
    numero = int(input("Introdueix el número: "))
    while(numero < 1 or numero > 90 or numeros[numero-1]) :
        numero = int(input("Número incorrecte! Introdueix-ne un de vàlid: "))
    numeros[numero-1] = True
    ultims.insert(0, numero)
    if(len(ultims) > 5) : ultims.pop(5)
    imprimirNumeros()

def linia() :
    print("LÍNIAAAA\n")

def bingo() :
    print("BINGOOOO\n")

def imprimirNumeros() :
    print("\n"+"-"*76+"")
    linia = ""
    for i in range(90) :
        linia += "| "
        if (not numeros[i]) : linia += "   "
        else :
            if (i < 9) : linia += "0"+str(i+1)+" "
            else : linia += str(i+1)+" "
        if ((i+1)%15 == 0 and i != 0) : 
            linia += "|"
            print(linia)
            linia = ""
            print("-"*76)
    linia = "\n"
    for n in ultims : 
        if (n < 10) : linia += '0'
        linia += str(n)+" "
    print(linia+"\n")

print("Benvinguts al Bingo del Sopar de la Fam\nOrganitzat pel Centre d'Esplai Flor de Neu\n")
partidaEnCurs = True

while(partidaEnCurs) :
    print("Què vols fer?\n")
    print("1. Introduir un número")
    print("2. Línia")
    print("3. Bingo")
    print("4. Acabar la partida")

    try:
        opcio = int(input("\nTria la opció: "))

        if (opcio == 1) : nouNumero()
        elif (opcio == 2) : linia()
        elif (opcio == 3) :  bingo()
        elif (opcio == 4) : partidaEnCurs = False
        else: print("\nOpció incorrecta! Introdueix un número vàlid\n")
    
    except:
        print("\nOpció incorrecta! Introdueix un número vàlid\n")