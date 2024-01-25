class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajat: {self.nume} {self.prenume}, Salariu: {self.salariu}')

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu *= (1 + procent / 100)


angajat1 = Angajat('Popescu', 'Ion', 5000)
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())

angajat1.marire_salariu(10)
print(angajat1.salariu_lunar())
