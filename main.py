from library import Library
from library_presenter import LibraryPresenter
from book import Book

lib = Library()
presenter = LibraryPresenter(lib)

buku1 = lib.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer")
buku2 = lib.tambah_buku("Laskar Pelangi", "Andrea Hirata")
buku3 = lib.tambah_buku("Clean Code", "Robert C. Martin")

radik = lib.tambah_member("Radik")
julian = lib.tambah_member("Julian")

# lib.pinjam_buku(radik, buku2)
lib.pinjam_buku(radik, Book("asxasdas", "penulis"))
# lib.pinjam_buku(julian, buku1) 
# print(lib.cek_ketersediaan(buku1)) 

# try:
#     lib.pinjam_buku(julian, buku1)
# except ValueError as e:
#     print("Error (expected):", e)


# lib.pinjam_buku(julian, buku2)

# lib.kembalikan_buku(radik, buku1)
# print(lib.cek_ketersediaan(buku1))


# try:
#     lib.kembalikan_buku(julian, buku1)
# except ValueError as e:
#     print("Error (expected):", e)


presenter.tampilkan_buku()
presenter.tampilkan_member()
presenter.tampilkan_riwayat()