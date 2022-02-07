x=0.03
kullanici=' '
isim=str(input("Lütfen İsminizi giriniz \n :"))
kullanici=isim
kilo=int(input("Lütfen Kilonuzu giriniz \n :") .format(kullanici))

hesap=kilo * x
print("""
Sayın {}
Günde {} litre su içmelisiniz !
kilo değeri = {} 



""".format(isim, hesap, kilo))

x=str(input("Başa sarmak için 'başa sar' yazınız, bitimek için 'bitir' yazınız\n "))
while x=='başa sar':
    x=0.03
    kullanici=' '
    isim=str(input("Lütfen İsminizi giriniz \n :"))
    kullanici=isim
    kilo=int(input("Lütfen Kilonuzu giriniz \n :") .format(kullanici))

    hesap=kilo * x
    print("""
    Sayın {}
    Günde {} litre su içmelisiniz !
    kilo değeri = {} 



    """.format(isim, hesap, kilo))
    x=str(input("Başa sarmak için 'başa sar' yazınız, bitirmek için 'bitir' yazınız\n "))
else:
    print("Program bitti")
    pass
