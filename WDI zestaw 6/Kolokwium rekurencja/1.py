# Rekurencja, operacja na liczbach ABC a - zamiana miejscami dwoch ostatnich cyfr, b - mnozenie liczby przez 3, c - usuwanie pierwszej cyfry

from math import log10

def dlugosc(x):
    dlugosc = int(log10(x)) + 1

    return dlugosc


def A(x):
    a = x%10
    b = (x//10)%10
    x = (x//100)*100 + 10*a + b
    return x

def B(x):
    
    return x*3

def C(x):
    mod = x%(10**(dlugosc(x)-1))
    
    return mod



def zad1(x,y):
    def rek(x,y,cnt, string):
        if x == y:
            print(string)
        elif cnt == 7:
            return
        else:
            if dlugosc(x) >=2:
                rek(A(x),y,cnt + 1, string + "A")
                rek(B(x), y, cnt + 1, string + "B")
                rek(C(x), y ,cnt +1, string + "C")
            else:
                rek(B(x), y, cnt + 1, string + "B")

    rek(x,y,0, "")

zad1(6,3)