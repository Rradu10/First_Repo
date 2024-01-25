def read(filename):
    with open(filename, 'r') as f:  # deschidere fisier in modul 'r' (citire / read) si stocare obiect in variabila f
        return f.readlines()


print(read('numere.txt'))


def write(filename, data):
    with open(filename, 'w') as f:  # deschidere fisier in modul 'w' - write
        f.writelines(data)


write('numere2.txt', ['1\n', '2\n', '3\n'])


def append(filename, data):
    with open(filename, 'a') as f:  # deschidere fisier in modul 'a' - append/adaugare
        f.writelines(data)


append('numere.txt', ['1\n', '2\n', '3\n'])
