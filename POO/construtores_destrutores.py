class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando classe... ')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("removendo instancia da classe")

    def falar(self):
        print('auau')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

c = Cachorro('Meg', 'Preta')
c.falar()

print(c)