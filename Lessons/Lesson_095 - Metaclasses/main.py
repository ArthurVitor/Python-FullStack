class A:
    def fala(self):
        self.b_fala()

class B(A):
    def b_fala(self):
        print('Oi')


b = B()
b.fala()