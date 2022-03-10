from numpy import empty
from src.FabricaAnimal import FabricaAnimal
from src.Util.Mensagens import Mensagens

class GerenciadorAnimal():
    def __init__(self):
        self.listaHistoricoAnimal = []
        self.opcoesEscolha = ['1', '2', '3', 'exit']

    def __registraHistorico(self, codigo, animal):
        self.listaHistoricoAnimal.append([codigo, animal])
    
    def __montaHistorico(self):
        resposta = 'Histórico:\n'
        for item in self.listaHistoricoAnimal:
            resposta = resposta + '{} {}\n'.format(item[0], item[1]._barulhoDoAnimal())
        return resposta

    def _executaAppAnimal(self):
        try:
            mensagem = Mensagens()
            fabrica = FabricaAnimal()
            terminate = False
            mensagem._enviaMensagem(mensagem.CONST_INICIO_USUARIO)
            while terminate == False:
                mensagem._enviaMensagem(mensagem.CONST_PERGUNTA_USUARIO)
                escolha = mensagem._aguardaEscolha()
                if escolha in self.opcoesEscolha:
                    if escolha == self.opcoesEscolha[3]:
                        mensagem._enviaMensagem(mensagem.CONST_ADIOS)
                        terminate = True
                    elif escolha == self.opcoesEscolha[2]:
                        historico = self.__montaHistorico()
                        mensagem._enviaMensagem(historico)
                    else:
                        animal = fabrica._fabricaAnimal(escolha)
                        mensagem._enviaMensagem(mensagem.respostaUsuario.format(str(escolha),  str(animal._barulhoDoAnimal())))
                        self.__registraHistorico(escolha, animal)
                else:
                    mensagem._enviaMensagem(mensagem.CONST_ESCOLHA_ERRADA)
        except Exception as e:
            print('Erro: %s', str(e))