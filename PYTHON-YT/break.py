#BREAK

angka = 0

while angka < 5:
    angka +=1
    print(f"count -> {angka}")

    if angka == 3:
        print("lets goooo")
        break

    print("heloo lil guy")

print("finishh")


data_int = int(input(f"hitung sampe brp bos? "))
angka = 0

while True:
    angka +=1
    print(f"count -> {angka}")

    if angka == data_int:
        print("lets goooo")
        break

    print("heloo lil guy")

print("finishh")