import random
print ("RUS RULETİ OYUNUNA HOŞGELDİNİZ...")
başla = input("LÜTFEN HERHANGİ BİR TUŞA BASINIZ: ")
rulet = random.randint(1, 6)
print ("KURŞUN YÜKLENİYOR...")
if rulet == random.randint(1, 6):
    print("MAALESEF ELENDİNİZ...")
elif rulet < random.randint(1, 6):
    print ("ŞANSLISINIZ,GEÇTİNİZ...")
else:
    print("ŞANSLISINIZ,YİNE GEÇTİNİZ...")