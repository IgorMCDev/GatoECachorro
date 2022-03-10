from src.Animais.Animal import Animal

class Gato(Animal):
    def __init__(self):
        super().__init__()
        self.CONST_NOME = 'Gato'
        self.CONST_BARULHO = 'Miau'
