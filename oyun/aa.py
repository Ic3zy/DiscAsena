import databaseveri

user=str("lc3zy")
approval, coin_amount, daily_date, time = databaseveri.verigetir(user)
time=time.replace(":", "")
zmn=list(time)
zmn1=int(zmn[0]+zmn[1])
zmn2=int(zmn[2]+zmn[3])
toplam_saat, dakika = databaseveri.surehsp(daily_date, zmn1,zmn2)
print(toplam_saat, dakika)
gcnzmn=toplam_saat
"""gcnzmn=gcnzmn.replace(" ","")
gcnzmn=gcnzmn.replace(",","")
gcnzmn=gcnzmn.replace("(","")
gcnzmn=gcnzmn.replace(")","")"""
print(gcnzmn)