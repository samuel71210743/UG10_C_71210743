nama = str(input("Masukan nama lengkap anda: "))
tinggi = int(input("Masukan tinggi badan anda: "))
berat_badan = int(input("Masukan berat badan anda: "))

BMI = (berat_badan / (tinggi/100)**2)

print("Hallo, ",nama) 
print("Indeks masa tubuh (BMI) Anda adalah ", BMI)

if BMI <= 18.5 : 
    print("Anda termasuk kedalam kategori kekurangan berat badan!")
elif BMI > 18.5 and BMI <= 25: 
    print("Anda termasuk ke dalam kategori berat badan ideal! ")
elif BMI < 25 and BMI <= 30 : 
    print("Anda termasuk ke dalam kategori kelebihan berat badan!")
else : 
    print("Anda termasuk ke dalam kategori obesitas!")
