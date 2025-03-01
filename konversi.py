def konversi_bilangan():
    while True:
        # Untuk Menampilkan pilihan menu program
        print("\nPilih Menu Konversi :")
        print("1. Desimal Ke Oktal")
        print("2. Desimal Ke Hexadesimal")
        print("3. Oktal Ke Desimal")
        print("4. Hexadesimal ke Desimal")
        print("5. Keluar")

        # memilih pilihan program
        pilihan = input("Pilih Program (1/2/3/4/5) : ")

        # Jika pengguna memilih opsi 1
        if pilihan == '1':
            desimal = int(input("Masukkan bilangan desimal : "))
            oktal = oct(desimal)[2:]
            print(f"Bilangan Oktal: {oktal}")

        # Jika pengguna memilih opsi 2
        elif pilihan == '2':
            desimal = int(input("Masukkan Bilangan Desimal : "))
            hexadesimal = hex(desimal)[2:]
            print(f"Bilangan Hexadesimal: {hexadesimal}")

        # Jika pengguna memilih opsi 3
        elif pilihan == '3':
            oktal = input("Masukkan bilangan Oktal : ")
            desimal = int(oktal, 8)
            print(f"Bilangan Desimal: {desimal}")

        # Jika pengguna memilih opsi 4
        elif pilihan == '4':
            hexadesimal = input("Masukkan bilangan Hexadesimal : ")
            desimal = int(hexadesimal, 16)
            print(f"Bilangan Desimal: {desimal}")

        # Jika pengguna memilih opsi 5 untuk keluar
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program konversi bilangan.")
            break

        # Jika pengguna memilih opsi yang tidak ada dalam menu
        else:
            print("Input Tidak Ada! Silakan pilih opsi yang valid.")

# Memanggil fungsi program
konversi_bilangan()
