import random
class pedrapepeletesoura:
    def __init__(self) -> None:
        self.config=['pedra','pepel','tesoura']
        self.msg='escolha entre pedra pepel e tesoura '
    def configuracao(self):
        self.jogo=random.choice(self.config)
    def inicializao(self):
        self.configuracao()
        self.escolha=input(self.msg)
        try:
            self.escolha
            self.jogo
            if self.escolha=='pedra' or self.escolha=='tesoura':
                if self.jogo=='pepel'or self.jogo=='pedra':
                    print('perdeu')
                        
            if self.escolha=='pedra' or self.escolha=='pepel':
                if self.jogo=='tesoura' or self.jogo=='pedra':
                    print('vc ganhou')
                      
                        
            if self.escolha=='pepel':
                if self.jogo=='tesoura':
                    print('vc perdeu ')
                elif self.escolha==self.jogo:
                    print('empate')
                    
        except Exception as err:
            print('ocorreu algum erro',err)
jogo=pedrapepeletesoura()
jogo.inicializao()