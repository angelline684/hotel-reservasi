from kamar import KamarStandar, KamarDeluxe, KamarSuite
from reservasi import Reservasi


class Hotel:
    def __init__(self, nama):
        self.nama = nama
        self._daftar_kamar = []
        self._daftar_reservasi = []

    @classmethod
    def hotel_contoh(cls):
        """Membuat hotel dengan beberapa kamar bawaan."""
        hotel = cls("Hotel Nusantara")
        for nomor in (101, 102, 103):
            hotel.tambah_kamar(KamarStandar(nomor, 300_000))
        for nomor in (201, 202):
            hotel.tambah_kamar(KamarDeluxe(nomor, 500_000))
        hotel.tambah_kamar(KamarSuite(301, 1_000_000))
        return hotel

    def tambah_kamar(self, kamar):
        self._daftar_kamar.append(kamar)

    def semua_kamar(self):
        return list(self._daftar_kamar)

    def kamar_tersedia(self):
        return [k for k in self._daftar_kamar if k.tersedia]

    def cari_kamar(self, nomor):
        for kamar in self._daftar_kamar:
            if kamar.nomor == nomor:
                return kamar
        raise ValueError(f"Kamar {nomor} tidak ditemukan.")

    def buat_reservasi(self, tamu, nomor_kamar, tanggal_str, malam):
        kamar = self.cari_kamar(nomor_kamar)
        kamar.pesan()  # error jika kamar sudah terisi
        try:
            reservasi = Reservasi.dari_string_tanggal(tamu, kamar, tanggal_str, malam)
        except ValueError:
            kamar.kosongkan()  # batalkan pemesanan kamar jika data tidak valid
            raise
        self._daftar_reservasi.append(reservasi)
        return reservasi

    def cari_reservasi(self, id_reservasi):
        for r in self._daftar_reservasi:
            if r.id == id_reservasi.upper():
                return r
        raise ValueError(f"Reservasi {id_reservasi} tidak ditemukan.")

    def batalkan_reservasi(self, id_reservasi):
        self.cari_reservasi(id_reservasi).batalkan()

    def check_out(self, id_reservasi):
        self.cari_reservasi(id_reservasi).selesai()

    def semua_reservasi(self):
        return list(self._daftar_reservasi)
