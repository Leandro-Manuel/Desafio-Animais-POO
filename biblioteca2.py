class animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def emitir_som(self):
        print(f'O {self.nome} está emitindo som!')

    def comer(self,comida):
        print(f'O {self.nome} foi comer {comida}')

class gato(animal):
    def __init__(self,nome,cor):
            super().__init__(nome,cor)

    def emitir_som(self):
            print(f'O {self.nome} está miando!')

    def comer(self,comida):
        print(f'O {self.nome} está comendo {comida}.')

class cachorro(animal):
    def __init__(self,nome,cor):
            super(). __init__(nome,cor)

    def emitir_som(self):
        print(f'O {self.nome} está latindo!')

    def comer(self,comida):
        print(f'O {self.nome} está comendo {comida}')


class coelho(animal):
    def __init__(self,nome,cor):
            super().__init__(nome,cor)

    def emitir_som(self):
        print(f'O {self.nome} está piando!')

    def comer(self,comida):
        print(f'O {self.nome} está comendo {comida}.')

class vaca(animal):
    def __init__(self,nome,cor):
            super().__init__(nome,cor)

    def emitir_som(self):
        print(f'O {self.nome} está rugindo!')

    def comer(self,comida):
        print(f'O {self.nome} está comendo {comida}.')