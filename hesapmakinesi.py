
try:
    print("Hesap makinesi uygulamasına hoş geldin, en fazla 5 sayıyla işlem yapabilirsin")
    sayı=int(input("Kaç sayıyla işlem yapacağını gir: "))
    while (sayı<=0 or sayı>5 or sayı==1):
        sayı=int(input("Lütfen kaç sayıyla işlem yapacağını gir: "))
    else:
        if sayı==2:
            sayi1=int(input("Birinci sayıyı giriniz: "))
            sayi2=int(input("İkinci sayıyı giriniz: "))
            islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            while not (islem=='t' or islem=='çı' or islem=='ça', islem=='b'):
                islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            else:
                if islem=='t':
                    print("Toplama işleminin sonucu {}".format(sayi1 + sayi2))
                elif islem=='çı':
                    print("Çıkarma işleminin sonucu {} ".format(sayi1 - sayi2))
                elif islem=='ça':
                    print("Çarpma işleminin sonucu {} ".format(sayi1 * sayi2))
                elif islem=='b':
                    print("Bölme işleminin sonucu {} ".format(sayi1 / sayi2))
        elif sayı==3:
            sayi1=int(input("Birinci sayıyı giriniz: "))
            sayi2=int(input("İkinci sayıyı giriniz: "))
            sayi3=int(input("Üçüncü sayıyı giriniz: "))
            islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            while not (islem=='t' or islem=='çı' or islem=='ça', islem=='b'):
                islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            else:
                if islem=='t':
                    print("Toplama işleminin sonucu {}".format(sayi1 + sayi2 + sayi3))
                elif islem=='çı':
                    print("Çıkarma işleminin sonucu {} ".format(sayi1 - sayi2 - sayi3))
                elif islem=='ça':
                    print("Çarpma işleminin sonucu {} ".format(sayi1 * sayi2 * sayi3))
                elif islem=='b':
                    print("Bölme işleminin sonucu {} ".format(sayi1 / sayi2 / sayi3))
        elif sayı==4:
            sayi1=int(input("Birinci sayıyı giriniz: "))
            sayi2=int(input("İkinci sayıyı giriniz: "))
            sayi3=int(input("Üçüncü sayıyı giriniz: "))
            sayi4=int(input("Dördüncü sayıyı giriniz: "))
            islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            while not (islem=='t' or islem=='çı' or islem=='ça', islem=='b'):
                islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            else:
                if islem=='t':
                    print("Toplama işleminin sonucu {}".format(sayi1 + sayi2 + sayi3 + sayi4))
                elif islem=='çı':
                    print("Çıkarma işleminin sonucu {} ".format(sayi1 - sayi2 - sayi3 - sayi4))
                elif islem=='ça':
                    print("Çarpma işleminin sonucu {} ".format(sayi1 * sayi2 * sayi3 * sayi4))
                elif islem=='b':
                    print("Bölme işleminin sonucu {} ".format(sayi1 / sayi2 / sayi3 / sayi4))
        elif sayı==5:
            sayi1=int(input("Birinci sayıyı giriniz: "))
            sayi2=int(input("İkinci sayıyı giriniz: "))
            sayi3=int(input("Üçüncü sayıyı giriniz: "))
            sayi4=int(input("Dördüncü sayıyı giriniz: "))
            sayi5=int(input("Beşinci sayıyı giriniz: "))
            islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            while not (islem=='t' or islem=='çı' or islem=='ça', islem=='b'):
                islem=str(input("Hangi işlemi yapmak istiyorsun (t, çı, ça, b): "))
            else:
                if islem=='t':
                    print("Toplama işleminin sonucu {}".format(sayi1 + sayi2 + sayi3 + sayi4 + sayi5))
                elif islem=='çı':
                    print("Çıkarma işleminin sonucu {} ".format(sayi1 - sayi2 - sayi3 - sayi4 - sayi5))
                elif islem=='ça':
                    print("Çarpma işleminin sonucu {} ".format(sayi1 * sayi2 * sayi3 * sayi4 * sayi5))
                elif islem=='b':
                    print("Bölme işleminin sonucu {} ".format(sayi1 / sayi2 / sayi3 / sayi4 / sayi5))
except:
    print("Program durdu")
finally:
    print("Uygulamayı kullandığınız için teşekkür ederiz")