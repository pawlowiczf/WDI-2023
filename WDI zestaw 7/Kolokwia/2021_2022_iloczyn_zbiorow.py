class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class

def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def

def create_linked_list(T):
    p = Node(None)
    q = p
    for element in T:
        k = Node(element)
        p.next = k
        p = k
    #end for
    return q.next
#end def 

# ----------

# Zbiór mnogościowy liczb naturalnych reprezentowanych jest przez listę o uporządkowanych rosnąco
# elementach. Proszę napisać funkcję iloczyn(z1, z2, z3), która przekształca 3 listy (zbiory) z1, z2,
# z3 w jedną listę (zbiór) zawierającą elementy będące częścią wspólną zbiorów z1, z2, z3. Funkcja
# powinna zwrócić wskazanie do listy wynikowej.


def iloczyn_two(p,q):

    if p == None or q == None:
        return None
    
    if p.val == q.val:
        x = p 
        p,q = p.next, q.next
        x.next = iloczyn_two(p,q)
        return x 
    else:
        if p.val < q.val:
            return iloczyn_two(p.next, q)
        else:
            return iloczyn_two(p, q.next)
        #end if 
#end def

def iloczyn(z1,z2,z3):
    return iloczyn_two( z1, iloczyn_two(z2,z3) )
#end def



T1 = [1,2,3,4,5,6,7,8,9]
T2 = [1,2,3,4,5,6,7,8]
T3 = [1,2,3,4,5,6,7]
z1 = create_linked_list(T1)
z2 = create_linked_list(T2)
z3 = create_linked_list(T3)


print_all( iloczyn(z1,z2,z3) )
    





    