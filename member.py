from itertools import count

class Member:
    _id_counter = count(1)

    def __init__(self, nama: str):
        self.id = next(Member._id_counter)
        self.nama = nama
        self.buku_dipinjam = []

    def __str__(self):
        judul_list = [b.judul for b in self.buku_dipinjam]
        return f"[{self.id}] {self.nama} - sedang pinjam: {judul_list or 'tidak ada'}"