from random import randint


def sumowanie_wierszy(tab):
    suma = 0
    n = len(tab)
    suma_wierszy = [0 for i in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[i][j]
        #end for 2
        suma_wierszy[i] = suma
    #end for 1

    return suma_wierszy


def sumowanie_kolumn(tab):
    suma = 0
    n = len(tab)
    suma_kolumn = [0 for i in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[j][i]
        #end for 2
        suma_kolumn[i] = suma
    #end for 1

    return suma_kolumn


def ratio_check_in_tab(tab):
    suma_wierszy = sumowanie_wierszy(tab)
    suma_kolumn = sumowanie_kolumn(tab)
    ratio = max = 0
    score = [0,0,0]
    n = len(tab)

    for i in range(n):
        for j in range(n):
            ratio = suma_kolumn[j] / suma_wierszy[i]
            if ratio > max:
                max = ratio
                score[0], score[1], score[2] = ratio, i, j
            #end if
        #end for 2
    #end for 1
    return score




# tab = [[1,2,3,4], [5,5,5,5],[2,2,1,2], [42,24,71,56]]
# print( ratio_check_in_tab(tab) )

### ----------------




