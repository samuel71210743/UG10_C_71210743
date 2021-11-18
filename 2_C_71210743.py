phi = 3.14

switcher = {
    1: "Limas",
    2: "Bola",
    3: "Kerucut",
}

# print("")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~\n"
      " Kalkulator Volume Bangun Ruang\n"
      " ~~~~~~~~~~~~~~~~~~~~~~~~ \n"
      " Pilih bangun ruang yang ingin dihitung volumenya: \n"
        "1. Limas\n"
        "2. Bola\n"
        "3. Kerucut"
)

pilihan = int(input("Masukkan pilihan anda:"))
# print(" ", pilihan)

if switcher.get(pilihan) == "Limas" :
    panjang_sisi = int(input("Masukkan panjang sisi alas limas: "))
    tinggi = int(input("Masukkan tinggi limas: "))
    volume_limas = 1/3 * (panjang_sisi*panjang_sisi) * tinggi
    print("Volume limas tersebut adalah ", volume_limas)
elif switcher.get(pilihan) == "Bola" : 
    jari_jari = int(input("Masukkan panjang jari-jari bola: "))
    volume_bola = 4/3 * (phi * ((jari_jari)**3))
    print("Volume bola tersebut adalah ", volume_bola)
elif switcher.get(pilihan) == "Kerucut" :
    jari_jari = int(input("Masukkan jari-jari kerucut: "))
    tinggi = int(input("Masukkan tinggi kerucut: "))
    volume_kerucut = 1/3 * (phi * ((jari_jari)**2)) * tinggi
    print("Volume kerucut tersebut adalah ", volume_kerucut)
else : 
    print("Pilihan anda tidak tersedia di menu kalkulator ini")
