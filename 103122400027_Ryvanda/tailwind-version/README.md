# Dokumentasi Website Ryco Spices - Versi Tailwind CSS

Dokumentasi teknis untuk implementasi website profil dan katalog ekspor rempah nusantara Ryco Spices menggunakan pendekatan utility-first dengan framework Tailwind CSS.

---

## 1. Ringkasan Proyek

Versi ini dibangun sepenuhnya menggunakan arsitektur utility-first Tailwind CSS. Berbeda dengan pendekatan tradisional yang memerlukan penulisan ribuan baris aturan CSS terpisah, versi ini tidak membutuhkan berkas CSS eksternal sama sekali (0 baris berkas CSS kustom). Seluruh gaya, tata letak, warna tema, efek interaktif, dan responsivitas diatur langsung pada atribut class elemen HTML.

---

## 2. Struktur Berkas

```text
tailwind-version/
├── README.md
├── index.html               # 1. Halaman Beranda Utama
├── tentang-kami.html        # 2. Halaman Profil Perusahaan, Visi & Misi
├── layanan.html             # 3. Halaman Layanan Ekspor & Spesifikasi Mutu
├── dokter.html              # 4. Halaman Tim Dokter Tanaman & Pakar Agronomi
├── galeri.html              # 5. Halaman Dokumentasi Panen & Fasilitas
├── member.html              # 6. Halaman Portal Login Mitra Petani & Buyer B2B
├── pendaftaran.html         # 7. Halaman Formulir Pendaftaran Kemitraan
└── kontak.html              # 8. Halaman Kontak Kantor & Tanya Jawab (FAQ)
```

---

## 3. Spesifikasi Teknis

- Framework CSS: Tailwind CSS via Play CDN Script
- Ikon: Bootstrap Icons 1.11.3 via CDN
- Tipografi: Playfair Display (font-heading) dan Plus Jakarta Sans (font-sans) via Google Fonts
- Skrip Tambahan: Skrip JavaScript Vanilla ringan untuk fungsi buka-tutup menu navigasi mobile (`toggleMobileMenu`)

---

## 4. Konfigurasi Tema (tailwind.config)

Setiap halaman menyertakan konfigurasi tema internal melalui script Tailwind untuk mendefinisikan palet warna resmi Ryco Spices:

```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        forest: {
          DEFAULT: '#2D5016',
          dark: '#1e380e',
          light: '#3e6a20'
        },
        earth: {
          DEFAULT: '#8B4513',
          dark: '#6e350d',
          light: '#a85a1f'
        },
        gold: {
          DEFAULT: '#C9A959',
          light: '#e0c785'
        },
        cream: '#FBF9F5'
      },
      fontFamily: {
        heading: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif']
      }
    }
  }
}
```

Dengan konfigurasi ini, class kustom seperti `bg-forest`, `text-gold`, `bg-cream`, dan `font-heading` dapat langsung digunakan di seluruh elemen tanpa perlu file CSS eksternal.

---

## 5. Rincian 8 Halaman

### 1. index.html (Beranda)
- Informasi bar atas, logo perusahaan, dan navigasi utama dengan menu dropdown untuk mobile.
- Hero banner menggunakan perpaduan gambar latar belakang dan gradien semitransparan Tailwind (`bg-gradient-to-r from-forest-dark/95`).
- Grid 4 kolom untuk keunggulan bisnis dengan efek transisi hover (`hover:-translate-y-1 hover:shadow-md`).
- Kartu katalog produk ekspor (Pala, Fuli, Cengkeh, Kayu Manis).
- Banner promosi kerjasama dagang ekspor dan footer lengkap.

### 2. tentang-kami.html (Tentang Kami)
- Tata letak dua kolom perpaduan foto kebun dan narasi sejarah rempah Maluku.
- Bagian Visi dan Misi dengan ikon vektor terpadu.
- Grid kartu fondasi nilai perusahaan: Integritas, Keberlanjutan, Pemberdayaan, dan Inovasi Pascapanen.

### 3. layanan.html (Layanan Ekspor)
- 4 kartu pilar layanan: Pengadaan FCL/LCL, Sortir Grade ABCD, Sertifikasi Dokumen Laboratorium, dan Kemasan Vacuum / Jute Bag.
- Tabel spesifikasi parameter mutu ekspor yang dirancang responsif menggunakan class Tailwind (`overflow-x-auto divide-y divide-stone-100`).

### 4. dokter.html (Dokter Tanaman)
- Fokus pada pembinaan perkebunan rempah: pemantauan jamur aflatoksin, pemeliharaan pohon pala, dan pencegahan hama ramah lingkungan.
- Kartu profil 4 tenaga ahli agronomis dan laboratorium.
- Banner informasi konsultasi kebun gratis bagi mitra binaan.

### 5. galeri.html (Galeri)
- Tata letak visual grid foto panen dan fasilitas ekspor (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`).
- Kartu visual dengan informasi detail produk dan label kategori yang rapi.

### 6. member.html (Portal Member)
- Desain formulir autentikasi anggota terintegrasi.
- Panel ringkasan keuntungan akun digital: pelacakan status pengiriman kontainer, pengunduhan sertifikat COA, jadwal inspeksi lapangan dokter tanaman, serta transparansi harga panen.

### 7. pendaftaran.html (Formulir Pendaftaran)
- Formulir multi-bagian yang terstruktur rapi: Pilihan tipe pendaftar (Buyer B2B vs Petani Mitra), biodata lembaga, lokasi operasional, pemilihan komoditas via checkbox, dan estimasi kuota pesanan.
- Komponen notifikasi sukses berbasis manipulasi class Tailwind sederhana.

### 8. kontak.html (Kontak & FAQ)
- Formulir kontak cepat untuk pertanyaan umum maupun permintaan sampel rempah.
- Informasi lengkap lokasi kantor di Jakarta dan gudang di Maluku.
- Kartu tanya jawab (FAQ) ringkas untuk pertanyaan seputar syarat minimum order (MOQ) dan sertifikasi fitosanitari.

---

## 6. Keunggulan Arsitektur Versi Tailwind

1. Nol Bloatware: Tidak ada baris CSS mati (unused CSS) karena seluruh styling menempel langsung pada markup.
2. Bebas Konflik Selector: Tidak ada permasalahan selektor yang saling menimpa (`specificity issues`) seperti pada file CSS konvensional yang panjang.
3. Kecepatan Render: Sangat cepat dimuat oleh peramban web karena ukuran dokumen HTML yang ringkas dan teroptimasi.
4. Konsistensi Desain: Nilai margin, padding, radius sudut, dan bayangan terkontrol melalui skala desain baku Tailwind.

---

## 7. Cara Menjalankan

1. Melalui Browser Langsung:
   Buka file `tailwind-version/index.html` menggunakan peramban web pilihan Anda.

2. Melalui Web Server Lokal (Disarankan):
   ```bash
   # Jalankan server lokal dari folder root proyek
   python3 -m http.server 8080
   ```
   Buka URL berikut pada browser:
   `http://localhost:8080/tailwind-version/index.html`
