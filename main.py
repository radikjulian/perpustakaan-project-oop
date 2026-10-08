from library import Library
from library_presenter import LibraryPresenter
from book import Book

lib = Library()
presenter = LibraryPresenter(lib)

daftar_buku = lib.get_daftar_buku
daftar_buku.append("asdsadsa")
print(daftar_buku)

# buku1 = lib.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer")
# buku2 = lib.tambah_buku("Laskar Pelangi", "Andrea Hirata")
# buku3 = lib.tambah_buku("Clean Code", "Robert C. Martin")

# radik = lib.tambah_member("Radik")
# julian = lib.tambah_member("Julian")

# lib.pinjam_buku(radik, Book("asxasdas", "penulis"))


# presenter.tampilkan_buku()
# presenter.tampilkan_member()
# presenter.tampilkan_riwayat()