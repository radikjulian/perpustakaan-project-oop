from enum import Enum


class StatusBuku(Enum):
    TERSEDIA = "teresedia"
    DIPINJAM = "dipinjam"

class StatusPeminjaman(Enum):
    AKTIF = "aktif"
    SELESAI = "selesi"