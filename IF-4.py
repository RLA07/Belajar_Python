total = int(input('Masukan umur anda: '))
if total < 5:
    print('Anda masih balita')
elif total >= 5 and total <= 11:
    print('Anda masih anak-anak')
elif total >= 12 and total <= 25:
    print('Anda sudah remaja')
elif total >= 26 and total <= 45:
    print('Anda sudah dewasa')
elif total >= 46 and total <= 65:
    print('Anda sudah lansia')
else:
    print('Anda sudah memasuki masa manula atas')
#data diatas diambil dari www.neliti.com
