# 1. Buat variabel nilai dan kehadiran
nilai = 82
kehadiran = 90

# 2. Periksa masing-masing syarat dengan operator >=
syarat_nilai = nilai >= 75          # True, karena 82 >= 75
syarat_kehadiran = kehadiran >= 80  # True, karena 90 >= 80

# 3. Tentukan kelulusan dengan operator and
lulus_and_awal = syarat_nilai and syarat_kehadiran

print("--- Hasil Data Awal (Nilai=82, Kehadiran=90) ---")
print(f"Syarat Nilai (>= 75)     : {syarat_nilai}")
print(f"Syarat Kehadiran (>= 80) : {syarat_kehadiran}")
print(f"Status Kelulusan (AND)   : {lulus_and_awal}\n")

# 4. Ubah nilai menjadi 70
nilai = 70

# Periksa kembali syarat-syaratnya
syarat_nilai = nilai >= 75          # False, karena 70 tidak >= 75
syarat_kehadiran = kehadiran >= 80  # True, karena 90 >= 80

# Jalankan kembali dengan operator and
lulus_and_baru = syarat_nilai and syarat_kehadiran

# 5. Coba gunakan operator or
lulus_or_baru = syarat_nilai or syarat_kehadiran

print("--- Hasil Setelah Nilai Diubah menjadi 70 ---")
print(f"Syarat Nilai (>= 75)     : {syarat_nilai}")
print(f"Syarat Kehadiran (>= 80) : {syarat_kehadiran}")
print(f"Status Kelulusan (AND)   : {lulus_and_baru}")
print(f"Status Kelulusan (OR)    : {lulus_or_baru}")
