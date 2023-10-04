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


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def

# --------

def NWD(a,b):
    while b > 0:
        a,b=b,a%b
    return a
#end def

def arithmetic_difference(p):
    value_nwd = 1
    r = p.next.val - p.val

    while p.next is not None:
        value_nwd = NWD(r, (p.next.val - p.val) )
        p = p.next
    #end while
    return value_nwd
#end def 

def repair(p):
    k = p
    counter = 0
    r = arithmetic_difference(p)

    while p.next is not None:
        
        diff = p.next.val - p.val
        if diff != r:
            new_value = Node(p.val + r, p.next)
            p.next = new_value
            counter += 1
        #end if
        p = p.next 
    #end while
    return k
#end def

T = [4,8,14]
p = create_linked_list(T)
print_all( repair(p) )