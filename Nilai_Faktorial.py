def faktorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka: "))
hasil = faktorial(angka)
print(f"{angka}! = ", end="")
for i in range(angka, 1, -1):
    print(f"{i} x ", end="")
print(f"1 = {hasil}")