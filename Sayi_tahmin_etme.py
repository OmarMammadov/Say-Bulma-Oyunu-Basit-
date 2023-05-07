from colorama import Fore

print(Fore.RED + "SAYI TAHMİN ETME OYUNU-1")

print(Fore.WHITE + "Seviye Seç;""\n" + Fore.MAGENTA + "1-KOLAY(0-50 Arası)""\n""2-ORTA(0-100 Arası)""\n""3-ZOR(0-1000 Arası)")

zorluk = int(input(Fore.YELLOW + "Lütfen Başlamadan Önce Zorluk Seviyesini Belirleyiniz(1/2/3): " + Fore.RESET))


from random import randint

rand = randint(0,50)
rand1 = randint(0,100)
rand2 = randint(0,1000)

if zorluk == 1:
    y = 50
    x = rand
    while True:
        sayı = int(input(Fore.RESET + "Sayıyı Tahmin Edin: "))

        if sayı == x:
            print(Fore.GREEN + "TEBRİKLER SONUNDA SAYIYI BULDUNUZ !!!")
            exit()

        elif sayı < x:
            print(Fore.LIGHTBLUE_EX + "Daha yukarı çık")

        elif sayı > x:
            print(Fore.LIGHTRED_EX + "biraz daha in")

        if sayı > 50:
            print(Fore.RED + "O KADAR DA UÇMA CANIM sayı 0-50 Aralığındadır.")

        if sayı < 0:
            print(Fore.RED + "SAÇMALAMA İSTERSEN Sayı 0-50 Aralığındadır.")


#----------------------------------------------------------
if zorluk == 2:
    y = rand1
    while True:
        sayı2 = int(input(Fore.RESET + "Sayıyı Tahmin Edin: "))

        if sayı2 == y:
            print(Fore.GREEN + "TEBRİKLER SONUNDA SAYIYI BULDUNUZ !!!")
            exit()

        elif sayı2 < y:
            print(Fore.LIGHTBLUE_EX + "Daha yukarı çık")

        elif sayı2 > y:
            print(Fore.LIGHTRED_EX + "biraz daha in")

        if sayı2 > 100:
            print(Fore.RED + "SAÇMALAMA Sayı 0-100 Aralığındadır.")

        if sayı2 < 0:
            print(Fore.RED + "YOK DAHA NELER Sayı 0-100 Aralığındadır.")

#---------------------------------------------------------

if zorluk == 3:
    z = rand2
    while True:
        sayı3 = int(input(Fore.RESET + "Sayıyı Tahmin Edin: "))

        if sayı3 == z:
            print(Fore.GREEN + "TEBRİKLER SONUNDA SAYIYI BULDUNUZ !!!")
            exit()

        elif sayı3 < z:
            print(Fore.LIGHTBLUE_EX + "Daha yukarı çık")

        elif sayı3 > z:
            print(Fore.LIGHTRED_EX + "biraz daha in")

        if sayı3 > 1000:
            print(Fore.RED + ("ABARTMA Sayı 0-1000 Aralığındadır."))

        if sayı3 < 0:
            print(Fore.RED + "YOK DAHA NELER Sayı 0-1000 Aralığındadır.")
