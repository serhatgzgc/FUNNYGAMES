import random
print ("SAYI TAHMİN OYUNUNA HOŞGELDİNİZ...")
tahmin = int(input("TAHMİNİNİZ NEDİR?: "))
sayi = random.randint(0,100)
if tahmin == sayi:
    print("TEBRİKLER DOĞRU TAHMİN!!!")
elif tahmin < sayi:
    print("LÜTFEN DAHA BÜYÜK BİR SAYI GİRİNİZ")
else :
    print("LÜTFEN DAHA KÜÇÜK BİR SAYI GİRİNİZ")


#Serhat Gezgiç