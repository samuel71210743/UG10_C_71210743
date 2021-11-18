n = int(input("Masukkan angka: "))



if (n%5 == 0 or n%3 == 0) and (n%2 == 0 or n%4 == 0) :
    a = "YA"
    b = "TENTU"
    print("Apakah Bilangan habis dibagi 5 atau 3? Jawab: ", a)
    print("Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab: ", b)
elif (n%5 == 0 or n%3 == 0) and (n%2 != 0 and n%4 !=0) : 
    a = "YA"
    b = "TIDAK"
    print("Apakah Bilangan habis dibagi 5 atau 3? Jawab: ", a)
    print("Apakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab: ", b)
else : 
    print("Bilangan tersebut tidak habis dibagi 5 atau 3. Program dihentikan")




