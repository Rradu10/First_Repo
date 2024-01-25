class CustomException(Exception):
    pass


'''
Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative.
Daca da sa se arunce o exceptie specifica
'''


class ContainsNegativeNumbersException(Exception):
    pass


def check_negative_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumbersException(f'Contine {number}')


check_negative_numbers([13, 2, 4, 8, -12])

