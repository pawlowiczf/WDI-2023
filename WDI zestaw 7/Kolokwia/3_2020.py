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


#  Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
# funkcję, która usuwa z listy wejściowej najkrótszą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
# dokładnie jednej najkrótszej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
# Funkcja powinna zwrócić liczbę usuniętych elementów.
# Na przykład z listy [ 1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [13 13 13],
# a z listy [1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 3 ] nie należy nic usuwać.


def sublist_constant_length(p):
    counter = 1

    while p is not None and p.next is not None and p.next.val == p.val:
        counter += 1
        p = p.next

    #end while
    return counter, p
#end def

def remove_constant_sublist(p):
    
    p = Node(None, p)
    q = p
    unique = False 
    min_length = float('inf')
    
    crd = (None, None)

    while p.next is not None:

        current_length, _end = sublist_constant_length( p.next )
        if current_length < min_length: 
            min_length = current_length
            unique = True 
            crd = (p, _end)
        elif current_length == min_length:
            unique = False 
        p = _end
    #end while
    
    if unique:
        min_before_start = crd[0]
        min_end = crd[1]
        min_before_start.next = min_end.next
        return q
    else:
        return q
    #end if

p = create_linked_list( [1,3,3,3,4,5,3,3,3,3,3,3,5,6,7] )

p = remove_constant_sublist( p )
print_all( p.next )


            
