# dwa równoliczne, niepuste podzbiory o jednakowej sumie elementow, tablica

def zad(t):
    def rek(suma,a,b,i):      #a to liczność zbioru a, b to liczność zbioru b
        if suma == 0 and a == b and a!=0:
            return True
        elif i==len(t):
            return False
        else:
            return rek(suma + t[i], a+1,b,i+1) or rek(suma-t[i],a,b+1,i+1) or rek(suma, a, b, i+1)
    return rek(0,0,0,0)


print(zad([2,4,5,21]))