from itertools import count
from status import StatusBuku


class Book:
    _id_counter = count(1)

    def __init__(self, judul: str, penulis: str):
        self.id = next(Book._id_counter)
        self.judul = judul
        self.penulis = penulis
        self.status = StatusBuku.TERSEDIA

    def is_tersedia(self) -> bool:
        return self.status == StatusBuku.TERSEDIA
    
    def __str__(self):
        return f"[{self.id}] {self.judul} - {self.penulis} ({self.status.value})"