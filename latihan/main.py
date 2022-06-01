from pemukul import Pemukul
from penembak import Penembak  
from pengendara import Pengendara 


karakter1 = Penembak("oja", 40)
print(karakter1.menyerang(),",menembak")

karakter2 = Pemukul("Mila", 50)
print(karakter2.menyerang(), ",memukul")

karakter3 = Pengendara("milja", 90)
print(karakter3.menyerang(), ",menabrak")
