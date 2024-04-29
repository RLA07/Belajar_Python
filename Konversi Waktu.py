# Konversi waktu dari jam dan menit ke detik
def konversi_ke_detik(jam, menit):
    detik = (jam * 3600) + (menit * 60)
    return detik

# Konversi hari dari tahun dan bulan
def konversi_ke_hari(tahun, bulan):
    # Saya bulatkan 1 bulan = 30 hari
    # dan 1 tahun = 360 hari
    hari = (tahun * 360) + (bulan * 30)
    return hari

# Pilih Konversi
print("Silahkan pilih jenis konversi")
print("1. Tahun dan Bulan ke Hari")
print("2. Jam dan Menit ke Detik")

# Cek hasil pilih
konversi = input("Masukan nomor yang diinginkan: ")
# Percabangan
if konversi == '1':
    # Input untuk konversi waktu
    jam = int(input("Masukkan jam: "))
    menit = int(input("Masukkan menit: "))
    detik = konversi_ke_detik(jam, menit)
    print(f"{jam} jam {menit} menit adalah {detik} detik.")
elif konversi == "2":
    # Input untuk konversi hari
    tahun = int(input("Masukkan tahun: "))
    bulan = int(input("Masukkan bulan (1-12): "))
    hari = konversi_ke_hari(tahun, bulan)
    print(f"{tahun} tahun {bulan} bulan adalah sekitar {hari} hari.")
else:
    print('Maaf tidak ada pilihan')
# Melakukan konversi dan menampilkan hasil




