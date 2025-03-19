def konversi_biner_ke_desimal(biner):
    """Konversi bilangan biner ke desimal dengan langkah-langkah"""
    steps = []
    steps.append(f"Konversi Biner {biner} ke Desimal:")
    total = 0
    length = len(biner)
    
    for i in range(length):
        bit = biner[i]
        pos = length - 1 - i
        nilai = int(bit) * (2 ** pos)
        steps.append(f"{bit} × 2^{pos} = {nilai}")
        total += nilai
    
    steps.append(f"Total = {' + '.join([str(int(bit) * (2 ** (length-1-i))) for i, bit in enumerate(biner)])} = {total}")
    return total, steps

def konversi_desimal_ke_biner(desimal):
    """Konversi bilangan desimal ke biner dengan langkah-langkah"""
    steps = []
    steps.append(f"Konversi Desimal {desimal} ke Biner:")
    n = int(desimal)
    remainders = []
    
    while n > 0:
        remainder = n % 2
        quotient = n // 2
        steps.append(f"{n} ÷ 2 = {quotient} sisa {remainder}")
        remainders.append(remainder)
        n = quotient
    
    # Menghilangkan langkah terakhir jika hasil bagi adalah 0
    if steps and steps[-1].startswith("1"):
        steps.pop()
    
    remainders.reverse()
    biner = ''.join(map(str, remainders))
    steps.append(f"Membaca sisa dari bawah ke atas: {biner}")
    return biner, steps

def konversi_oktal_ke_desimal(oktal):
    """Konversi bilangan oktal ke desimal dengan langkah-langkah"""
    steps = []
    steps.append(f"Konversi Oktal {oktal} ke Desimal:")
    total = 0
    length = len(oktal)
    
    for i in range(length):
        digit = oktal[i]
        pos = length - 1 - i
        nilai = int(digit) * (8 ** pos)
        steps.append(f"{digit} × 8^{pos} = {nilai}")
        total += nilai
    
    steps.append(f"Total = {' + '.join([f'{d}×8^{len(oktal)-1-i}' for i, d in enumerate(oktal)])} = {total}")
    return total, steps

def konversi_desimal_ke_heksadesimal(desimal):
    """Konversi bilangan desimal ke heksadesimal dengan langkah-langkah"""
    steps = []
    steps.append(f"Konversi Desimal {desimal} ke Heksadesimal:")
    n = int(desimal)
    remainders = []
    hex_chars = "0123456789ABCDEF"
    
    while n > 0:
        remainder = n % 16
        steps.append(f"{n} ÷ 16 = {n//16} sisa {remainder} ({hex_chars[remainder]})")
        remainders.append(remainder)
        n = n // 16
    
    remainders.reverse()
    heksa = ''.join([hex_chars[r] for r in remainders])
    steps.append(f"Membaca sisa dari bawah ke atas: {heksa}")
    return heksa, steps

def konversi_heksadesimal_ke_biner(heksadesimal):
    """Konversi heksadesimal ke biner dengan langkah-langkah"""
    steps = []
    steps.append(f"Konversi Heksadesimal {heksadesimal} ke Biner:")
    
    # Langkah 1: Heksadesimal ke Desimal
    desimal = int(heksadesimal, 16)
    steps.append(f"1. Heksadesimal ke Desimal: {heksadesimal} = {desimal}")
    
    # Langkah 2: Desimal ke Biner
    steps.append("2. Desimal ke Biner:")
    n = desimal
    remainders = []
    
    while n > 0:
        remainder = n % 2
        steps.append(f"   {n} ÷ 2 = {n//2} sisa {remainder}")
        remainders.append(remainder)
        n = n // 2
    
    remainders.reverse()
    biner = ''.join(map(str, remainders))
    steps.append(f"   Membaca sisa terbalik: {biner}")
    return biner, steps

# [Tambahkan fungsi konversi lainnya dengan pola yang sama...]

while True:
    print("\n" + "="*40)
    print("Pilih Basis Bilangan:")
    print("1. Biner      3. Oktal")
    print("2. Desimal    4. Heksadesimal")
    basis_awal = input("Masukkan pilihan (1-4): ")

    print("\nKonversi Ke:")
    print("1. Biner      3. Oktal")
    print("2. Desimal    4. Heksadesimal")
    basis_akhir = input("Masukkan pilihan (1-4): ")

    bilangan = input("\nMasukkan bilangan: ").upper()

    try:
        if basis_awal == basis_akhir:
            hasil = bilangan
            steps = [f"Tidak perlu konversi: {bilangan} tetap {bilangan}"]
        else:
            if basis_awal == '1':    # Biner
                if basis_akhir == '2':
                    hasil, steps = konversi_biner_ke_desimal(bilangan)
                elif basis_akhir == '3':
                    # Konversi melalui desimal
                    temp, steps1 = konversi_biner_ke_desimal(bilangan)
                    hasil, steps2 = konversi_desimal_ke_oktal(temp)
                    steps = steps1 + steps2
                elif basis_akhir == '4':
                    temp, steps1 = konversi_biner_ke_desimal(bilangan)
                    hasil, steps2 = konversi_desimal_ke_heksadesimal(temp)
                    steps = steps1 + steps2
            
            elif basis_awal == '2':  # Desimal
                if basis_akhir == '1':
                    hasil, steps = konversi_desimal_ke_biner(bilangan)
                elif basis_akhir == '3':
                    hasil, steps = konversi_desimal_ke_oktal(bilangan)
                elif basis_akhir == '4':
                    hasil, steps = konversi_desimal_ke_heksadesimal(bilangan)
            
            elif basis_awal == '3':  # Oktal
                if basis_akhir == '1':
                    temp, steps1 = konversi_oktal_ke_desimal(bilangan)
                    hasil, steps2 = konversi_desimal_ke_biner(temp)
                    steps = steps1 + steps2
                elif basis_akhir == '2':
                    hasil, steps = konversi_oktal_ke_desimal(bilangan)
                elif basis_akhir == '4':
                    temp, steps1 = konversi_oktal_ke_desimal(bilangan)
                    hasil, steps2 = konversi_desimal_ke_heksadesimal(temp)
                    steps = steps1 + steps2
            
            elif basis_awal == '4':  # Heksadesimal
                if basis_akhir == '1':
                    hasil, steps = konversi_heksadesimal_ke_biner(bilangan)
                elif basis_akhir == '2':
                    hasil, steps = konversi_heksadesimal_ke_desimal(bilangan)
                elif basis_akhir == '3':
                    temp, steps1 = konversi_heksadesimal_ke_desimal(bilangan)
                    hasil, steps2 = konversi_desimal_ke_oktal(temp)
                    steps = steps1 + steps2

        print("\n" + "="*40)
        print(f"Hasil konversi: {hasil}")
        print("\nProses Konversi:")
        for langkah in steps:
            print(f"• {langkah}")

    except ValueError:
        print("Input tidak valid!")

    ulangi = input("\nUlangi konversi? (y/n): ").lower()
    if ulangi != 'y':
        break
