# Odcinek leżący na osi liczbowej jest opisywany parą liczb całkowitych (a, b). Dana jest tablica
# opisująca zbiór takich odcinków. Proszę napisać funkcję zwracającą wartość True, jeżeli z tablicy
# można wybrać zbiór odcinków, z których dwa nie zachodzą na siebie, a łączna ich długość wynosi
# 2022 lub False w przeciwnym wypadku


def do_cross( tuple_1, tuple_2 ):
    a, b = tuple_1
    c, d = tuple_2
    if b == c or a <= c <= b or a <= d <= b or a == d: return False
    return True 


def zad2(T):
    def rek(T, i, suma, P, cnt):

        if suma == 2022:
            return True 

        if suma > 2022: 
            return False

        if i == len(T):
            return False 

        for j in range( cnt ):
            if do_cross( T[j], T[ P[j] ] ): break
        else:
            if rek(T, i + 1, suma, P, cnt): return True 
            P[ cnt ] = i
            return rek(T, i + 1, suma + T[i][1] - T[i][0] + 1, cnt + 1 )

        return rek(T, i + 1, suma, P, cnt)
        


        

