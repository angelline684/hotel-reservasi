class Tamu:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp  # lewat setter, jadi otomatis divalidasi

    @property
    def no_hp(self):
        return self._no_hp

    @no_hp.setter
    def no_hp(self, nilai):
        if not Tamu.valid_no_hp(nilai):
            raise ValueError("Nomor HP tidak valid (10-13 digit angka).")
        self._no_hp = nilai

    @staticmethod
    def valid_no_hp(nilai):
        return nilai.isdigit() and 10 <= len(nilai) <= 13

    def __str__(self):
        return f"{self.nama} ({self._no_hp})"
