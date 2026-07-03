from itertools import count
from member import Member
from book import Book
from status import StatusPeminjaman
from datetime import datetime


class Loan:
    _id_counter = count(1)

    def __init__(self, member: Member, book:Book):
         self.id = next(Loan._id_counter)
         self.member = member
         self.book = book
         self.status = StatusPeminjaman.AKTIF
         self.tanggal_pinjam = datetime.now()
         self.tanggal_kembali = None

    def selesaikan(self):
         self.status = StatusPeminjaman.SELESAI
         self.tanggal_kembali = datetime.now()

    def __str__(self):
         kembali = self.tanggal_kembali.strftime("%Y-%m-%d %H:%M") if self.tanggal_kembali else "-"
         return (f"Loan#{self.id} | {self.member.nama} -> {self.book.judul} "
                f"| status: {self.status.value} | pinjam: {self.tanggal_pinjam.strftime('%Y-%m-%d %H:%M')} "
                f"| kembali: {kembali}")