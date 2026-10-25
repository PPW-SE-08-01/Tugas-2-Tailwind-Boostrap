
# 🏨 Grand Luxora Hotel

### Tugas 2 – Pemrograman Web

Website **Grand Luxora Hotel** merupakan project website reservasi hotel yang dikembangkan sebagai bagian dari tugas mata kuliah Pemrograman Web.

Project ini dibuat dalam dua versi menggunakan framework CSS yang berbeda, yaitu **Tailwind CSS** dan **Bootstrap 5**, untuk mempelajari serta membandingkan penerapan kedua framework dalam membangun website yang modern dan responsif.

## 📁 Struktur Folder

```text
Tugas-2-Tailwind-Boostrap/
│
├── boostrap-version/
│   ├── index.html
│   ├── rooms.html
│   ├── reservation.html
│   ├── booking.html
│   ├── css/
│   └── images/
│
├── tailwind-version/
│   ├── index.html
│   ├── rooms.html
│   ├── reservation.html
│   ├── booking.html
│   └── images/
│
└── README.md
```

*Struktur file di dalam setiap folder dapat disesuaikan dengan implementasi project.*

## ✨ Fitur Website

**1. Home**

Halaman utama yang memperkenalkan Grand Luxora Hotel dan menyediakan navigasi menuju halaman lainnya.

**2. Rooms**

Menampilkan tiga pilihan kamar beserta fasilitas dan harga per malam:

| Tipe Kamar | Harga / Malam |
|---|---|
| Deluxe Room | Rp500.000 |
| Suite Room | Rp900.000 |
| Family Room | Rp1.200.000 |

**3. Reservation**

Halaman formulir reservasi yang menyediakan input:

- Nama lengkap
- Nomor telepon
- Pilihan tipe kamar
- Tanggal check-in dan check-out
- Jumlah tamu

**4. My Booking**

Halaman yang disediakan untuk menampilkan informasi reservasi. Pada versi statis tanpa JavaScript atau backend, data booking belum dapat disimpan dan ditampilkan secara otomatis.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| HTML5 | Struktur halaman website |
| CSS3 | Styling tambahan |
| Tailwind CSS | Framework styling berbasis utility class |
| Bootstrap 5 | Framework CSS berbasis komponen dan grid |
| Bootstrap Icons | Ikon pada antarmuka |
| Google Fonts | Font Poppins dan Playfair Display |

## 🎨 Desain Website

Grand Luxora Hotel menggunakan konsep desain **modern, elegan, dan minimalis** dengan kombinasi warna:

- **Gold:** `#c9a227`
- **Cream:** `#faf8f3`
- **Charcoal:** `#1c1c1c`

Website dirancang responsif agar dapat menyesuaikan tampilan pada perangkat desktop, tablet, dan mobile.

## 🚀 Cara Menjalankan Project

1. Clone repository:

   ```bash
   git clone https://github.com/AhmadShofii/Tugas-2-Tailwind-Boostrap.git
   ```

2. Masuk ke direktori project:

   ```bash
   cd Tugas-2-Tailwind-Boostrap
   ```

3. Pilih versi website yang ingin dijalankan:
   - `boostrap-version/` untuk Bootstrap.
   - `tailwind-version/` untuk Tailwind CSS.

4. Buka file `index.html` menggunakan browser atau ekstensi **Live Server** pada Visual Studio Code.

## 🔍 Perbandingan Tailwind CSS dan Bootstrap

| Aspek | Tailwind CSS | Bootstrap |
|---|---|---|
| Pendekatan | Utility-first | Component-based |
| Styling | Menggunakan utility class | Menggunakan class komponen |
| Kustomisasi | Fleksibel | Menggunakan komponen dan CSS tambahan |
| Layout | Flexbox dan Grid utilities | Bootstrap Grid System |
| Responsif | Responsive utilities | Responsive breakpoints |

## 📝 Kesimpulan

Pengembangan website Grand Luxora Hotel menggunakan Tailwind CSS dan Bootstrap memberikan pemahaman mengenai dua pendekatan berbeda dalam membangun antarmuka website.

**Tailwind CSS** memberikan fleksibilitas dalam mengatur desain melalui utility class, sedangkan **Bootstrap** menyediakan komponen dan sistem grid yang mempermudah proses pengembangan.

Kedua framework dapat digunakan untuk menghasilkan website yang menarik, terstruktur, dan responsif.

## 👨‍💻 Developer

**Ahmad Shofii**

Mata Kuliah: Pemrograman Web

GitHub: [@AhmadShofii](https://github.com/AhmadShofii)

---

**Grand Luxora Hotel** — Tugas 2 Pemrograman Web.
