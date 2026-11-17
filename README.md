# Sistem Reservasi Hotel (OOP Python)

Project sederhana berbasis terminal untuk mengelola reservasi hotel, dibuat untuk memenuhi UTS Pemrograman Berorientasi Objek.

Nama: Angeline Balqis Indarto
NIM:  14012500117

## Fitur

- Melihat semua kamar dan kamar yang tersedia
- Membuat reservasi (nama, no. HP, tanggal check-in, jumlah malam)
- Menghitung total biaya otomatis sesuai tipe kamar
- Membatalkan reservasi
- Check-out

## Struktur Project

```
hotel-reservasi/
├── main.py         # program utama (menu)
├── hotel.py        # class Hotel
├── kamar.py        # class Kamar (abstrak), KamarStandar, KamarDeluxe, KamarSuite
├── tamu.py         # class Tamu
├── reservasi.py    # class Reservasi
└── README.md
```

## Konsep OOP yang Digunakan

| Konsep | Penerapan |
|---|---|
| Class & Object | `Hotel`, `Kamar`, `Tamu`, `Reservasi` |
| Constructor | `__init__` di setiap class |
| Atribut | Atribut instance dan class attribute (`Kamar.jumlah_kamar`) |
| Encapsulation | Atribut `_tersedia`, `_harga_dasar`, `_no_hp` |
| Property (getter/setter) | `Kamar.tersedia`, `Tamu.no_hp` (dengan validasi) |
| Inheritance | `KamarStandar`, `KamarDeluxe`, `KamarSuite` mewarisi `Kamar` |
| Abstract Class | `Kamar` memakai `ABC` dan `@abstractmethod` |
| Polymorphism | `hitung_harga()` berbeda di tiap tipe kamar |
| Class method | `Kamar.total_kamar()`, `Hotel.hotel_contoh()`, `Reservasi.dari_string_tanggal()` |
| Static method | `Kamar.format_rupiah()`, `Tamu.valid_no_hp()` |
| Magic method | `__str__` |
| Exception handling | `ValueError` untuk input/kondisi tidak valid |

## Aturan Harga

| Tipe | Harga/malam | Aturan |
|---|---|---|
| Standar | Rp300.000 | Harga normal |
| Deluxe | Rp500.000 | Diskon 10% jika menginap 3 malam atau lebih |
| Suite | Rp1.000.000 | Biaya layanan 5% |

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
python main.py
```

## Contoh Penggunaan

```
Nama tamu            : Budi
No. HP               : 081234567890
Nomor kamar          : 201
Check-in (YYYY-MM-DD): 2026-12-01
Jumlah malam         : 3

Reservasi berhasil!
[RSV001] Budi | Kamar 201 (Deluxe) | 2026-12-01 s/d 2026-12-04 (3 malam) | Rp1.350.000 | Aktif
```
