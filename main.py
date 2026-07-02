from library import Library

lib = Library()

buku1 = lib.tambah_buku("Laskar Pelangi", "Andrea Hirata")
buku2 = lib.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer")
buku3 = lib.tambah_buku("Clean Code", "Robert C. Martin")

radik = lib.tambah_member("Radik")
julian = lib.tambah_member("Julian")

lib.tampilkan_buku()
lib.tampilkan_member()

lib.pinjam_buku(radik, buku1)
lib.pinjam_buku(radik, buku3) 
print(lib.cek_ketersediaan(buku1)) 

# try:
#     lib.pinjam_buku(julian, buku1)
# except ValueError as e:
#     print("Error (expected):", e)


lib.pinjam_buku(julian, buku2)

lib.tampilkan_member()

lib.kembalikan_buku(radik, buku1)
print(lib.cek_ketersediaan(buku1))

lib.tampilkan_member()

try:
    lib.kembalikan_buku(julian, buku1)
except ValueError as e:
    print("Error (expected):", e)

lib.tampilkan_riwayat()

print(buku1)