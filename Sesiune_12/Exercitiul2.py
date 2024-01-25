from datetime import date
from pprint import pprint
class Factura:
    serie = 'X'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        data = date.today().strftime('%d-%m-%Y')

        total = self.cantitate * self.pret_buc

        print(f'Factura seria {self.serie} numar {self.numar}')
        print(f"Data: {data}")
        print("Produs    | Cantitate | Pret bucata | Total")
        print(f"{self.nume_produs}   |      {self.cantitate}    |     {self.pret_buc}     |  {total}")

# Exemplu de utilizare:
factura1 = Factura(1, "Telefon", 7, 700)
factura1.genereaza_factura()
