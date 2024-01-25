'''
Să se tipărească toate numerele prime aflate între doi întregi citiţi.
Programul va folosi o funcţie care testează dacă un număr este prim sau nu.
'''
import math
def is_prime(nr):
    if nr < 2 :
        return False
    # for i in range(2,nr//2+1): # optimizare 1 --> reducerea spatiului de cautare pana la jumatatea nr
    for i in range(2,int(math.sqrt(nr))+1): # optimizare 2 --> reducerea spatiului de cautare pana la rad din nr
        if nr%i==0:
            return False
    return True

def print_primes_between(start,end):
    for n in range(start,end+1):
        if is_prime(n):
            print(n)

print_primes_between(4,50)
