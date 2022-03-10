from src.Animais.Gato import Gato
from src.Animais.Cachorro import Cachorro

class FabricaAnimal():
    def __init__(self):
        self.dict_animal= {'1' : Gato, '2' : Cachorro}

    def _fabricaAnimal(self, numeroAnimal):
        animal = None
        try:
            if numeroAnimal in self.dict_animal:
                animal = self.dict_animal[numeroAnimal]()
        except Exception as e:
            print('Erro na fabrica: %s', str(e))
        return animal
        
