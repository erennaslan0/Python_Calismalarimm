# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) ** 2

boy = float(input("Lütfen boyunuzu giriniz: "))
kilo = int(input("Lütfen kilonuzu giriniz: "))
print("beden kitle endeksiniz:",kilo / (boy**2))

#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

#Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input("a: "))
b = int(input("b: "))
c = (a**2 + b**2)**0.5
print("Hipotenüs: ",c)

# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

yakan_miktar = float(input("kilometrede yaktıgı miktar: "))
yol = int(input("Kac kilometre yol yaptıgınızı giriniz: "))
print("Tutar: {} TL ".format(yakan_miktar * yol))

# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = input("Lütfen adınızı giriniz: ")
soyad = input("Lütfen soyadınızı giriniz: ")
numara = int(input("Lütfen numaranızı giriniz: "))
print("\nBilgiler...\n")
print("{}\n{}\n{}\n".format(ad,soyad,numara))