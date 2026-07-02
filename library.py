from book import Book
from member import Member
from status import StatusPeminjaman, StatusBuku
from loan import Loan

class Library:
    def __init__(self):
        self.daftar_buku = []
        self.daftar_member = []
        self.riwayat_peminjaman = []

    def tambah_buku(self, judul:str , penulis:str):
        buku = Book(judul, penulis)
        self.daftar_buku.append(buku)
        return buku
    
    def tambah_member(self, nama:str):
        member = Member(nama)
        self.daftar_member.append(member)
        return member
    
    def pinjam_buku(self,member:Member, book: Book,):
        if not book.is_tersedia() :
            raise ValueError(f"Buku '{book.judul}'sedang dipinjam, tidak bisa dipinjam member lain")
        
        book.status = StatusBuku.DIPINJAM
        member.buku_dipinjam.append(book)

        loan = Loan(member, book)
        self.riwayat_peminjaman.append(loan)

    def kembalikan_buku(self, member:Member, book:Book):
        if book.is_tersedia():
            raise ValueError(f"Buku '{book.judul}'sedang tidak dipinjam, tidak bisa dikembalikan")
        
        loan_aktif = next(
            (l for l in self.riwayat_peminjaman
            if l.book == book and l.member == member and l.status == StatusPeminjaman.AKTIF),
                None
        )

        if loan_aktif is None:
            raise ValueError(f"Tidak ditemukan peminjaman aktif untuk '{member.nama}' - '{book.judul}'.")
        
        book.status = StatusBuku.TERSEDIA
        if book in member.buku_dipinjam: member.buku_dipinjam.remove(book)
        loan_aktif.selesaikan()
        return loan_aktif
    
    def cek_ketersediaan(self, book: Book) -> str:
        return "Tersedia" if book.is_tersedia() else "Sedang dipinjam"
    
    def tampilkan_buku(self):
        print("=== Daftar Buku ===")
        for b in self.daftar_buku:
            print(b)

    def tampilkan_member(self):
        print("=== Daftar Member ===")
        for m in self.daftar_member:
            print(m)

    def tampilkan_riwayat(self):
        print("=== Riwayat Peminjaman ===")
        for l in self.riwayat_peminjaman:
            print(l)