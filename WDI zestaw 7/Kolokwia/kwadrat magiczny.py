def suma(T):
    n = len( T )
    last_sum = 0
    tmp_sum = 0
    result = 0
    
    for y in range(n):
        for x in range(n):
            tmp_sum += T[y][x] 
        #end for 2
        last_sum = tmp_sum
        result += tmp_sum
        if tmp_sum != last_sum: return False 
    #end for 1
    
    for x in range(n):
        for y in range(n):
            tmp_sum += T[y][x]
        #end for 2
        last_sum = tmp_sum
        result -= tmp_sum 
        if tmp_sum != last_sum: return False 
    #end for 1

    return result == 0 
#end def 

    


