from dataclasses import dataclass, field
from typing import Set

def init_colors():
    return {'rosu', 'albastru', 'verde', 'mov', 'lime', 'portocaliu'}

@dataclass
class Masina:
    model: str
    viteza_maxima: int
    culoare: str = 'gri'
    viteza_actuala: int = 0
    culori_disponibile: Set[str] = field(default_factory=init_colors)
    marca: str = 'MercedesBenz'
    inmatriculat: bool = False

    def descrie(self):
        print(f'Marca: {self.marca}')
        print(f'Model: {self.model}')
        print(f'Viteza maxima: {self.viteza_maxima}')
        print(f'Viteza actuala: {self.viteza_actuala}')
        print(f'Culoare: {self.culoare}')
        print(f'Inmatriculata: {self.inmatriculat}')

    def inmatriculare(self):
        self.inmatriculat = True

    def vopseste(self, culoare):
        culoare_lower = culoare.lower()
        if culoare_lower in self.culori_disponibile:
            self.culoare = culoare_lower
        else:
            print('Culoarea dorită nu este disponibilă')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Viteza invalida')
        elif viteza >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0
        print('Masina s-a oprit')

# Exemplu de utilizare:
masina = Masina('EQS', 250)
masina.descrie()
masina.inmatriculare()
masina.vopseste('lime')
masina.accelereaza(300)
masina.descrie()
masina.franeaza()
masina.descrie()
