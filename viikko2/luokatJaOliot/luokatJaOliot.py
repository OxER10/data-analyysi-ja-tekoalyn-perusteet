class Murtoluku:
    osoittaja = 1
    nimittäjä = 2
    
    def __init__(self, osoittaja, nimittäjä):
        self.osoittaja = osoittaja
        self.nimittäjä = nimittäjä
        
    def sievenna(self):
        a = self.osoittaja
        b = self.nimittäjä
        
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        
        self.osoittaja /= a
        self.nimittäjä /= a
    
    def tulosta(self):
        print(f"{int(self.osoittaja)} / {int(self.nimittäjä)}")

murtoluku1 = Murtoluku(34562,311058)
murtoluku1.tulosta()
murtoluku1.sievenna()
murtoluku1.tulosta()