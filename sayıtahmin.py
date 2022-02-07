import random
girilensayi=int(input("Bir sayı giriniz: "))
while not girilensayi>10:
    print("Girilen sayının 10'dan büyük olması gerekiyor")
    girilensayi=int(input("Bir sayı giriniz: "))
else:
    y=random.randint(1, girilensayi)
    sayitahmin=int(input("Sayıyı tahmin edin: "))
while not sayitahmin==y:
    print("Sayı {} değil" .format(sayitahmin))
    sayitahmin=int(input("Sayıyı tahmin edin: "))
else:
    print("Tebrikler sayıyı bildin")
    pass
