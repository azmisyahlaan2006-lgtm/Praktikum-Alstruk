# Inisialisasi struktur data dari soal
nilai = [78, 85, 90, 85]
mahasiswa = {"nama": "Nadia", "kelas": "IF-A"}
koordinat = (5, 8)
angka = {2, 4, 4, 6, 8}

# 1. Tampilkan nilai pertama dari list
print(f"1. Nilai pertama dari list: {nilai[0]}")

# 2. Tambahkan nilai 95 ke list dan tampilkan list terbaru
nilai.append(95)
print(f"2. List terbaru setelah ditambah 95: {nilai}")

# 3. Tampilkan nama mahasiswa dari dictionary
print(f"3. Nama mahasiswa: {mahasiswa['nama']}")

# 4. Tampilkan koordinat pertama dari tuple
print(f"4. Koordinat pertama dari tuple: {koordinat[0]}")

# 5. Tampilkan angka unik dengan sorted(angka)
print(f"5. Angka unik (sorted): {sorted(angka)}")
