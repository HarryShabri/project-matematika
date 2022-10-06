import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('grey')
t.color('white')
t.speed(5)
t.goto(-250,0)
t.forward(500)
t.left(90)
t.forward(200)
t.left(90)
t.forward(500)
t.left(90)
t.forward(200)
t.color('white')
t.penup()
t.goto(0,90)
t.write("KELOMPOK 1 MATEMATIKA DASAR", align='center', font='Times 20 normal')
t.color('white')
t.penup()
t.goto(-220,-50)
t.write("Nama anggota : ", align='center', font='Times 18 normal')
t.color('white')
t.penup()
t.goto(-220,-80)
t.write("1. Harry Shabri", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(-220,-110)
t.write("2.......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(-220,-140)
t.write("3.......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(-220,-170)
t.write("4.......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(-220,-200)
t.write("5.......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(-220,-230)
t.write("6.......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-80)
t.write("Nim : 17220385", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-110)
t.write("Nim......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-140)
t.write("Nim......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-170)
t.write("Nim......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-200)
t.write("Nim......", align='center', font='Times 15 normal')
t.color('white')
t.penup()
t.goto(50,-230)
t.write("Nim......", align='center', font='Times 15 normal')

t.color('red')
t.penup()
t.goto(190,300)
t.write("*Silahkan tutup python turtle graphics untuk menjalankan program", align='center', font='Times 10 normal')
t.hideturtle()
turtle.done()
#Fungsi def
def luaspersegi(sisi):
    luas = sisi * sisi
    return(luas)
def kelilingpersegi(sisi):
    keliling = 4 * sisi
    return(keliling)
def luaspersegipanjang(panjang, lebar):
    luas = panjang * lebar
    return(luas)
def kelilingpersegipanjang(panjang, lebar):
    keliling = 2*(panjang+lebar)
    return(keliling)
def luassegitiga(alas, tinggi):
    luas = 0.5*alas*tinggi
    return(luas)
def kelilingsegitiga(sisi1, sisi2, sisi3):
    keliling = sisi1+sisi2+sisi3
    return(keliling)
def luaslingkaran(r):
    luas = 3.14*r*r
    return(luas)
def kelilinglingkaran(r):
    keliling = 2*3.14*r
    return(keliling)
def luasjajargenjang(alas, tinggi):
    luas = alas*tinggi
    return(luas)
def kelilingjajargenjang(alas, sisimiring):
    keliling = 2*(alas+sisimiring)
    return(keliling)
def volumekubus(sisi):
    volume = sisi*sisi*sisi
    return(volume)
def luaskubus(sisi):
    luas = 6*sisi*sisi
    return(luas)
def Volumebalok(panjang, Lebar, tinggi):
    volume = panjang * Lebar * tinggi
    return(volume)
def Luasbalok(panjang, Lebar, tinggi):
    luas = (2*panjang*Lebar)+(2*Lebar*tinggi)+(2*panjang*tinggi)
    return(luas)
def Volumetabung(r,tinggi):
    Volume = 3.14*r*r*tinggi
    return(Volume)
def Luastabung(r,tinggi):
    Luas = 2*3.14*r*(r+tinggi)
    return(Luas)
def Volumebola(r):
    volume = 4/3*3.14*r*r*r
    return(volume)
def Luasbola(r):
    luas = 4*3.14*r*r
    return(luas)
def Volumekerucut(r,tinggi):
    volume = 1/3*3.14*r*r*tinggi
    return(volume)
def Luaskerucut(r,sisi):
    luas = 3.14*r*(r + sisi)
    return(luas)
#PROGRAM MENU

menu_bangunan = ("")
bangun_datar = ("")
bangun_ruang = ("")
menu_operasi = ("")

while menu_bangunan !=0:
    print("========MATEMATIKA DASAR========")
    print("1. Bangun datar")
    print("2. Bangun ruang")
    print("3. Selesai ")
    print('================================')
    menu_bangunan = int(input("\nmasukkan menu yang diinginkan  :"))
    if menu_bangunan == 1 :
        print('''
========================================
|| 1. Segitiga                        ||
|| 2. Lingkaran                       ||
|| 3. Jajar genjang                   ||
|| 4. Persegi                         ||
|| 5. Persegi panjang                 ||
|| 6. Kembali                         ||
========================================''')
        while bangun_datar !=0 :
            bangun_datar = int(input("\nmasukkan bangun datar yang dipilih  :"))
            if bangun_datar == 1:
                while menu_operasi !=0:
                    print('''
=====================================
|| 1. Luas Segitiga                ||
|| 2. Keliling segitiga            ||
=====================================''')
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("==================================")
                        a=int(input("Masukan Alas Segitiga : "))
                        t=int(input("Masukan Tinggi Segitiga : "))
                        print("Luas Segitiga : ", luassegitiga(a,t) , "cm2")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        s1=int(input("Masukan sisi1 Segitiga : "))
                        s2=int(input("Masukan sisi2 Segitiga : "))
                        s3=int(input("Masukan sisi3 Segitiga : "))
                        print("keliling Persegi Panjang : ", kelilingsegitiga(s1,s2,s3) , "cm")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Segitiga")
                        print("2. Lingkaran")
                        print("3. Jajar genjang")
                        print("4. Persegi")
                        print("5. Persegi panjang")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")                
            elif bangun_datar == 2:
                while menu_operasi !=0 :
                    print("===================================")
                    print("1. Luas Lingkaran")
                    print("2. Keliling Lingkaran")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        r=int(input("Masukan Jari-jari lingkaran : "))
                        print("Luas Lingkaran : ", luaslingkaran(r) , "cm2")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        r=int(input("Masukan Jari-jari lingkaran : "))
                        print("Luas Lingkaran : ", kelilinglingkaran(r) , "cm")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Segitiga")
                        print("2. Lingkaran")
                        print("3. Jajar genjang")
                        print("4. Persegi")
                        print("5. Persegi panjang")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia") 
            elif bangun_datar == 3:
                while menu_operasi !=0 :
                    print("===================================")
                    print("1. Luas Jajar genjang")
                    print("2. Keliling Jajar genjang")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        a=int(input("Masukan Alas Jajargenjang : "))
                        t=int(input("Masukan Tinggi Jajargenjang : "))
                        print("Luas Jajar genjang : ", luasjajargenjang(a,t) , "cm2")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        a=int(input("Masukan Alas Jajargenjang : "))
                        s=int(input("Masukan Sisi Miring Jajargenjang : "))
                        print("Keliling Jajar genjang : ", kelilingjajargenjang(a,s) , "cm")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Segitiga")
                        print("2. Lingkaran")
                        print("3. Jajar genjang")
                        print("4. Persegi")
                        print("5. Persegi panjang")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")   
            elif bangun_datar == 4:
                while menu_operasi!=0 :
                    print("===================================")
                    print("1. Luas Persegi")
                    print("2. Keliling Persegi")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        s=int(input("Masukan sisi Persegi : "))
                        print("Luas persegi : ", luaspersegi(s) , "cm2")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        s=int(input("Masukan sisi Persegi : "))
                        print("Keliling persegi : ", kelilingpersegi(s) , "cm")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Segitiga")
                        print("2. Lingkaran")
                        print("3. Jajar genjang")
                        print("4. Persegi")
                        print("5. Persegi panjang")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_datar == 5:
                while menu_operasi !=0 :
                    print("===================================")
                    print("1. Luas Persegi panjang")
                    print("2. Keliling Persegi panjang")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        p=int(input("Masukan panjang Persegi Panjang : "))
                        l=int(input("Masukan lebar Persegi Panjang : "))
                        print("Luas Persegi Panjang : ", luaspersegipanjang(p,l) , "cm2")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        p=int(input("Masukan panjang Persegi Panjang : "))
                        l=int(input("Masukan lebar Persegi Panjang : "))
                        print("keliling Persegi Panjang : ", kelilingpersegipanjang(p,l) , "cm")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Segitiga")
                        print("2. Lingkaran")
                        print("3. Jajar genjang")
                        print("4. Persegi")
                        print("5. Persegi panjang")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_datar == 6:
                    break
            else:
                print("menu tidak tersedia")
                print("===================================")
                print("1. Segitiga")
                print("2. Lingkaran")
                print("3. Jajar genjang")
                print("4. Persegi")
                print("5. Persegi panjang")
                print("\n6. Kembali")
                print("===================================")
    elif menu_bangunan == 2:
        print('''
========================================
|| 1. Kubus                           ||
|| 2. Balok                           ||
|| 3. Tabung                          ||
|| 4. Bola                            ||
|| 5. Kerucut                         ||
|| 6. Kembali                         ||
========================================''')
        while bangun_ruang !=0 :
            bangun_ruang = int(input("\nmasukkan bangun ruang yang dipilih  :"))
            if bangun_ruang == 1:
                while menu_operasi !=0:
                    print("===================================")
                    print("1. Volume Kubus")
                    print("2. Luas Kubus")
                    print("3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        s=int(input("Masukan sisi kubus : "))
                        print("Volume kubus : ", volumekubus(s) , "cm3")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        s=int(input("Masukan sisi kubus : "))
                        print("Luas kubus : ", luaskubus(s) , "cm2")
                        print("===================================")
                    elif menu_operasi == 3:
                        print("===================================")
                        print("1. Kubus")
                        print("2. Balok")
                        print("3. Tabung")
                        print("4. Bola ")
                        print("5. Kerucut")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_ruang == 2:
                while menu_operasi !=0:
                    print("===================================")
                    print("1. Volume Balok")
                    print("2. Luas Balok")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        p=int(input("Masukan panjang balok : "))
                        l=int(input("Masukan lebar balok : "))
                        t=int(input("Masukan tinggi balok : "))
                        print("Volume balok : ", Volumebalok(p,l,t) , "cm3")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        p=int(input("Masukan panjang balok : "))
                        l=int(input("Masukan lebar balok : "))
                        t=int(input("Masukan tinggi balok : "))
                        print("Volume balok : ", Luasbalok(p,l,t) , "cm2")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Kubus")
                        print("2. Balok")
                        print("3. Tabung")
                        print("4. Bola ")
                        print("5. Kerucut")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_ruang == 3:
                while menu_operasi !=0:
                    print("===================================")
                    print("1. Volume Tabung")
                    print("2. Luas Tabung")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        r=int(input("Masukan Jari-jari tabung : "))
                        t=int(input("Masukan Tinggi tabung : "))
                        print("Volume tabung : ", Volumetabung(r,t) , "cm3")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        r=int(input("Masukan Jari-jari tabung : "))
                        t=int(input("Masukan Tinggi tabung : "))
                        print("Luas tabung : ", Luastabung(r,t) , "cm2")
                        print("===================================")
                    elif menu_operasi == 3:
                        print("===================================")
                        print("1. Kubus")
                        print("2. Balok")
                        print("3. Tabung")
                        print("4. Bola ")
                        print("5. Kerucut")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_ruang == 4:
                while menu_operasi !=0 :
                    print("1. Volume Bola")
                    print("2. Luas Bola")
                    print("\n3. Kembali")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        r=int(input("Masukan Jari-jari bola : "))
                        print("Volume bola : ", Volumebola(r) , "cm3")
                        print("")
                        print("")
                    elif menu_operasi == 2:
                        print("===================================")
                        r=int(input("Masukan Jari-jari bola : "))
                        print("Luas bola : ", Luasbola(r) , "cm2")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Kubus")
                        print("2. Balok")
                        print("3. Tabung")
                        print("4. Bola ")
                        print("5. Kerucut")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_ruang == 5:
                while menu_operasi !=0:
                    print("===================================")
                    print("1. Volume Kerucut")
                    print("2. Luas Kerucut")
                    print("\n3. Kembali")
                    print("===================================")
                    menu_operasi = int(input("\nmasukkan operasi yang dipilih  :"))
                    if menu_operasi == 1 :
                        print("===================================")
                        r=int(input("Masukan Jari-jari kerucut : "))
                        t=int(input("Masukan Tinggi kerucut : "))
                        print("Volume kerucut : ", Volumekerucut(r,t) , "cm3")
                        print("===================================")
                    elif menu_operasi == 2:
                        print("===================================")
                        r=int(input("Masukan Jari-jari kerucut : "))
                        s=int(input("Masukan Sisi kerucut : "))
                        print("Luas kerucut : ", Luaskerucut(r,s) , "cm2")
                        print("===================================")
                    elif menu_operasi == 3 :
                        print("===================================")
                        print("1. Kubus")
                        print("2. Balok")
                        print("3. Tabung")
                        print("4. Bola ")
                        print("5. Kerucut")
                        print("\n6. Kembali")
                        print("===================================")
                        break
                    else:
                        print("menu tidak tersedia")
            elif bangun_ruang == 6 :
                break
            else:
                print("menu tidak tersedia")
    elif menu_bangunan == 3:
        print("=================================================")
        print("||                                             ||")
        print("||       Terimakasih telah menggunakan         ||")
        print("||                                             ||")
        print("=================================================")
        break
    else:
        print("menu tidak tersedia")
else : 
    print("input yang anda masukkan salah")