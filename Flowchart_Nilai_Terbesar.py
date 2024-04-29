print("Masukkan bilangan pertama: ", end='', flush=True)
a = int(input())
print("Masukkan bilangan kedua: ", end='', flush=True)
b = int(input())
if a > b:
    terbesar = a
    print("Bilangan pertama adalah " + str(a) + "Bilangan kedua adalah " + str(b) + "Bilangan terbesar adalah " + str(terbesar))
else:
    if b > a:
        terbesar = b
        print("Bilangan terbesar adalah " + str(terbesar))
    else:
        print("Kedua bilangan sama besar")
