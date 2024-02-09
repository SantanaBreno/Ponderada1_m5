class Pessoa():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cumprimentar(self):
        print(f'Olá {self.name}!, você tem {self.age} anos')

pessoa = Pessoa('Breno', 21)

pessoa.cumprimentar()