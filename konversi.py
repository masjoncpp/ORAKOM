#untuk mendifinisikan fungsi program
def konversi_bilangan():
    #untuk menampilkan pilihan menu program
    print("Pilih Menu Konversi :")
    print("1. Desimal Ke Oktal")
    print("2. Desimal Ke Hexadesimal")
    print("3. Oktal Ke Desimal")
    print("4. Hexadesimal ke Desimal")
    
    #untuk memanggil input dari pengguna supaya dapat menggunakan program
    pilihan = input("Pilih Program (1/2/3/4) : ")
    
    #jika pengguna memilih opsi 1
    if pilihan == '1':
        #pengguna menginput bilangan desimal
        desimal = int(input("Masukkan bilangan desimal : "))
        #untuk mengkonversi bilangan desimal ke oktal
        oktal = oct(desimal)[2:]
        #menampilkan hasil konversi
        print(f"Bilangan Oktal: {oktal}")

    #jika pengguna memilih opsi 2
    elif pilihan == '2':
        #pengguna menginput bilangan desimal
        desimal = int(input("Masukkan Bilangan Desimal : "))
        #untuk mengkonversi bilangan desimal ke hexadesimal
        hexadesimal = hex(desimal)[2:]
        #menampilkan hasil konversi
        print(f"Bilangan Hexadesimal: {hexadesimal}")

    #jika pengguna memilih opsi 3
    elif pilihan == '3':
        #pengguna menginput bilangan oktal
        oktal = input("Masukkan bilangan Oktal : ")
        #untuk mengkonversi bilangan oktal ke desimal
        desimal = int(oktal, 8)\
        #menampilkan hasil konversi
        print(f"Bilangan Desimal: {desimal}")

    #jika pengguna memilih opsi 4
    elif pilihan == '4':
        #pengguna menginput bilangan hexadesimal
        hexadesimal = input("Masukkan bilangan Hexadesimal : ")
        #untuk mengkonversi bilangan hexadesimal ke desimal
        desimal = int(hexadesimal, 16)
        #menampilkan hasil konversi
        print(f"Bilangan Desimal: {desimal}")

    else:
        print("Input Tidak Ada!")
#untuk memanggil fungsi program 
konversi_bilangan()