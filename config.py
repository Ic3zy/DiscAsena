def alive():
    ALİVE = "default"
    if ALİVE == "default":
        ALİVE = (
            "Tanrı Türk'ü Korusun. 🐺 Asena Hizmetinde!\n\n"
            "Version:0,26 Public\n"
            "Branch:Master\n"
            "Telegram Group: ttps://t.me/AsenaSupport\n"
            "Telegram Channel: ttps://t.me/asenaremaster\n"
            "Plugin Channel: ttps://t.me/asenaplugin\n"
            "Asena Kullanıcısı: "
        )
    return ALİVE

def dctkn():
    TOKEN = 'YOUR BOT TOKEN'
    return TOKEN

def athr():
    AUTHOR = "31ciyusuf"  # Discord kullanıcı adınızı giriniz.
    MAİN_AUTH = "lc3zy"  # Değiştirmeyiniz.
    return AUTHOR, MAİN_AUTH

def wrktyp():
    WORKTYPE = "private"
    if WORKTYPE not in ["private", "public"]:
        print("HATA : BOT WORKTYPE!!!")
        WORKTYPE = "private"
    return WORKTYPE
