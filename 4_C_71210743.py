bilangan1 = int(input("Masukkan bilangan 1: "))
bilangan2 = int(input("Masukkan bilangan 2: "))
bilangan3 = int(input("Masukkan bilangan 3: "))


if ((bilangan1 > bilangan2) and (bilangan1 > bilangan3)) and (bilangan2 > bilangan3) :
    print("Bilangan terbesar adalah", bilangan1)
    print("Bilangan terkecil adalah", bilangan3)
elif((bilangan2 > bilangan1) and (bilangan2 > bilangan3)) and (bilangan1 > bilangan3) :
    print("Bilangan terbesar adalah", bilangan2)
    print("Bilangan terkecil adalah", bilangan3)
elif((bilangan3 > bilangan1) and (bilangan3 > bilangan2)) and (bilangan2 > bilangan1) :
    print("Bilangan terbesar adalah", bilangan3)
    print("Bilangan terkecil adalah", bilangan1)
elif((bilangan3 > bilangan1) and (bilangan3 > bilangan2)) and (bilangan1 > bilangan2) :
    print("Bilangan terbesar adalah", bilangan3)
    print("Bilangan terkecil adalah", bilangan2)
elif((bilangan1 > bilangan2) and (bilangan1 > bilangan3)) and (bilangan3 > bilangan2) :
    print("Bilangan terbesar adalah", bilangan1)
    print("Bilangan terkecil adalah", bilangan2)
elif((bilangan2 > bilangan1) and (bilangan2 > bilangan3)) and (bilangan3 > bilangan1) :
    print("Bilangan terbesar adalah", bilangan2)
    print("Bilangan terkecil adalah", bilangan1)
elif(bilangan1 > bilangan2 > bilangan3) and (bilangan2 == bilangan3) :
    print("Bilangan terbesar adalah", bilangan1)
    print("Bilangan terkecil adalah", bilangan2)
elif(bilangan2 > bilangan3 > bilangan1) and (bilangan3 == bilangan1) :
    print("Bilangan terbesar adalah", bilangan2)
    print("Bilangan terkecil adalah", bilangan3)
elif(bilangan3 > bilangan1 > bilangan2) and (bilangan1 == bilangan2) :
    print("Bilangan terbesar adalah", bilangan3)
    print("Bilangan terkecil adalah", bilangan1)
elif(bilangan2 > bilangan1) and (bilangan1 == bilangan3):
    print("Bilangan terbesar adalah", bilangan2)
    print("Bilangan terkecil adalah", bilangan1)
elif(bilangan3 > bilangan1) and (bilangan1 == bilangan2):
    print("Bilangan terbesar adalah", bilangan3)
    print("Bilangan terkecil adalah", bilangan2)
elif(bilangan1 > bilangan2) and (bilangan2 == bilangan3):
    print("Bilangan terbesar adalah", bilangan1)
    print("Bilangan terkecil adalah", bilangan3)
