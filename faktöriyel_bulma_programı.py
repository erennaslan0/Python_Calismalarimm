print("""**********************************
      
FAKTÖRİYEL BULMA PROGRAMI
      
Çıkmak için "q" ya basin.
      
**********************************""")

while True:
      sayi = input("sayi: ")
      if sayi == "q":
            print("Programdan cikiliyor...")
            break
      else:
            sayi = int(sayi)
            
            faktöriyel = 1
            
            for i in range(2,sayi+1):
                  print("Girdiğiniz sayinin faktöriyeli: ",faktöriyel)
                  faktöriyel *= i 
                  
                  
sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"mükemmel bir sayıdır.")
else:
    print(sayı,"mükemmel bir sayı değildir.")                  
                  
            
      
      
      
      