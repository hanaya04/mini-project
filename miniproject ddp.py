Nama = input("Masukkan Nama Anda: ")
NIM = input("Masukkan NIM Anda: ")

print("--------------------------------")

def hitung_gaji():
    jam_kerja = float(input("Masukkan jumlah jam kerja: "))
    tarif_kerja = float(input("Masukkan tarif per jam: "))

    # Menghitung Gaji Kerja
    total_gaji = jam_kerja * tarif_kerja

    # Memeriksa apakah jam kerja lebih dari 160
    if jam_kerja > 160:
        bonus = 0.1 * total_gaji
        total_gaji += bonus
        print("Anda mendapat bonus sebesar 10%: {bonus}")
    else:
        print("Anda tidak memiliki bonus.")

    print(f"Gaji total Anda adalah: {total_gaji}")

while True:
    hitung_gaji()
    ulangi = input("Apakah Anda ingin menghitung gaji lagi? (yes/no): ").lower()
    if ulangi != 'yes':
        break
print("Terima Kasih")
