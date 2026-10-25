# Ryco Spices - Proyek Website Rempah Nusantara

Repositori proyek website profil dan katalog ekspor rempah nusantara Ryco Spices. Struktur repositori ini telah ditata ulang secara terorganisir ke dalam tiga bagian utama:

1. `bootstrap-version/`: Implementasi menggunakan Bootstrap 5.3.3 dengan stylesheet kustom super ringkas (111 baris).
2. `tailwind-version/`: Implementasi menggunakan Tailwind CSS dengan pendekatan utility-first tanpa file CSS eksternal.
3. `legacy-version/`: Folder arsip untuk menyimpan berkas web versi lama (WordPress export).

---

## 1. Struktur Direktori Proyek

```text
Ryco/
├── README.md                       # Dokumentasi utama proyek
├── images/                         # Aset gambar produk dan fasilitas (.webp, .svg)
│
├── bootstrap-version/              # Versi 1: Bootstrap 5.3 (Ringkas dan Terstruktur)
│   ├── README.md                   # Dokumentasi khusus versi Bootstrap
│   ├── css/
│   │   └── style.css               # Hanya 111 baris (mengoptimalkan utilitas Bootstrap)
│   ├── index.html                  # 1. Halaman Beranda
│   ├── tentang-kami.html           # 2. Halaman Profil Perusahaan, Visi & Misi
│   ├── layanan.html                # 3. Halaman Layanan Ekspor & Tabel Mutu
│   ├── dokter.html                 # 4. Halaman Tim Dokter Tanaman & Pakar Agronomi
│   ├── galeri.html                 # 5. Halaman Dokumentasi Panen & Fasilitas
│   ├── member.html                 # 6. Halaman Portal Login Mitra Petani & Buyer B2B
│   ├── pendaftaran.html            # 7. Halaman Formulir Registrasi Kemitraan
│   └── kontak.html                 # 8. Halaman Kontak & FAQ Ekspor
│
├── tailwind-version/               # Versi 2: Tailwind CSS (Modern Utility-First)
│   ├── README.md                   # Dokumentasi khusus versi Tailwind
│   ├── index.html                  # 1. Halaman Beranda
│   ├── tentang-kami.html           # 2. Halaman Profil Perusahaan, Visi & Misi
│   ├── layanan.html                # 3. Halaman Layanan Ekspor & Tabel Mutu
│   ├── dokter.html                 # 4. Halaman Tim Dokter Tanaman & Pakar Agronomi
│   ├── galeri.html                 # 5. Halaman Dokumentasi Panen & Fasilitas
│   ├── member.html                 # 6. Halaman Portal Login Mitra Petani & Buyer B2B
│   ├── pendaftaran.html            # 7. Halaman Formulir Registrasi Kemitraan
│   └── kontak.html                 # 8. Halaman Kontak & FAQ Ekspor
│
└── legacy-version/                 # Folder Khusus: Arsip Versi Lama
    ├── assets/                     # style.css lama (3.407 baris) dan skrip lama
    ├── index.html                  # Halaman utama lama (WordPress export)
    ├── about/                      # Folder halaman about lama
    ├── contact/                    # Folder halaman contact lama
    ├── products/                   # Folder halaman products lama
    ├── build.mjs                   # Skrip migrasi lama
    ├── robots.txt                  # Berkas crawler lama
    ├── sitemap.xml                 # Berkas peta situs lama
    └── wp-old-orig/                # Salinan ekspor WordPress lama
```

---

## 2. Perbandingan Teknis Antar Versi

| Parameter | bootstrap-version/ | tailwind-version/ | legacy-version/ (Versi Lama) |
| :--- | :--- | :--- | :--- |
| Framework Utama | Bootstrap 5.3.3 | Tailwind CSS 3.x | Standalone Custom CSS |
| Baris CSS Kustom | 111 baris | 0 baris (Utility-first) | 3.407 baris |
| Ukuran File CSS | Sekitar 3 KB | 0 KB (Tanpa file CSS) | Sekitar 73 KB |
| Sistem Grid | Bootstrap Grid (.container, .row, .col) | Tailwind Flex & Grid Utilities | Grid kustom warisan |
| Ikonografi | Bootstrap Icons 1.11.3 | Bootstrap Icons 1.11.3 | SVG inline manual |
| Kemudahan Pemeliharaan | Sangat mudah dan modular | Sangat fleksibel dan cepat diedit | Sulit karena banyak konflik aturan |
| Jumlah Halaman | 8 Halaman terstandarisasi | 8 Halaman terstandarisasi | 4 Halaman terfragmentasi |

---

## 3. Rangkuman 8 Halaman yang Disediakan

1. index.html: Halaman beranda dengan hero banner rempah, empat keunggulan komparatif, katalog produk unggulan (Biji Pala, Fuli, Cengkeh, Kayu Manis), serta ajakan kemitraan ekspor.
2. tentang-kami.html: Narasi warisan perkebunan rempah Banda Neira, visi dan misi jangka panjang, serta fondasi nilai etika dan keberlanjutan.
3. layanan.html: Layanan pengadaan partai besar (FCL/LCL), seleksi grade ABCD, pengujian laboratorium aflatoksin, pengemasan ekspor, dan tabel spesifikasi mutu.
4. dokter.html: Halaman khusus tim pakar proteksi tanaman dan agronomis kebun, pencegahan penyakit pohon pala, uji tanah vulkanik, serta pendampingan petani binaan.
5. galeri.html: Dokumentasi visual proses pemetikan buah pala, pemisahan fuli merah alami, penjemuran higienis solar dome, hingga pengemasan karung goni di gudang.
6. member.html: Portal login mandiri untuk buyer B2B (pelacakan kontainer dan unduh dokumen COA) serta petani mitra (kalender dokter tanaman dan transparansi harga).
7. pendaftaran.html: Formulir pendaftaran resmi kemitraan buyer luar negeri maupun kelompok tani binaan dengan opsi pemilihan komoditas dan sampel fisik.
8. kontak.html: Formulir pengiriman pesan, informasi kantor representatif di Jakarta, gudang pengeringan di Kepulauan Banda, serta daftar tanya jawab (FAQ).

---

## 4. Panduan Menjalankan

Seluruh halaman web dapat dijalankan secara langsung tanpa memerlukan proses kompilasi maupun instalasi dependensi tambahan.

Opsi 1: Membuka File Langsung
Klik dua kali berkas HTML yang ingin Anda uji:
- bootstrap-version/index.html
- tailwind-version/index.html

Opsi 2: Menggunakan Server Lokal Python
Jalankan perintah berikut pada terminal di dalam folder root Ryco:
```bash
python3 -m http.server 8080
```
Buka peramban web dan akses alamat:
- Versi Bootstrap: http://localhost:8080/bootstrap-version/index.html
- Versi Tailwind: http://localhost:8080/tailwind-version/index.html
- Versi Arsip Lama: http://localhost:8080/legacy-version/index.html
