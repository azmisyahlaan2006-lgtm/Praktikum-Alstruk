# Nama Toko: Toko Koko Miiww

#Buat variabel harga dan jumlah
harga = 12500
jumlah = 4

#Hitung total harga (menggunakan operator perkalian *)
total_harga = harga * jumlah

#Hitung sisa pembagian total harga dengan 2.000 menggunakan operator %
sisa_pembagian = total_harga % 2000

#Hitung harga setelah diskon Rp5.000 (menggunakan operator pengurangan -)
harga_setelah_diskon = total_harga - 5000

#Tampilan hasil dari setiap perhitungan dengan label yang jelas
print("========================================")
print("           TOKO KOKO MIIWW              ")
print("========================================")
print(f"Harga per buku       : Rp {harga:,}")
print(f"Jumlah buku dibeli   : {jumlah} buah")
print("----------------------------------------")
print(f"Total Harga          : Rp {total_harga:,}")
print(f"Sisa Pembagian % 2000: Rp {sisa_pembagian:,}")
print(f"Harga Setelah Diskon : Rp {harga_setelah_diskon:,}")
print("========================================")
