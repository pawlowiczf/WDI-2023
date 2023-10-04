from math import sqrt



def czy_pierwsza(n):
    if n == 2 or n == 3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    #end
    return True


def only_odd(n):
    temp = n
    while temp != 0:
        if ( temp % 10 ) % 2 == 0: return False
        temp = temp // 10
    #end
    return True



def check_verse_in_tab(tab):
    for ele in tab:
        if not czy_pierwsza( ele ) and only_odd( ele ):
            return True
    #end for
    return False



def only_odd_in_verses(tab):

    for i in tab:
        if check_verse_in_tab( i ):
            pass
        else:
            return False
    #end for
    return True



tab = [ [6,2,9], [15,4,15], [15,6,9] ]
print( only_odd_in_verses(tab) )

