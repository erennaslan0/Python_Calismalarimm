print("""
******************************************** 
 
Atm Makinesine Hosgeldiniz
 

İslemler;

1.Bakiye Sorgulama

2.Para Yatirma

3.Para çekme

Programdan çikmak için 'q' ya basin.

********************************************       
""")

bakiye = 1000

while True:
    işlem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    if işlem == "q":
        print("Yine bekleriz...")
        break
    elif işlem == "1":
        print("Bakiyeniz {} TL'dir ".format(bakiye))
    elif işlem == "2":
        miktar = int(input("Lütfen yatirmak istediğiniz tutari giriniz "))
        bakiye += miktar
    elif işlem == "3":
        miktar == int(input("Lütfen çekmek istediğiniz tutari giriniz"))
        if bakiye - miktar == 0:
            print("Bu miktari çekemezsiniz")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem")    
                 
      