''' Singleton=Sablon creational care se asigura ca o clasa are doar o singura instanta si
 ofera acces universal catre aceasta instanta
Avantaje:
1.Poti sa fii sigur ca o clasa are o singura instanta;
2.Acea distanta este accesibila de oriunde din cod;
3.Acea instanta este initializata doar cand este folosita pentru prima oara;
4.Acest sablon poate masca un design slab, de exemplu;
 atunci cand componentele programului scriu prea multe una despre cealalta;
 '''





class SingletonLogger:
    _instance = None

    def __init__(self, filename):
        if hasattr(self._instance, 'filename'):
            return
        self.filename = filename

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating object')
            cls._instance = super().__new__(cls)
        return cls._instance


logger = SingletonLogger('Hello.txt')
logger2 = SingletonLogger('Hello2.txt')
print(logger, logger2)
print(logger.filename, logger2.filename)
