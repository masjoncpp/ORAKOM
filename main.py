def desimal_ke_lain(n, basis):
    if basis == 2:
        return bin(n)[2:]  # Hilangkan '0b' untuk biner
    elif basis == 8:
        return oct(n)[2:]  # Hilangkan '0o' untuk oktal
    elif basis == 16:
        return hex(n)[2:]  # Hilangkan '0x' untuk hexadesimal
    else:
        return "Basis tidak valid"

def lain_ke_desimal(n, basis):
    return int(n, basis)

def main():
    while True:  # Looping utama
        print("\nPilih jenis bilangan yang akan dikonversi:")
        print("1. Desimal")
        print("2. Hexadesimal")
        print("3. Oktal")
        print("4. Biner")
        print("5. Keluar")
        jenis = input("Masukkan pilihan (1-5): ")

        if jenis == '5':  # Opsi keluar
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break

        if jenis not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        if jenis == '1':
            bilangan = input("Masukkan bilangan desimal: ")
            try:
                bilangan = int(bilangan)
            except ValueError:
                print("Input tidak valid. Harap masukkan bilangan desimal.")
                continue
        elif jenis == '2':
            bilangan = input("Masukkan bilangan hexadesimal: ")
        elif jenis == '3':
            bilangan = input("Masukkan bilangan oktal: ")
        elif jenis == '4':
            bilangan = input("Masukkan bilangan biner: ")

        print("\nMau dikonversikan kemana?")
        print("1. Desimal")
        print("2. Hexadesimal")
        print("3. Oktal")
        print("4. Biner")
        tujuan = input("Masukkan pilihan (1-4): ")

        if tujuan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        if jenis == '1':
            if tujuan == '1':
                print("Hasil konversi:", bilangan)
            elif tujuan == '2':
                print("Hasil konversi:", desimal_ke_lain(bilangan, 16))
            elif tujuan == '3':
                print("Hasil konversi:", desimal_ke_lain(bilangan, 8))
            elif tujuan == '4':
                print("Hasil konversi:", desimal_ke_lain(bilangan, 2))
        elif jenis == '2':
            if tujuan == '1':
                print("Hasil konversi:", lain_ke_desimal(bilangan, 16))
            elif tujuan == '2':
                print("Hasil konversi:", bilangan)
            elif tujuan == '3':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 16), 8))
            elif tujuan == '4':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 16), 2))
        elif jenis == '3':
            if tujuan == '1':
                print("Hasil konversi:", lain_ke_desimal(bilangan, 8))
            elif tujuan == '2':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 8), 16))
            elif tujuan == '3':
                print("Hasil konversi:", bilangan)
            elif tujuan == '4':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 8), 2))
        elif jenis == '4':
            if tujuan == '1':
                print("Hasil konversi:", lain_ke_desimal(bilangan, 2))
            elif tujuan == '2':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 2), 16))
            elif tujuan == '3':
                print("Hasil konversi:", desimal_ke_lain(lain_ke_desimal(bilangan, 2), 8))
            elif tujuan == '4':
                print("Hasil konversi:", bilangan)

if __name__ == "__main__":
    main()
