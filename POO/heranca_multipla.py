class Animal:
    def __init__(self, numero_patas,):
        self.numero_patas = numero_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join({f'{chave} = {valor}' for chave, valor in self.__dict__.items()})}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass 

class Gato(Mamifero):
    pass

class Leão(Mamifero):
    pass

class Ornitorrnico(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        #print(Ornitorrnico.__mro__) #da a ordem da resolução para encotrar atributos
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)


g = Gato(numero_patas=4, cor_pelo='Preto')
print(g)


ornitorrinco = Ornitorrnico(numero_patas=2, cor_pelo='vermelho', cor_bico='laranja')
print(ornitorrinco)