import csv
import json


class Translator:
    translations = {}

    def localize(self, text):
        return self.translations.get(text)


class EnglishTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "hello",
            "lume": "world",
            "pisica": "cat",
            "caine": "dog",
            "soare": "sun",
            "carte": "book",
            "puteri": "powers",
            "apa": "water",
            "munte": "mountain",
            "oras": "city",
            "floare": "flower",
            "masa": "table",
            "telefon": "phone",
            "tara": "country",
            "ploaie": "rain",
            "fericit": "happy",
            "fermecat": "enchanted",
            "cafea": "coffee",
            "calatorie": "journey",
            "muzica": "music"
        }


class SpanishTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "hola",
            "lume": "mundo",
            "pisica": "gato",
            "caine": "perro",
            "soare": "sol",
            "carte": "libro",
            "puteri": "poderes",
            "apa": "agua",
            "munte": "montana",
            "oras": "ciudad",
            "floare": "flor",
            "masa": "mesa",
            "telefon": "telefono",
            "tara": "pais",
            "ploaie": "lluvia",
            "fericit": "feliz",
            "fermecat": "encantado",
            "cafea": "cafe",
            "calatorie": "viaje",
            "muzica": "musica"
        }


class FrenchTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "salut",
            "lume": "monde",
            "pisica": "chat",
            "caine": "chien",
            "soare": "soleil",
            "carte": "livre",
            "puteri": "pouvoirs",
            "apa": "eau",
            "munte": "montagne",
            "oras": "ville",
            "floare": "fleur",
            "masa": "table",
            "telefon": "telephone",
            "tara": "pays",
            "ploaie": "pluie",
            "fericit": "heureux",
            "fermecat": "ensorcele",
            "cafea": "cafe",
            "calatorie": "voyage",
            "muzica": "musique"
        }


class TranslatorFactory:
    __TRANSLATORS_MAPPING = {
        'EN': EnglishTranslator,  # clasa
        'ES': SpanishTranslator,
        'FR': FrenchTranslator
    }

    def get_translator(self, lanquage):
        translator_class = self.__TRANSLATORS_MAPPING.get(
            lanquage)  # translator_class este un obiect de tip clasa si va tb
        # sa il apelam cu paranteze pentru a instantia un obiect din aceasta clasa
        return translator_class()


factory = TranslatorFactory()
english_trans = factory.get_translator('EN')
french_trans = factory.get_translator('FR')
print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')


class FileTranslator:
    def __init__(self, filename):
        self.filename = filename

    def read_words(self):
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def translate(self):
        words = self.read_words()
        translated_words = []
        factory = TranslatorFactory()
        for word in words:
            translator = factory.get_translator(word['limba_destinatie'].upper())
            translated_words.append({
                'cuvant_initial': word['cuvant'],
                'limba_de_traducere': word['limba_destinatie'],
                'traducere': translator.localize(word['cuvant'])
            })
        self.write_translations(translated_words)

    def write_translations(self, translated_words):
        with open('translations.json', 'w') as f:
            json.dump(translated_words, f, indent=4)


file_translator = FileTranslator('de_tradus.csv')
file_translator.translate()
