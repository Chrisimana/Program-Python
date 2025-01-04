def kalimat_vokal(kalimat):
    vokal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    kalimat = kalimat[::-1]
    vokal = sum(1 for huruf in kalimat if huruf in vokal)
    return kalimat, vokal
kalimat = input("Masukkan kalimat: ")
kalimat, vokal = kalimat_vokal(kalimat)
print("Kalimat terbalik: ", kalimat)
print("Jumlah huruf vokal: ", vokal)