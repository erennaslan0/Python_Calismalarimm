import random 
turaGelen = 0
yaziGelen = 0 
paraYüzeyi = ["Tura","Yazi"]

atilacakPara = int(input("Kac kere para atmak istiyorsunuz? : "))

while atilacakPara > 0:
    paraÜstü = random.choice(paraYüzeyi)
    if paraÜstü == "Tura":
        print("Tura geldi")
        turaGelen += 1
    else:
        print("Yazi geldi")
        yaziGelen += 1
    atilacakPara -= 1
    
print("Yazi sayisi: {}\nTura sayisi: {} ".format(yaziGelen,turaGelen))        
        
                       
