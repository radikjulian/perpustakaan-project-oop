from enum import Enum


class StatusBuku(Enum):
    TERSEDIA = "tersedia"
    DIPINJAM = "dipinjam"

class StatusPeminjaman(Enum):
    AKTIF = "aktif"
    SELESAI = "selesai"