class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
        else:
            print(f'Task-ul {nume} nu exista')

    def afiseaza_todo_list(self):
        for task in self.todo.keys():
            print(task)

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(f'Detalii pentru task-ul {nume_task}:')
            print(self.todo[nume_task])
        else:
            raspuns = input(f'Task-ul {nume_task} nu exista in lista. Doriti sa-l adaugati? (da/nu): ')
            if raspuns.lower() == 'da':
                detalii = input('Introduceți detalii pentru task-ul nou: ')
                self.adauga_task(nume_task, detalii)
            else:
                print('la revedere')

# Exemplu de utilizare:
lista_taskuri = TodoList()
lista_taskuri.adauga_task('Curat', 'Curatenie generala in casa')
lista_taskuri.adauga_task('Cumparaturi', 'Cumparaturi pentru cina')
lista_taskuri.afiseaza_todo_list()
lista_taskuri.afiseaza_detalii_suplimentare('Cumparaturi')
lista_taskuri.afiseaza_detalii_suplimentare('Mancare')
lista_taskuri.finalizeaza_task('Cumparaturi')
lista_taskuri.afiseaza_todo_list()
__init__
