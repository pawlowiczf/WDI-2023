# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na kawałki, tak aby każdy
# kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję cutting(s), która zwraca liczbę
# sposobów pocięcia słowa na kawałki.

def samogloska(n):
    values = { 'a','e','i','o','u','y' }
    if n in values: return 1
    return 0

def cutting(s):
    
    def rek(s, i, k, cnt): # s - nasz wyraz, i - indeks na ktorym jestesmy w wyrazie, k - poczatek ostatniego pociecia, cnt - przyjmuje wartosci 1 lub wiecej. 1-en, gdy bedzie 1 samogloska
 
        if cnt == 2:
            return 0

        if i == len(s):
            if cnt == 1:
                return 1 
            return 0 
        #end if 

        if cnt == 1:
            return rek(s, i + 1, k, cnt + samogloska( s[i] ) ) + rek(s, i + 1, i, samogloska( s[i] ) )
        return rek(s, i + 1, k, cnt + samogloska( s[i] ) )
    #end def
    return rek(s,0,0,0)

print( cutting('student' ) )
print( cutting('sesja' ) )
print( cutting('ocena' ) )
print( cutting('informatyka' ) )

        
        
        
       