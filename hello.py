class Pessoa():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def cumprimentar(self):
        print(f'Olá {self.name}!, você tem {self.age} anos e sua altura é {self.height}')

pessoa = Pessoa('Breno', 21, 1.82)

pessoa.cumprimentar()