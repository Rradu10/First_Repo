from abc import ABC, abstractmethod
from pprint import pprint


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print('Copiii invata sa deseneze')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora 5')


class GradinitaPrivata(Gradinita, ABC):
    __elevi={}
    def _adauga_elevi(self,**kwargs):
        self.__elevi.update(kwargs)
    @property
    def elevi(self):
        return self.__elevi
    @elevi.setter
    def elevi(self,value):
        self._adauga_elevi(**value)

    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina')

class GradinitaPrivata11(GradinitaPrivata):
    def ora_de_somn(self):
        print('Copiii dorm intre 11:30 si 14:30')



class GradinitaPublica25(GradinitaPublica):
    nr_elevi = 600
    _adresa = 'Strada Napoca 12'
    __fonduri = 300_000

    @property
    def fonduri(self):
        return self.__fonduri

    @fonduri.setter
    def fonduri(self, value):
        self.__fonduri = value

    @fonduri.deleter
    def fonduri(self):
        self.__fonduri = None

    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar')

    def calculeaza_medie_buline_rosii(self, buline):
        medie = sum(buline) / len(buline)
        if medie > 5:
            print('Elevii acestei gradinite sunt foarte neastamparati')

    def info_elevi(self):
        elevi = {}
        while True:
            nume_elev = input('Introdu numele elevului: ')
            nume_parinti = input('Introdu nume parinti: ')
            varsta = input('Introdu varsta: ')
            activitate = input('Introdu activitatea preferata: ')
            elevi[nume_elev] = {
                'nume_parinti': nume_parinti,
                'varsta': varsta,
                'activitate': activitate
            }
            introduce = input('Doresti sa introduci date in continuare? (y/n): ')
            if introduce.lower() != 'y':
                break

        pprint(elevi)


p = GradinitaPublica()
p.activitate_practica()

# pr = GradinitaPrivata() # da eroare pt ca nu se pot crea obiecte pt clase abstracte

p25 = GradinitaPublica25()
p25.activitate_practica()
p25.ora_de_somn()
p25.calculeaza_medie_buline_rosii([1, 2, 3, 4])
p25.calculeaza_medie_buline_rosii([8, 9, 10, 7])
# p25.info_elevi()

print(p25.nr_elevi)


print(p25.fonduri)
p25.fonduri = 250_000
print(p25.fonduri)

del p25.fonduri
print(p25.fonduri)


pr11=GradinitaPrivata11()
pr11.elevi={'Andrei': {'varsta': 3,'an_inscriere':2022}}
pr11.elevi={'Valentina': {'varsta': 2,'an_inscriere':2023}}
pprint(pr11.elevi)
