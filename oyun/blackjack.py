import random
def hesapla_eldeki_kartlar(kartlar):
    toplam = sum(kartlar)
    as_sayisi = kartlar.count(1)
    while toplam <= 11 and as_sayisi > 0:
        toplam += 10
        as_sayisi -= 1
    return toplam
qkart = random.randint(1, 10)
qkart2 = random.randint(1, 10)
qkart=1
krupye_kartlar = [qkart, qkart2]
print("Krupye kartları:", qkart, qkart2)
kartlar = random.randint(1, 10)
kartlar2 = random.randint(1, 10)
oyuncu_kartlar = [kartlar, kartlar2]
print("Oyuncu kartları:", kartlar, kartlar2)
qkrt = hesapla_eldeki_kartlar(krupye_kartlar)
krt = hesapla_eldeki_kartlar(oyuncu_kartlar)
kbj = krt == 21
qbj = qkrt == 21
if kbj:
    print("Kullanıcı Black Jack!")
    kznn = "oyuncu"
elif qbj:
    print("Kasa Black Jack!")
    kznn = "kasa"
    exit()
ppd = oyuncu_kartlar.count(1) == 2
print(f"Krupye eli : {krupye_kartlar} ({qkrt})\nSenin elin : {oyuncu_kartlar} ({krt})")
ek = input("Kart eklemek ister misin? (evet/hayır): ").lower()
while ek == "evet":
    ekkrt = random.randint(1, 10)
    oyuncu_kartlar.append(ekkrt)
    krt = hesapla_eldeki_kartlar(oyuncu_kartlar)
    print(f"Krupye eli : {krupye_kartlar} ({qkrt})\nSenin elin : {oyuncu_kartlar} ({krt})")
    if krt > 21:
        print("Kasa kazandı")
        exit()
    ek = input("Kart eklemek ister misin? (evet/hayır): ").lower()
while qkrt < 17:
    qek = random.randint(1, 10)
    krupye_kartlar.append(qek)
    qkrt = hesapla_eldeki_kartlar(krupye_kartlar)
    print("Kasa kart çekti:", qkrt)
if krt <= 21:
    if qkrt <= 21:
        if qkrt == krt:
            print("Berabere")
        elif qkrt < krt:
            print("Kullanıcı kazandı")
        else:
            print("Kasa kazandı")
    else:
        print("Kullanıcı kazandı")
else:
    print("Kasa kazandı")
print(f"Krupye eli : {krupye_kartlar} ({qkrt})\nSenin elin : {oyuncu_kartlar} ({krt})")
