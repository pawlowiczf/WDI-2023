class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# end class


def print_all(p):
    while p is not None:
        print(p.val, end=" ")
        p = p.next
# end def


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next

  return g.next
# end def

# ----------------------


def add_gurdian_at_back(p):
    first = p
    while p.next is not None:
        p = p.next
    # end while
    p.next = Node(None)
    p = p.next
    p.next = Node(None)
    return first
# end def


def remove(p, q):

    p = Node(None, p)
    q = Node(None, q)

    first_p = p
    first_q = q.next

    tail_p = p
    tail_q = q

    q = q.next

    # Iterujemy po liscie nieuporzadkowanej z ogonem i szukamy tego samego elementu w liscie uporzadkowanej p, bedziemy tak iterowac dopoki p.val < q.val

    while q is not None:
      p = first_p.next
      tail_p = first_p
      while p is not None and p.val < q.val:
        p = p.next
        tail_p = tail_p.next
      # end while
      if p is not None and p.val == q.val :
        tail_q.next = q.next
        tail_p.next = p.next
        q = q.next
      else:
        tail_q = tail_q.next
        q = q.next
    # end while
    return first_p.next, first_q
#end def
 

#end def

T1 = [1,2,4,5]
T2 = [7,3,15,2,1,8]
p = create_linked_list(T1)
q = create_linked_list(T2)

p, q = remove(p,q)

print_all(p)
print()
print_all(q)