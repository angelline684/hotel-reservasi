from abc import ABC, abstractmethod


class Kamar(ABC):
    """Class abstrak sebagai induk semua jenis kamar."""

    jumlah_kamar = 0  # class attribute

    def __init__(self, nomor, harga_dasar):
        self.nomor = nomor
        self._harga_dasar = harga_dasar  # encapsulation (protected)
        self._tersedia = True
        Kamar.jumlah_kamar += 1

    # ---------- Property ----------
    @property
    def harga_dasar(self):
        return self._harga_dasar

    @property
    def tersedia(self):
        return self._tersedia

    # ---------- Method biasa ----------
    def pesan(self):
        if not self._tersedia:
            raise ValueError(f"Kamar {self.nomor} sedang tidak tersedia.")
        self._tersedia = False

    def kosongkan(self):
        self._tersedia = True

    # ---------- Abstract method (wajib di-override) ----------
    @property
    @abstractmethod
    def tipe(self):
        pass

    @abstractmethod
    def hitung_harga(self, malam):
        """Menghitung total harga untuk sejumlah malam."""

    @abstractmethod
    def fasilitas(self):
        pass

    # ---------- Class method & static method ----------
    @classmethod
    def total_kamar(cls):
        return Kamar.jumlah_kamar

    @staticmethod
    def format_rupiah(angka):
        return "Rp{:,.0f}".format(angka).replace(",", ".")

    # ---------- Magic method ----------
    def __str__(self):
        status = "Tersedia" if self._tersedia else "Terisi"
        return (f"Kamar {self.nomor} [{self.tipe}] - "
                f"{Kamar.format_rupiah(self._harga_dasar)}/malam - {status}")


class KamarStandar(Kamar):  # inheritance
    @property
    def tipe(self):
        return "Standar"

    def hitung_harga(self, malam):  # polymorphism
        return self._harga_dasar * malam

    def fasilitas(self):
        return ["AC", "TV", "Wi-Fi"]


class KamarDeluxe(Kamar):
    @property
    def tipe(self):
        return "Deluxe"

    def hitung_harga(self, malam):
        total = self._harga_dasar * malam
        if malam >= 3:  # diskon 10% untuk menginap 3 malam atau lebih
            total *= 0.9
        return total

    def fasilitas(self):
        return ["AC", "TV", "Wi-Fi", "Kulkas mini", "Sarapan"]


class KamarSuite(Kamar):
    BIAYA_LAYANAN = 0.05  # 5%

    @property
    def tipe(self):
        return "Suite"

    def hitung_harga(self, malam):
        total = self._harga_dasar * malam
        return total + total * KamarSuite.BIAYA_LAYANAN

    def fasilitas(self):
        return ["AC", "Smart TV", "Wi-Fi", "Bathtub", "Sarapan", "Ruang tamu"]
