from latihan.karakter import Karakter
from penembak import Penembak

class Pemukul(Karakter):
    def __init__(self, nama: str, power: int):
        super().__init__(nama, power)
        
    def menyerang(self):
        print ("mengeluarkan power dengan memukul")