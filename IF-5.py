print('Pilih jenis kelamin (Pria/Wanita)')
jenis_kelamin = str(input('Masukkan jenis kelamin: '))
umur = int(input('Masukkan umur anda: '))
if (jenis_kelamin == 'pria'):
    if (umur >= 25):
        print('Anda boleh menikah')
    else:
        print('Anda tidak boleh menikah')
elif (jenis_kelamin == 'wanita'):
    if (umur >= 20):
        print('Anda boleh menikah')
    else:
        print('Anda tidak boleh menikah')
else:
    print('Masukkan jenis kelamin yang benar')
