Daftar_Buku = [
    "seni hidup bahgia",
    "hujan",
    "aku kamu dan waktu di kala itu",
    "tentang kamu",
    "aku kalah aku merindukannmu",
    "untuk satu nama yang sulit ku hapus",
]

pinjaman = []

print ("JUDUL BUKU DI FAKULTAS TEKNIK UNMUL",)

for i in Daftar_Buku:
    print("-", i )

while True:
    print("--menu--")
    print("1. pinjam buku")
    print("2. hapus buku yang di pinjam")
    print("3. selesai")

    pilihan_buku = input("pilih menu (1/2/3): ")

    if pilihan_buku == "1":
        judul = input("masukkan judul buku yang imgin di pinjam: ")

        if judul in Daftar_Buku:
            pinjaman.append(judul)
            print("buku berhasil di pinjam")
        else:
            print("judul buku yang di masukkan tidak tersedia")

    elif pilihan_buku == "2":
        if pinjaman == []:
            print("belum ada buku yang anda pinjam")
        else:
            judul = input("masukkan judul buku yang ingin di hapus: ")    
            if judul in pinjaman:
                pinjaman.remove(judul)
                print("berhasil di hapus dari daftar pinjaman", pinjaman)
            else:
                print("judul buku tidak di temukan dalam daftar pinjaman!!")

    elif pilihan_buku == "3":
        break

    else:
        print("error!! pilihan menu tidak tersedia")


print("DAFTAR BUKU YANG DI PINJAM")
if pinjaman == []:
    print("tidak  ada buku yang di pinjam")
else:
    for i in pinjaman:
        print("-", i)


