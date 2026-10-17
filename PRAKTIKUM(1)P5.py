nama = "fajar"
umur = 19
berat = 54.5
terdaftar = True

print("Nama saya adalah", nama)
print("Umur saya ", umur, "tahun")
print("Berat saya adalah", berat, "kg")
print("Saya", "sudah" if terdaftar else "belum", "terdaftar")

print("\n---MENAMPILKAN TIPE DATA---")
print("Tipe data nama:", type(nama))
print("Tipe data umur:", type(umur))
print("Tipe data berat:", type(berat))
print("Tipe data terdaftar:", type(terdaftar))

print("\n---UMUR FAJAR YANG BARU---")
print("umur fajar yang baru adalah", umur + 1, "tahun")
umur = umur + 1
print("Umur saya sekarang adalah", umur, "tahun")
print("tipe data umur sekarang adalah", type(umur))

