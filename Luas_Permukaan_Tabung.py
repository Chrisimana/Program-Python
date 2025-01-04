import math

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari tabung (dalam satuan cm): "))
tinggi = float(input("Masukkan tinggi tabung (dalam satuan cm): "))

# Menghitung luas permukaan tabung
# Luas permukaan tabung = 2 * π * r * (r + t)
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Menampilkan hasil
print(f"Luas permukaan tabung adalah: {luas_permukaan:.2f} cm²")
