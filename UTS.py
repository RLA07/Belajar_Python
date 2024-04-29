def convertermatauang():
    print("Pilih jenis mata uang yang akan ditukar: ")
    print("1. Rupiah ke USD")
    print("2. Rupiah ke JPY")
    print("3. Rupiah ke EUR")
    print("Pilihan: ", end='', flush=True)
    jenis = int(input())
    if jenis == 1:
        uSD()
    else:
        if jenis == 2:
            jPY()
        else:
            if jenis == 3:
                eUR()
            else:
                print("Tolong pilih konversi yang benar (1, 2, atau 3)")
                convertermatauang()

def eUR():
    eUR = 15865
    print("Masukkan jumlah uang yang akan ditukar (rupiah): ", end='', flush=True)
    asal = float(input())
    hasil = asal / eUR
    print(hasil)

def jPY():
    jPY = 129.9
    print("Masukkan jumlah uang yang akan ditukar (rupiah): ")
    asal = float(input())
    hasil = asal / jPY
    print(hasil)

def uSD():
    uSD = 9840
    print("Masukkan jumlah uang yang akan ditukar (rupiah): ")
    asal = float(input())
    hasil = asal / uSD
    print(hasil)

# Main
convertermatauang()
print("Terima Kasih")
