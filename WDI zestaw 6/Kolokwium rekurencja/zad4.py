# Dana jest liczba naturalna N. Prosze zaimplementowac funkcje divide(n), ktora sprwadza czy jest mozliwe pociecie liczby N na kawalki, tak aby kazdy
# z kawalkow byl liczba pierwsza oraz liczba kawalkow tez byla pierwsza. Funkcja powinna zwrocic wartosc logiczna.

from math import sqrt


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i <= sqrt( n ) + 1:
        if n % i == 0: return False
        else:
            i += 2
            if n % i == 0: return  False
            i += 4
    #end while
    return True



def zad4(n):
    def rek(n,x,ilosc__cyfr,cnt): # cnt - liczba kawalkow 
        if n == 0: 
            print(x,cnt)
            return is_prime(x) and is_prime(cnt)
        else:
            x+=(n%10)*(10**(ilosc__cyfr))
            if is_prime(x):
                return rek(n//10,0,0, cnt + 1) or rek(n//10,x,ilosc__cyfr+1,cnt)
            else:
                return rek(n//10,x,ilosc__cyfr+1,cnt)
            
    return rek(n,0,0,1)


print(zad4(21722))