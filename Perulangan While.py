#Variabel data UKT Mahasiswa
ukt1="Rp. 500.000"
ukt2="Rp. 1.000.000"
ukt3="Rp. 1.500.000"
ukt4="Rp. 2.500.000"
ukt5="Rp. 4.000.000"
ukt6="Rp. 5.500.000"
ukt7="Rp. 6.500.000"
ukt8="Rp. 7.500.000"

#Definisi mencocokkan Level UKT dengan Jumlah UKT
def hitung_ukt():
    ukt=int(input("Level UKT (1-8): "))
    if ukt==1:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt1,"\n")
    elif ukt==2:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt2,"\n")
    elif ukt==3:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt3,"\n")
    elif ukt==4:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt4,"\n")
    elif ukt==5:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt5,"\n")
    elif ukt==6:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt6,"\n")
    elif ukt==7:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt7,"\n")
    elif ukt==8:
        print("\nNama anda:", nama, "\nNIM:", nim, "\nProgram Studi:", prodi, "\nJumlah UKT:", ukt8,"\n")
    else:
        print("Masukkan Level UKT yang sesuai!!!")
        hitung_ukt()
        
#Mulai Program
pilih='y'
while (pilih=='y' or pilih=='Y'):
    #Menginput data mahasiswa
    nama=input("Nama: ")
    nim=int(input("Masukkan NIM: "))
    prodi=input("Program studi: ")
    #Mencocokkan hasil UKT
    hitung_ukt()
    #mengulang proses input
    pilih=input("Tekan Y untuk mengulang atau tekan apapun untuk selesai: ")
    print ("\n")
