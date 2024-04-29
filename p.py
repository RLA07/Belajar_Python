input_string = input("Masukkan string: ")
n = len(input_string)
for i in range(n, 0, -1):
    print(input_string[:i])