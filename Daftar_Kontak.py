import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan daftar kontak
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("======================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

# Fungsi untuk menambah kontak
def new_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon: ")
    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }
    return kontak

# Fungsi untuk menghapus kontak
def hapus_kontak(daftar_kontak):
    telepon = input("Nomor telepon yang akan dihapus: ")

    index = -1
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break

    if index == -1:
        print("Data kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data")

# Fungsi untuk mencari kontak
def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama yang dicari: ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yang_dicari.lower()) != -1:
            print("======================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")

# Fungsi untuk menampilkan kontak
def display_kontak_gui():
    output_text.delete(1.0, tk.END) 
    for kontak in daftar_kontak:
        output_text.insert(tk.END, f"Nama : {kontak['nama']}\n")
        output_text.insert(tk.END, f"Email : {kontak['email']}\n")
        output_text.insert(tk.END, f"Telepon : {kontak['telepon']}\n")
        output_text.insert(tk.END, "=" * 30 + "\n")

# Fungsi untuk menambah kontak
def tambah_kontak_gui():
    def submit_form():
        nama = entry_nama.get()
        email = entry_email.get()
        telepon = entry_telepon.get()
        kontak = {
            "nama": nama,
            "email": email,
            "telepon": telepon
        }
        daftar_kontak.append(kontak)
        messagebox.showinfo("Info", "Kontak berhasil ditambah")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Tambah Kontak")

    tk.Label(top, text="Nama").pack()
    entry_nama = tk.Entry(top)
    entry_nama.pack()

    tk.Label(top, text="Email").pack()
    entry_email = tk.Entry(top)
    entry_email.pack()

    tk.Label(top, text="Telepon").pack()
    entry_telepon = tk.Entry(top)
    entry_telepon.pack()

    tk.Button(top, text="Submit", command=submit_form).pack()

# Fungsi untuk menghapus kontak
def hapus_kontak_gui():
    def submit_delete():
        telepon = entry_telepon_delete.get()
        index = -1
        for i in range(len(daftar_kontak)):
            if daftar_kontak[i]["telepon"] == telepon:
                index = i
                break
        if index == -1:
            messagebox.showerror("Error", "Kontak tidak ditemukan")
        else:
            del daftar_kontak[index]
            messagebox.showinfo("Info", "Kontak berhasil dihapus")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Hapus Kontak")

    tk.Label(top, text="Nomor Telepon yang akan dihapus").pack()
    entry_telepon_delete = tk.Entry(top)
    entry_telepon_delete.pack()

    tk.Button(top, text="Hapus", command=submit_delete).pack()

# Fungsi untuk mencari kontak 
def cari_kontak_gui():
    def submit_search():
        nama_yang_dicari = entry_nama_search.get()
        result_text.delete(1.0, tk.END) 
        found = False
        for kontak in daftar_kontak:
            if nama_yang_dicari.lower() in kontak["nama"].lower():
                result_text.insert(tk.END, f"Nama : {kontak['nama']}\n")
                result_text.insert(tk.END, f"Email : {kontak['email']}\n")
                result_text.insert(tk.END, f"Telepon : {kontak['telepon']}\n")
                result_text.insert(tk.END, "=" * 30 + "\n")
                found = True
        if not found:
            result_text.insert(tk.END, "Kontak tidak ditemukan")

    top = tk.Toplevel(root)
    top.title("Cari Kontak")

    tk.Label(top, text="Nama yang dicari").pack()
    entry_nama_search = tk.Entry(top)
    entry_nama_search.pack()

    tk.Button(top, text="Cari", command=submit_search).pack()

# Untuk menyimpan kontak
daftar_kontak = []

# Membuat aplikasi
root = tk.Tk()
root.title("Aplikasi Daftar Kontak")

# Menampilkan Daftar Kontak
tk.Button(root, text="Tampilkan Daftar Kontak", command=display_kontak_gui).pack()

# Menambah Kontak
tk.Button(root, text="Tambah Kontak", command=tambah_kontak_gui).pack()

# Menghapus Kontak
tk.Button(root, text="Hapus Kontak", command=hapus_kontak_gui).pack()

# Mencari Kontak
tk.Button(root, text="Cari Kontak", command=cari_kontak_gui).pack()

# Untuk output
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Untuk hasil pencarian
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Menjalankan aplikasi
root.mainloop()