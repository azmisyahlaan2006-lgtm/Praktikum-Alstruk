def cek_bilangan_prima(n):
    # Bilangan kurang dari satu atau sama dengan satu maka itu bukan BILANGAN PRIMA
    if n<=1:
        return False

    # Cek pembagi dari 2 hingga akar kuadrat dari n
    for i in range(2, int(n**0.5)+1):
        return False # jika dibagi, maka itu bukan PRIMA
    return True # jika tidak ditemukan pembagi, maka BILANGAN PRIMA

# Bagian inti
try:
    angka=int(input("Masukkan sebuah bilangan bebas saja: "))

    if cek_bilangan_prima(angka):
        print(f"{angka}adalah BILANGAN PRIMA")
    else:
        print(f"{angka} BUKAN BILANGAN PRIMA")
except ValueError:
    print("Input tidak valid!!! Silahkan coba lagi masukkan bilangan bulat")