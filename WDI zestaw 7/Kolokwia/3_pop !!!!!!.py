# Proszę napisać funkcję Two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch
# list. W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa
# razy, a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list.


def put_guardian(p): # tworzy guardiana 
    g = Node( None, p )
    return g 
#end def 


class Node:
    def __init__(self):
        self.val = None
        self.next = None 
#end class


def how_many(p, element):
    cnt = 0

    while p is not None:

        if p.val == element: cnt += 1
        
        p = p.next
    #end while

    return cnt == 2 

#end def

def remove_same_values(p, number): # OPANUJ TO, ŚWIETNE!!!!!!!!!!

    if p is None: 
        return None
    
    else:

        if p.val == number:
            return remove_same_values(p.next, number)
        
        else:
            p.next = remove_same_values(p.next, number)
            return p

#end def 



def two(p):
    #guardiany
    a = Node(None)
    b = Node(None)
    
    while p is not None:

        x = how_many(p, p.val)
        tmp = p
        p = p.next

        if x == 2:
            tmp.next = a.next
            a.next = tmp 
        
        else:
            tmp.next = b.next
            b.next = tmp
        #end if 

        p = remove_same_values(p, tmp.val)

    #end while
    return a,b

        






