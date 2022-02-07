from tkinter import *
from tkinter import messagebox
import platform
from tkcalendar import DateEntry
import os
pcadi=("Giriş yapılan hesap -->{} ".format(platform.node()))


loji=Tk()
loji.geometry("1200x600")
loji.title("Kimlik Tanımlama Programı")
loji.config(bg="Gray")

menu=Menu(loji)
loji.config(menu=menu)





d=Menu(menu)

menu.add_command(label=pcadi)



menu.add_command(label="Çıkış", command=loji.destroy)

kayit=Frame(loji, width=1200, height=680)
kayit.place(relx=0.01, rely=0.01)

def kayitet():
    tckimlik=tcentry.get()
    ad=isimentry.get()
    soyad=soyisimentry.get()
    dg=dogum_tarih_Secici.get()
    serinoo=serinoentry.get()
    anne=anneadientry.get()
    baba=babaadientry.get()
    sg=songecerlilik.get()
    tum_bilgiler=("""
            İsim: {}
            Soyisim: {}
            Tc kimlik: {}
            Seri No: {}
            Son Geçerlilik Tarihi: {}
            Doğum Tarihi: {}
            Anne Adı: {}
            Baba Adı: {}
            """).format(ad, soyad.upper(), tckimlik, serinoo.upper(), sg, dg ,anne, baba, )
    dosya=os.open("Kimlik Kartı.txt", os.O_RDWR|os.O_CREAT)
    os.write(dosya, tum_bilgiler.encode())
    os.close(dosya)
    messagebox.showinfo("Başarılı", "Bilgiler Sisteminize Kimlik Kartı Adında Kayıt Edilmiştir")
    
  

#dugme1=Button(loji, text="Kayıt Et", command=kayitet)
#dugme1.place(relx=0.96, rely=0.88, relheight=0.1)

menu.add_command(label="Kayıt Et", command=kayitet)

tc=Label(kayit, text="Tc kimlik numarası", font="Helvetica 15", bg="Gray")
tc.place(relx=0.01, rely=0.02)

tcentry=Entry(kayit, bg="Gray", fg="Black", font="helvetica 15", bd=2)
tcentry.place(relx=0.2, rely=0.02)

isim=Label(kayit, text="İsim", font="Helvetica 15", bg="Gray")
isim.place(relx=0.01, rely=0.1)

isimentry=Entry(kayit, bg="Gray", fg="Black", font="Helvetica 15 bold", bd=2)
isimentry.place(relx=0.2, rely=0.1)


soyisim=Label(kayit, text="Soyisim", font="Helvetica 15", bg="Gray")
soyisim.place(relx=0.01, rely=0.2)

soyisimentry=Entry(kayit, bg="Gray", fg="Black", font="Helvetica 15 bold", bd=2)
soyisimentry.place(relx=0.2, rely=0.2)
soyisimentry.place()

dogumtarihi=Label(text="Doğum Tarihi", font="Helvetica 15", bg="Gray")
dogumtarihi.place(relx=0.02, rely=0.3)

dogum_tarih_Secici=DateEntry(kayit, width=34, background='White', foreground='black', borderwidth=1, locale="de_DE")
dogum_tarih_Secici.place(relx=0.2, rely=0.3)

serino=Label(kayit, text="Seri No", font="Helvetica 15", bg="Gray")
serino.place(relx=0.01, rely=0.4)

serinoentry=Entry(kayit, bg="Gray", fg="Black", font="Helvetica 15 bold", bd=2)
serinoentry.place(rely=0.4, relx=0.2)

anneadi=Label(kayit, text="Anne Adı", font="Helvetica 15", bg="Gray")
anneadi.place(relx=0.01, rely=0.5)

anneadientry=Entry(kayit, bg="Gray", fg="Black", font="Helvetica 15 bold", bd=2)
anneadientry.place(relx=0.2, rely=0.5)

babaadi=Label(kayit, text="Baba Adı", font="Helvetica 15", bg="Gray")
babaadi.place(relx=0.01, rely=0.6)

babaadientry=Entry(kayit, bg="Gray", fg="Black", font="Helvetica 15 bold", bd=2)
babaadientry.place(relx=0.2, rely=0.6)

songecerlilik=DateEntry(kayit, width=34, background='White', foreground='black', borderwidth=1, locale="de_DE")
songecerlilik.place(relx=0.2, rely=0.7)

songecerlilik1=Label(kayit, text="Son Geçerlilik Tarihi", font="Helvetica 15", bg="Gray")
songecerlilik1.place(relx=0.01, rely=0.7)


loji.mainloop()