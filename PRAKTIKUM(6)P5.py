# Fungsi untuk merekap nilai mahasiswa
def rekap_nilai(nama, nilai_tugas, nilai_ujian):
    # 1. Simpan nama dalam variabel string (dari parameter)
    # 2. Simpan nilai dalam variabel numerik (dari parameter)
    
    # 3. Hitung rata-rata kedua nilai
    rata_rata = (nilai_tugas + nilai_ujian) / 2
    
    # 4. Memeriksa status kelulusan (minimal 75)
    status_lulus = rata_rata >= 75
    
    # 5. Tampilkan nama, kedua nilai, rata-rata, dan status lulus (True/False)
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {nilai_tugas}")
    print(f"Nilai Ujian    : {nilai_ujian}")
    print(f"Rata-rata      : {rata_rata}")
    print(f"Status Lulus   : {status_lulus}")
    print("-" * 30)

# 6. Uji program dengan dua kombinasi nilai yang berbeda
print("=== UJI COBA 1 ===")
rekap_nilai("Budi Santoso", 80, 70)

print("=== UJI COBA 2 ===")
rekap_nilai("Siti Aminah", 90, 85)

print("=== UJI COBA 3 (INPUT MANUAL) ===")
nama_baru = input("Ketik Nama Mahasiswa        : ")
tugas_baru = float(input("Ketik Nilai Tugas    : "))
ujian_baru = float(input("Ketik Nilai Ujian    : "))

# Memanggil fungsi menggunakan data baru
rekap_nilai(nama_baru, tugas_baru, ujian_baru)