from library import Library

class LibraryPresenter:
    def __init__(self, library:Library):
        self.library = library

    def tampilkan_buku(self):
        print("=== Daftar Buku ===")
        for b in self.library.get_daftar_buku():
            print(b)

    def tampilkan_member(self):
        print("=== Daftar Member ===")
        for m in self.library.get_daftar_member():
            print(m)

    def tampilkan_riwayat(self):
        print("=== Riwayat Peminjaman ===")
        for l in self.library.get_riwayat_peminjaman():
            print(l)