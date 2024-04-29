def hitung(bil1, bil2, operator):
    if operator == "*":
        hasil = bil1 * bil2
        print(hasil)
    else:
        if operator == "/":
            hasil = float(bil1) / bil2
            print(hasil)
        else:
            if operator == "+":
                hasil = bil1 + bil2
                print(hasil)
            else:
                if operator == "-":
                    hasil = bil1 - bil2
                    print(hasil)
                else:
                    if operator == "%":
                        hasil = bil1 % bil2
                        print(hasil)
                    else:
                        hitung(operator)

# Main
print("Masukkan bilangan 1: ")
bil1 = int(input())
print("Masukkan bilangan 2: ")
bil2 = int(input())
print("Masukkan opertaor (+, -, *, /, %): ")
operator = input()
hitung(bil1, bil2, operator)
