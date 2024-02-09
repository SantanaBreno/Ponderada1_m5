class Pessoa():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def cumprimentar(self):
        print(f'Olá {self.name}!, sua altura é {self.height}')

pessoa = Pessoa('Breno', 1.82)

pessoa.cumprimentar()