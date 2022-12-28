# klavyeden girilen bir sayının karesini,küpünü ve karekökünü alan programı yazınız

import math


sayi = int(input("Lütfen bir sayi giriniz: "))

sayi_karesi = sayi**2
sayi_küpü = sayi**3
sayi_karekökü = math.sqrt(sayi)

print("Girdiginiz sayinin karesi: {}\nKüpü: {}\nKarekökü: {}\n".format(sayi_karesi,sayi_küpü,sayi_karekökü))