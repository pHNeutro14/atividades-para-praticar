class Tartaruga:
    def __init__(self, nome, posicao_x, posicao_y):
        self.nome = nome
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    def andar_pra_frente(self, passos):
        self.posicao_x += passos

    def andar_pra_tras(self, passos):
        self.posicao_x -= passos

    def andar_pra_cima(self, passos):
        self.posicao_y += passos
    
    def andar_pra_baixo(self, passos):
        self.posicao_y -= passos

    def onde_estou(self):
        print('Eu sou a tartaruga ', self.nome, 'e estou na posição X: ', self.posicao_x, ' Y: ', self.posicao_y)

        