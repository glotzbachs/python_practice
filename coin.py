import random

class Penny:

    def __init__(self, rare=False):
        self.value = 0.01
        self.color = 'copper'
        self.num_edges = 1
        self.diameter = 19.05
        self.thickness = 1.52
        self.heads = True
        self.rare=rare
        if self.rare:
            self.value=0.015
    
    def rust(self):
        self.color='greenish'

    def clean(self):
        self.color='copper'

    def flip(self):
        heads = [True, False]
        choice = random.choice(heads)
        self.heads = choice

    def __del__(self):
        print('Coin spent')
    
coin1 = Penny()
coin2 = Penny(rare=True)

print(coin1.value)
print(coin2.value)

print(coin1.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)

print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)

del coin1

print(coin1) #error, coin 1 was deleted!

print(type(coin1))
