import sqlite3
from datetime import datetime
print("Sqlite3 from coinler ad onay coin daily time sqdbdatabase.db")
con = sqlite3.connect("oyun\\database.db")
cursor = con.cursor()
bonus = datetime.now()
bonusdaily=bonus.strftime("%H:%M")
bonus = bonus.strftime("%Y-%m-%d")
bonus=bonus.replace(" ", "")
bonusdaily=bonusdaily.replace(" ", "")
def tabloostur():
    cursor.execute("CREATE TABLE IF NOT EXISTS coinler(ad TEXT, onay TEXT, coin İNT, daily İNT, time İNT)")
    con.commit()
tabloostur()
def connect():
    con.commit()
    print("scale for coinler con.commit connect /help")
    sver="select * from coinler"
    cursor.execute(sver)
    liste=cursor.fetchall()
    for e in liste:
        print(e)
    con.commit()
def verigetir(username):
    con.commit()
    cursor.execute("SELECT * FROM coinler WHERE ad = ?", (username,))
    veri = cursor.fetchall()
    if not veri:
        return None, None, None, None
    first_entry = veri[0]
    approval = first_entry[1]
    coin_amount = first_entry[2]
    daily_date = first_entry[3]
    time = first_entry[4]
    con.commit()
    return approval, coin_amount, daily_date, time 
def login(username,accept,money,tdail,timr):
    veri= "INSERT INTO coinler VALUES (?,?,?,?,?)"
    cursor.execute(veri,(username,accept,money,tdail,timr))
    con.commit()
def yaz(username,money):
    approval, coin_amount, daily_date, time = verigetir(username)
    oldcoin=coin_amount
    cursor.execute("update coinler set coin = ? where ad = ?", (money,username))
    con.commit()
    return oldcoin
def banned(username):
    cursor.execute("update coinler set onay = ? where ad = ?", ("banned",username))
    con.commit()
def unbanned(username):
    cursor.execute("update coinler set onay = ? where ad = ?", ("yes",username))
    con.commit()
def surehsp(gecmis_tarih, gecmis_saat, gecmis_dakika):
    tarih_str = f"{gecmis_tarih} {gecmis_saat}:{gecmis_dakika}"
    try:
        gecmis_datetime = datetime.strptime(tarih_str, "%Y-%m-%d %H:%M")
    except ValueError as e:
        print(f"Tarih ve saat formatında bir hata oluştu: {e}")
        return None, None
    suanki_datetime = datetime.now()
    fark = suanki_datetime - gecmis_datetime
    toplam_saat = fark.days * 24 + fark.seconds // 3600
    dakika = (fark.seconds % 3600) // 60
    toplam_saat = str(toplam_saat).rjust(2, '0')
    dakika = str(dakika).rjust(2, '0')
    return toplam_saat, dakika
gecmis_tarih = "2024-07-30"
gecmis_saat = "16"
gecmis_dakika = "30"
#örnek kullanım
#login("test","yes","10",bonus,bonusdaily)
