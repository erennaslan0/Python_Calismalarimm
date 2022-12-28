sayi = int(input("Lütfen bir sayı giriniz: "))

if sayi < 0:
    print("Girdiğiniz sayı negatiftir.")
elif sayi == 0:
    print("Girdiğiniz sayı nötrdür.")    
else:
    print("Girdiğiniz sayı pozitiftir.") 
    
##############################################################################################    
      
    
işlem = input("Lütfen bir işlem giriniz: ")

if işlem == "1":
    print("İşlem 1 seçildi.") 
elif işlem == "2":
    print("İşlem 2 seçildi.")       
elif işlem == "3":
    print("İşlem 3 seçildi.")
elif işlem == "4":
    print("İşlem 4 seçildi.")
else:
    print("Geçersiz işlem!!! ")   
    
##############################################################################################      


note = float(input("Lütfen notunuzu giriniz: "))

if (note >= 90):
    print("AA")    
elif (note >= 85):
    print("BA")
elif (note >= 80):
    print("BB")
elif (note >= 75):
    print("CB")
elif (note >= 70):
    print("CC")
elif (note >= 65):
    print("DC")
elif (note >= 60):
    print("DD")
else:
    print("KALDINIZ!!! ")   
    
############################################################################################

#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 #Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 #BKİ 18.5'un altındaysa -------> Zayıf

 #BKİ 18.5 ile 25 arasındaysa ------> Normal

 #BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 #BKİ 30'un üstündeyse -------------> Obez                             
    
    
kilo = int(input("Lütfen kilonuzu giriniz: "))
boy = float(input("Lütfen boyunuzu giriniz: "))
beden_kitle_endeksi = kilo / boy**2

if beden_kitle_endeksi < 18.5:
    print("Zayıfsınız")
elif beden_kitle_endeksi >= 18.5 and beden_kitle_endeksi < 25:
    print("Normalsiniz")
elif beden_kitle_endeksi >= 25 and beden_kitle_endeksi < 30:
    print("Fazla kilolusunuz")
else:
    print("Obezsiniz")                
    