from math import sqrt
# maska tritowa :))
# 0 - element z tablicy 1, 1 - element z tablicy 2, 2 - elementy z obu tablic
# system trójkowy: n % 3: [ 0, 1, 2 ]


def czy_pierwsza(n):
    if n == 2 or n == 3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i < sqrt(n+1) + 1:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    #end while
    return True


def mask_creation(t1,t2,mask):
    suma = 0
    counter = 0

    for i in range( len(t1) ):
        if mask % 3 == 0: suma += t1[i]
        elif mask % 3 == 1: suma += t2[i]
        elif mask % 3 == 2: suma += t1[i] + t2[i]
        mask //= 3
    return suma


def maska_tritowa(t1, t2):
    licznik = 0
    for mask in range(3 ** len(t1)):
        if czy_pierwsza( mask_creation(t1,t2, mask) ): licznik += 1
    #end for
    return licznik

# --- main

t1 = [1, 4, 52, 3, 5, 2, 35]
t2 = [33, 0, 93, 5, 12, 2, 5]
print(maska_tritowa(t1, t2))

t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]
print(maska_tritowa(t1, t2))


t1 = [1,2]
t2 = [9,4]
print( maska_tritowa(t1, t2) )

t1 = [1,4]
t2 = [3,5]
print( maska_tritowa(t1,t2) )

t1=[1,0]
t2=[0,6]
print( maska_tritowa(t1,t2) )





