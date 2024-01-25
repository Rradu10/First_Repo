# O variabila este un container unde se stocheaza o valoare ce poate fi schimbata ulterior

marca = 'Mercedes'  # string
an_de_fabricatie = 2022  # int
consum = 8.5  # float
sistem_de_franare_ABS = True  # bool

print(type(marca),type(an_de_fabricatie),type(consum),type(sistem_de_franare_ABS))

consum=round(consum)
print(consum,type(consum))

print(f'Vehiculul este marca {marca}, este din anul {an_de_fabricatie}, are consum {consum}l/100km si vine echipata cu ABS-{sistem_de_franare_ABS}')

nume='Abarzaei'
prenume='Rares'
x=len(nume)+len(prenume)
print(f'Numele complet are {x}')


