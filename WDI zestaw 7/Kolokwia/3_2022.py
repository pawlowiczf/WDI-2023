class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def


# Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
# dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
# sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
# dokładnie z 3 liczbami czynnikowo-podobnymi.


def czynnikowo_podobne(a,b):
    n = 2
    counter = 0

    while a > 1:
        flag = False

        while a % n == 0:
            a = a // n
            flag = True 

        if flag and b % n == 0:
            counter += 1 
        #end if
        n += 1 
    #end while
    return counter == 1
#end def 


def three(T):

    result = 0

    for y in range(1, len(T) - 1):
        for x in range(1, len(T) - 1):
            tmp = 0

            if czynnikowo_podobne( T[y][x], T[y-1][x-1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y-1][x+1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y+1][x-1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y+1][x+1] ): tmp += 1

            if tmp == 3: result += 1
        #end for 2
    #end for 1
    return result 

