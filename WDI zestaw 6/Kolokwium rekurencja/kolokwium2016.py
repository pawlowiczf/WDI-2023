# Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
# możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
# poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
# Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
# pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
# znalezionych i wypisanych sum

from math import sqrt

def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def zad(t1,t2):
    w = [0] * len(t1)
    
    def rek(i, suma):
        
        if i == len(t1):
            if prime(suma):
                for k in range( len(t1) ):
                    if k >= 1: print("+", end="")
                    if w[k] == 0: print( t1[k], end="")
                    elif w[k] == 1: print( t2[k], end="" )
                    else: print( t1[k]"+",t2[k], end="" )
                    if k == len(t1) - 1: print()
        #end if
        # 0 - biore z 1 tablicy, 1 - biore z 2 tablicy, 2 - biore z obu tablic
        else:
            w[i] = 0
            rek(i+1, suma+t1[i] )

            w[i] = 1
            rek(i+1, suma+t2[i] )

            w[i] = 2
            rek(i+1, suma+t1[i]+t2[i])
        #end def
    rek(0,0)

#end def


t1 = [1,3,2,4]
t2 = [9,7,4,8]
zad(t1,t2)