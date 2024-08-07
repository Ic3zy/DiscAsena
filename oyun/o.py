import random
klioymk=input("kaç lira")
klioymk=int(klioymk)
liste=["a","b","c"]
liste1=random.choice(liste)
liste2=random.choice(liste)
liste3=random.choice(liste)
if liste1==liste2==liste3:
    klioymk*=3
    print("tebrikler kazandınız kazanılan miktar",klioymk)
else:
    print("tebrikler kaybettiniz kaybedilen miktar",klioymk)