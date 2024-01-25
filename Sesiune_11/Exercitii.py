'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
'''
from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    PI=3.14
    @abstractmethod
    def aria(self):
        pass
    def descrie(self):
        print("Cel mai probabil am colturi")
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.latura = latura
    def aria(self):
        return self.latura ** 2
    @



patrat=Patrat(5)
print(patrat.aria())
patrat.descrie()








# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self.raza=raza
#     def aria(self):
#         return self.raza**2*FormaGeometrica.PI
# cerc=Cerc(5)
# print(cerc.aria())




