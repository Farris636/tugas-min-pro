nama = input("masukkan nama anda: ")
if nama == "farris":
    print("hello farris")
else:
    print("nama anda salah")
nim = input("masukkan nim anda: ")
if nim == "079":
    print("nim anda benar")
else:
    print("nim anda salah")
print()
print("Nama: ",nama)
print("NIM: ",nim)

def operasi():
    jam_kerja = int(input("\nmasukkan jam kerja anda: "))
    tarif_kerja = int(input("masukkan tarif kerja/jam: "))
    gaji = jam_kerja * tarif_kerja
    print ("ini adalah gaji anda: ",gaji)
    if jam_kerja > 160:
        bonus = gaji * 0.10
        print("bonus anda sebesar: ",bonus)
    else:
        print("tidak ada bonus: ")

while True:
    operasi()
    ulang = input("\napakah anda ingin menghitung ulang gaji? (y/t)")
    if ulang == "t":
        break
print("terimakasih")