from random import randint

def nwd(a, b):
    while b:
        a, b = b, a%b
    return a


def zad3(T):

    def tower_left(y, x, steps):
        if y == len( T ) - 1 and x == len( T ) - 1:
            return steps 
        #end if

        min_steps = float('inf')

        for y_move in range( y+1, len(T) ):
            if nwd( T[y_move][x], T[y][x] ) == 1:
                min_steps = min( min_steps, tower_left(y_move, x, steps + 1) )
        
        for x_move in range( x + 1, len(T) ):
            if nwd( T[y][x_move], T[y][x] ) == 1:
                min_steps = min( min_steps, tower_left(y, x_move, steps + 1 ) )

        return min_steps
    #end def

    def tower_right(y, x, steps):
        if y == len( T ) - 1 and x == 0:
            return steps 
        #end if

        min_steps = float('inf')

        for y_move in range( y+1, len(T) ):
            if nwd( T[y_move][x], T[y][x] ) == 1:
                min_steps = min( min_steps, tower_left(y_move, x, steps + 1) )
        
        for x_move in range( x - 1, -1, -1 ):
            if nwd( T[y][x_move], T[y][x] ) == 1:
                min_steps = min( min_steps, tower_left(y, x_move, steps + 1 ) )

        return min_steps
    #end def

    val_left = tower_left(0,0,0)
    val_right = tower_right(0,len(T) - 1, 0)

    if val_left < val_right: return 1
    elif val_right < val_left: return 2
    return 0
#end def

