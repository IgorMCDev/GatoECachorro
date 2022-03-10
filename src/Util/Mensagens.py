class Mensagens():
    def __init__(self):
        self.CONST_INICIO_USUARIO =  'Olá, conheço o som de alguns animais.\n' + \
            'Gostaria de descobrir algum? '
        self.CONST_PERGUNTA_USUARIO =  'Selecione um animal de acordo com o digito:\n' + \
            '1    =>    Gato \n' + \
            '2    =>    Cachorro \n\n' + \
            'Ou, ainda digite:\n' + \
            '3    =>  Para obter o histórico de animais.\n' + \
            'exit =>  Para finalizar a execução.\n'
        self.CONST_ADIOS = 'Até a próxima.'
        self.CONST_ESCOLHA_ERRADA = 'Essa ecolha não existe'
        self.respostaUsuario = '{} {}'

    def _enviaMensagem(self, mensagem):
        print(mensagem)
        print("\n")

    def _aguardaEscolha(self):
        return input()

