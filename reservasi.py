from datetime import date, timedelta

from kamar import Kamar


class Reservasi:
    _counter = 0  # class attribute untuk membuat ID otomatis

    def __init__(self, tamu, kamar, check_in, malam):
        if malam < 1:
            raise ValueError("Jumlah malam minimal 1.")
        Reservasi._counter += 1
        self.id = f"RSV{Reservasi._counter:03d}"
        self.tamu = tamu
        self.kamar = kamar
        self.check_in = check_in
        self.malam = malam
        self.status = "Aktif"

    @property
    def check_out(self):
        return self.check_in + timedelta(days=self.malam)

    @property
    def total_biaya(self):
        return self.kamar.hitung_harga(self.malam)  # polymorphism

    @classmethod
    def dari_string_tanggal(cls, tamu, kamar, tanggal_str, malam):
        """Membuat reservasi dari tanggal berformat YYYY-MM-DD."""
        tahun, bulan, hari = map(int, tanggal_str.split("-"))
        return cls(tamu, kamar, date(tahun, bulan, hari), malam)

    def batalkan(self):
        if self.status != "Aktif":
            raise ValueError("Reservasi ini sudah tidak aktif.")
        self.status = "Dibatalkan"
        self.kamar.kosongkan()

    def selesai(self):
        self.status = "Selesai"
        self.kamar.kosongkan()

    def __str__(self):
        return (
            f"[{self.id}] {self.tamu.nama} | Kamar {self.kamar.nomor} "
            f"({self.kamar.tipe}) | {self.check_in} s/d {self.check_out} "
            f"({self.malam} malam) | "
            f"{Kamar.format_rupiah(self.total_biaya)} | {self.status}"
        )
