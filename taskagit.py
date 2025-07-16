import random
while True:
    oyuncu=input("Tas,Kagit,Makas Secin: ").lower()
    komputer=random.choice(["tas","kagit","makas"])
    if oyuncu not in ["tas", "kagit", "makas"]:
        print("Yalniz 'tas', 'kagit' ve 'makas' sece bilersiniz.")
        continue
    elif oyuncu == "tas" and komputer == "makas" or oyuncu == "kagit" and komputer == "tas" or oyuncu == "makas" and komputer == "kagit":
        print(f"Komputerin secimi: {komputer}. Siz qazandiniz!")
        break
    elif oyuncu == komputer:
        print(f"Komputerin secimi: {komputer}. Berabere!")
        break
    else:
        print(f"Komputerin secimi: {komputer}. Komputer qazandi!")
        break