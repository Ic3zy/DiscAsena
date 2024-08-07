import oyun.databaseveri as databaseveri
import random

databaseveri.connect()
approval, coin_amount, daily_date, time = databaseveri.verigetir("test")
para = coin_amount
print("Başlangıç parası:", para)
rul = random.randint(1, 36)
print("Rulet Sayısı:", rul)
oynalar = input("Hangi sayıyı veya renkleri oynamak istersin? (Örnek: 12, 13, kırmızı, siyah) ")
pare = input("Kaç lira ile oynamak istersin? ")
try:
    pare = int(pare)
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
    pare = 0
toplam_pare = pare * len(oynalar.replace(" ", "").split(','))
if toplam_pare > para:
    print("Bakiye yetersiz. Bahis miktarınızı azaltın.")
else:
    birst12 = list(range(1, 13))
    ikist12 = list(range(13, 25))
    ucst12 = list(range(25, 37))
    birto18 = list(range(1, 19))
    ondokuzto36 = list(range(19, 37))
    kirmizi = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    siyah = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    birst = "None"
    onsekiz = "None"
    skrl = "None"
    if rul in birst12:
        birst = "st12"
    elif rul in ikist12:
        birst = "nd12"
    elif rul in ucst12:
        birst = "rd12"
    if rul in birto18:
        onsekiz = "1to19"
    elif rul in ondokuzto36:
        onsekiz = "19to36"
    if rul in kirmizi:
        skrl = "kırmızı"
    elif rul in siyah:
        skrl = "siyah"
    oynalar = oynalar.replace(" ", "").split(',')
    kazanc = 0
    for oyna in oynalar:
        if oyna.isdigit():
            oyna = int(oyna)
            if oyna == rul:
                kazanc += pare * 34
                print(f"{oyna} sayısına bahis kazandınız! Kazancınız: {pare * 34} lira")
        elif oyna == "siyah":
            if oyna == skrl:
                kazanc += pare * 2
                print(f"Siyah bahsi kazandınız! Kazancınız: {pare * 2} lira")
        elif oyna == "kırmızı":
            if oyna == skrl:
                kazanc += pare * 2
                print(f"Kırmızı bahsi kazandınız! Kazancınız: {pare * 2} lira")
        elif oyna == "1to19":
            if oyna == onsekiz:
                kazanc += pare * 2
                print(f"1 to 19 bahsi kazandınız! Kazancınız: {pare * 2} lira")
        elif oyna == "19to36":
            if oyna == onsekiz:
                kazanc += pare * 2
                print(f"19 to 36 bahsi kazandınız! Kazancınız: {pare * 2} lira")
        elif oyna == "st12":
            if oyna == birst:
                kazanc += pare * 3
                print(f"1st 12 bahsi kazandınız! Kazancınız: {pare * 3} lira")
        elif oyna == "nd12":
            if oyna == birst:
                kazanc += pare * 3
                print(f"2nd 12 bahsi kazandınız! Kazancınız: {pare * 3} lira")
        elif oyna == "rd12":
            if oyna == birst:
                kazanc += pare * 3
                print(f"3rd 12 bahsi kazandınız! Kazancınız: {pare * 3} lira")
        else:
            print(f"Geçersiz bahis: {oyna}")
    para -= toplam_pare
    para += kazanc
    if kazanc == 0:
        print(f"Hiçbir bahis kazanamadınız. Kaybedilen tutar: {toplam_pare} lira")
    else:
        kaybedilen_tutar = toplam_pare - kazanc
        print(f"Toplam kazancınız: {kazanc} lira")
        print(f"Toplam kaybedilen tutar: {kaybedilen_tutar} lira")
    databaseveri.yaz("test", para)
    print(f"Yeni bakiye: {para} lira")
