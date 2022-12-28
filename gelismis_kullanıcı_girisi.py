print("""
*********************************
 Kullanici giris programi
*********************************
""")

sys_kullanici_adi = "bbaran"
sys_parola = "1903"
giris_hakki = 3


while True:
    kullanici_adi = input("Kullanici adi: ")
    parola = input("Parola: ")
    
    if kullanici_adi == sys_kullanici_adi and parola != sys_parola:
        print("Parolaniz hatalidir....")
        giris_hakki -= 1
    elif kullanici_adi != sys_kullanici_adi and parola == sys_parola:
         print("Kullanici adi hatali...")
         giris_hakki -= 1
    elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
        print("Kullanici adi ve parola hatalidir")
        giris_hakki -= 1
    else:
        print("programa basarıyla giris yaptiniz...")
        break
    if ( giris_hakki == 0 ):
        print("giris hakkiniz doldu")
        break
    
     
    
    
    
 
    
     
             









    