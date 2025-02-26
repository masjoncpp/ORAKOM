def konversi_bilangan()
  print("Pilih Menu Konversi :")
  print("1.Desimal Ke Oktal")
  print("2.Desimal Ke Hexadesimal")
  print("3.Oktal Ke Desimal")
  print("4. Hexadesimal ke Desimal")

pilihan=input("Pilih Program(1/2/3/4) : ")
  if pilihan =='1':
    desimal = int(input("Masukkan bilangan desimal : ")
    oktal = oct(desimal)[2:]
    print(f"Bilangan Oktal:{oktal}")

  elif pilihan == '2':
      desimal=int(input("Masukkan Bilangan Desimal : ")
      hexadesimal=hex(desimal)[2:]
    print(f"Bilangan Hexadesimal{hexadesimal}")

elif pilihan == '3':
    oktal=input("Masukkan bilangan Oktal :")
    desimal=int(oktal,8)
print(f"Bilangan Desimal{desimal}")

elif pilihan == '4'
      hexadesimal=input("Masukkan bilangan Hexadesimal")
      desimal = int(hexadesimal,16)
print(f"Bilangan Desimal : {desimal}")

else : 
  print("Input Tidak Ada!")

konversi_bilangan()
