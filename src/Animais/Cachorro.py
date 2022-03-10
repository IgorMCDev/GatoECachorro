from src.Animais.Animal import Animal

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.CONST_NOME = 'Cachorro'
        self.CONST_BARULHO = 'AuAu'