from hotel import Hotel
from tamu import Tamu


def tampilkan_menu(nama_hotel):
    print("\n" + "=" * 45)
    print(f"  SISTEM RESERVASI {nama_hotel.upper()}")
    print("=" * 45)
    print("1. Lihat semua kamar")
    print("2. Lihat kamar tersedia")
    print("3. Buat reservasi")
    print("4. Lihat daftar reservasi")
    print("5. Batalkan reservasi")
    print("6. Check-out")
    print("0. Keluar")


def lihat_kamar(hotel, hanya_tersedia=False):
    daftar = hotel.kamar_tersedia() if hanya_tersedia else hotel.semua_kamar()
    if not daftar:
        print("Tidak ada kamar.")
        return
    for kamar in daftar:
        print(kamar)
        print("   Fasilitas:", ", ".join(kamar.fasilitas()))


def buat_reservasi(hotel):
    nama = input("Nama tamu            : ").strip()
    no_hp = input("No. HP               : ").strip()
    tamu = Tamu(nama, no_hp)

    print("\nKamar yang tersedia:")
    lihat_kamar(hotel, hanya_tersedia=True)

    nomor = int(input("\nNomor kamar          : "))
    tanggal = input("Check-in (YYYY-MM-DD): ").strip()
    malam = int(input("Jumlah malam         : "))

    reservasi = hotel.buat_reservasi(tamu, nomor, tanggal, malam)
    print("\nReservasi berhasil!")
    print(reservasi)


def lihat_reservasi(hotel):
    daftar = hotel.semua_reservasi()
    if not daftar:
        print("Belum ada reservasi.")
    for r in daftar:
        print(r)


def main():
    hotel = Hotel.hotel_contoh()

    while True:
        tampilkan_menu(hotel.nama)
        pilihan = input("Pilih menu: ").strip()
        try:
            if pilihan == "1":
                lihat_kamar(hotel)
            elif pilihan == "2":
                lihat_kamar(hotel, hanya_tersedia=True)
            elif pilihan == "3":
                buat_reservasi(hotel)
            elif pilihan == "4":
                lihat_reservasi(hotel)
            elif pilihan == "5":
                hotel.batalkan_reservasi(input("ID reservasi: "))
                print("Reservasi dibatalkan.")
            elif pilihan == "6":
                hotel.check_out(input("ID reservasi: "))
                print("Check-out berhasil. Terima kasih!")
            elif pilihan == "0":
                print("Terima kasih telah menggunakan sistem ini.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
