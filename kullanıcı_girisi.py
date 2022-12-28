print("""********************
KULLANICI GİRİŞİ
***************************      
""")

sys_kullanici_adi = "baranngoktrk"
sys_parola = "12112002"

kullanici_adi = input("Kullanici adini giriniz: ")
parola = input("Parolanızı giriniz: ")

if (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Parola hatalidirr...")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanici adi hatalidirr...")
elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanici adi ve parola hatalidirr...")
else:
    print("Sisteme basariyla giris yaptiniz...")               