def fib(n):
    if n==1: # fibacci 1st is 1. and fibnacci 2nd is 1. Both 0, and 1 can't be calculated usinb fib(n-2) + finb(n-1). 
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1) +fib(n-2)
    

#print(fib(7))

def fibMem2(n, fibdict={0: 0, 1: 1}):# usinmg a default Dictionery with initial fib values.
    if n in fibdict:
        return fibdict[n]
    else:
        fibdict[n] = fibMem2(n - 1,fibdict) + fibMem2(n - 2,fibdict)
        return fibdict[n]

print(fibMem2(100))