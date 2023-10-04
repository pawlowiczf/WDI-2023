from random import randint


def is_on_board(y,x,n):
    return x < n and y < n


def can_move_to(from_x, from_y, x, y):
    return from_x <= x and from_y <= y


def get_first(n):
    while n // 10 > 0:
        n = n // 10
    #end while
    return n % 10


def get_last(n):
    return n % 10


def can_get_to(y,x):
    global tab
    if y == 7 and x == 7: return True

    for i, j in [ (1,1), (1,0), (0,1) ]:
        if can_move_to(y, x, y + i, x + j) and is_on_board(y + i, x + j, len(tab) ):
            first = get_first( tab[y+i][x+j] )
            last = get_last( tab[y][x] )
            if last < first:
                return can_get_to( x + i, y + j )
    #end for

    return False
#end def


for i in range(10000):
    tab = [ [randint(1,15) for _ in range(8)] for _ in range(8) ]
    if can_get_to(0,0): print("1")
