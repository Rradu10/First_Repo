'''
1.Funcție care să calculeze și să returneze suma a două numere

2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
'''

'''
5. Scrieţi o funcţie care returnează prima cifră a unui număr natural. 
De exemplu, dacă parametrul efectiv este 127, funcţia va returna 1.
'''

def first_digit(numar):
    while numar >= 10:
        numar //= 10
    return numar

print(first_digit(127))


'''
6. Să se tipărească toate numerele prime aflate între doi 
întregi citiţi. Programul va folosi o funcţie care testează 
dacă un număr este prim sau nu.
'''
def prime_number(nr):
    if nr<=1:
        return False
    if nr <=3:
        return True
    for i in range(4,nr//2+1):
        if nr%i==0:
            return False
    return True

def prime_numbers_between_2_numbers(a,b):
    for nr in range(a,b+1):
        if prime_number(nr):
            print(nr)

prime_numbers_between_2_numbers(10,23)



'''
7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, 
numere care se divid cu suma cifrelor lor. Programul va utiliza o funcţie care returnează 
suma cifrelor unui număr întreg primit ca parametru.
'''
def digits_sum(nr):
    s = 0
    while nr > 0:
        s += nr % 10
        nr //= 10
    return s

def numbers_with_digit_sum_divisible(a, b):
    for nr in range(a, b + 1):
        if nr % digits_sum(nr) == 0:
            print(nr)

numbers_with_digit_sum_divisible(1,25)






'''
Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, 
numere care se divid cu suma cifrelor lor. Programul va utiliza o funcţie care returnează suma cifrelor 
unui număr întreg primit ca parametru.
'''


def sum_digits(nr):
    s = 0
    while nr != 0:
        ultima_cifra = nr % 10
        # print(f'ultima_cifra: {ultima_cifra}')
        s += ultima_cifra
        # print(f' suma:{s}')
        nr = nr // 10
        # print(f'nr:{nr}')
    return s


sum_digits(123)


def print_numbers_divisible_by_digit_sum(start, end):
    for n in range(start, end + 1):
        if n % sum_digits(n) == 0:
            print(n)


print_numbers_divisible_by_digit_sum(1, 70)
