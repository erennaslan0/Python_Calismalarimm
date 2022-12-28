print("""********************
Hesap Makinesi Programı      
      
İşlemler;

1.Toplama İşlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4.Bölme işlemi
******************************      
""")

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz"))
işlem = input("Lütfen bir işlem seçiniz")

if (işlem == "1"):
    print("{} sayısı ile {} sayısının toplamı {}'dır ".format(a,b,a+b))
elif (işlem == "2"):
    print("{} sayısı ile {} sayısının farkı {}'dır ".format(a,b,a-b))
elif (işlem == "3"):
    print("{} sayısı ile {} sayısının çarpımı {}'dır ".format(a,b,a*b))
elif (işlem == "4"):
    print("{} sayısı ile {} sayısının bölümü {}'dır ".format(a,b,a/b))
else:
    print("Geçersiz işlem")                