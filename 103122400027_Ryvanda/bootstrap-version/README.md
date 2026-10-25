# Dokumentasi Website Ryco Spices - Versi Bootstrap 5

Dokumentasi teknis untuk implementasi website profil dan katalog ekspor rempah nusantara Ryco Spices menggunakan framework Bootstrap 5.3.3.

---

## 1. Ringkasan Proyek

Versi ini dirancang untuk menyederhanakan kode website dari versi warisan sebelumnya yang menggunakan stylesheet hingga 3.400 baris. Pada versi Bootstrap ini, seluruh tata letak dan komponen distandarisasi menggunakan sistem utilitas Bootstrap 5.3.3, sehingga file CSS kustom berhasil dipangkas menjadi hanya 111 baris tanpa mengurangi kualitas visual maupun fungsi interaktif.

---

## 2. Struktur Berkas

```text
bootstrap-version/
├── README.md
├── css/
│   └── style.css            # Stylesheet kustom ringkas (111 baris)
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

- Framework CSS: Bootstrap 5.3.3 via CDN (jsDelivr)
- Framework JS: Bootstrap Bundle 5.3.3 (Popper included)
- Ikon: Bootstrap Icons 1.11.3 via CDN
- Tipografi: Playfair Display (Heading) dan Plus Jakarta Sans (Body text) via Google Fonts
- Palet Warna Kustom:
  - Forest Green (Primary): #2D5016
  - Earth Brown (Secondary): #8B4513
  - Soft Gold (Warning/Accent): #C9A959
  - Cream White (Light Background): #FBF9F5
  - Dark Slate (Body/Text): #2D312E

---

## 4. Penjelasan File CSS Kustom (css/style.css)

File `css/style.css` hanya berukuran 111 baris dan berfokus pada:
1. Menimpa variabel CSS dasar Bootstrap (`--bs-primary`, `--bs-secondary`, `--bs-light`, `--bs-body-font-family`) agar seragam dengan identitas jenama Ryco Spices.
2. Mengatur font serif untuk elemen heading (`h1` sampai `h5`).
3. Mengatur efek latar belakang banner utama (`.hero-wrapper`).
4. Efek transisi kartu saat kursor melayang (`.card-hover`).
5. Tombol melayang WhatsApp di pojok kanan bawah (`.floating-whatsapp`).

Seluruh kebutuhan layout (grid, spasi margin/padding, flexbox, perataan teks, border, badge, dan modal/collapse) ditangani langsung oleh class bawaan Bootstrap.

---

## 5. Rincian 8 Halaman

### 1. index.html (Beranda)
- Top bar informasi kontak dan sertifikasi ekspor.
- Navigasi responsif dengan tombol hamburger untuk perangkat seluler.
- Hero section dengan ajakan bertindak (CTA).
- Bagian 4 keunggulan utama perusahaan.
- Katalog komoditas unggulan: Biji Pala (Nutmeg), Fuli (Mace), Cengkeh (Cloves), dan Kayu Manis (Cinnamon).
- Banner ajakan kemitraan dan footer informatif.

### 2. tentang-kami.html (Tentang Kami)
- Narasi sejarah rempah Kepulauan Banda dan Maluku.
- Penjelasan komitmen perdagangan yang adil (Fair Trade).
- Kartu Visi dan Misi perusahaan.
- 4 pilar nilai perusahaan: Integritas, Keberlanjutan, Pemberdayaan, dan Inovasi Pascapanen.

### 3. layanan.html (Layanan Ekspor)
- 4 layanan utama: Pengadaan FCL/LCL, Sortir Mutu Grade ABCD, Uji Laboratorium Fitosanitari, dan Pengemasan Kustom / Private Labeling.
- Tabel spesifikasi teknis parameter mutu kadar air, minyak atsiri, dan kemurnian.
- Call to action permintaan penawaran harga dan sampel.

### 4. dokter.html (Dokter Tanaman)
- Penyesuaian tema agribisnis untuk peran dokter tanaman dan proteksi kebun.
- Penjelasan program pencegahan jamur aflatoksin, kanker batang, dan uji nutrisi tanah.
- Kartu profil 4 pakar: Dr. Ir. Budi Santoso (Patologi Tanaman), Apt. Sarah Wijaya (Fitokimia), Ir. Hendra Maluku (Agronomis Lapangan), dan Dewi Anggraini, S.Si (Kepala Laboratorium Mutu).

### 5. galeri.html (Galeri)
- Dokumentasi visual menggunakan format kartu grid Bootstrap yang responsif.
- Menampilkan foto asli perkebunan, pemisahan fuli merah, penjemuran pala, cengkeh, kayu manis, dan gudang transit ekspor.

### 6. member.html (Portal Member)
- Formulir login khusus mitra petani dan buyer B2B.
- Pilihan jenis akun (Buyer, Petani Binaan, Distributor Domestik).
- Panel informasi fitur digital: Pelacakan kontainer kapal, unduh sertifikat COA mandiri, jadwal kunjungan dokter tanaman, dan transparansi harga komoditas.

### 7. pendaftaran.html (Formulir Pendaftaran)
- Formulir pendaftaran resmi calon mitra buyer ekspor maupun kelompok tani binaan.
- Input data lembaga, domisili, pilihan komoditas, estimasi tonase, dan permintaan sampel fisik.
- Notifikasi status pengiriman data berbasis komponen alert Bootstrap.

### 8. kontak.html (Kontak & FAQ)
- Formulir pengiriman pesan langsung dengan pemilihan subjek pertanyaan.
- Informasi alamat kantor representatif di Jakarta dan fasilitas gudang di Banda Neira, Maluku Tengah.
- Komponen Accordion Bootstrap untuk menjawab pertanyaan yang sering diajukan (MOQ, sampel, sertifikasi aflatoksin).

---

## 6. Cara Menjalankan

1. Melalui Browser Langsung:
   Buka file `bootstrap-version/index.html` menggunakan peramban web pilihan Anda (Google Chrome, Firefox, Edge, Safari).

2. Melalui Web Server Lokal (Disarankan):
   ```bash
   # Jalankan server lokal dari folder root proyek
   python3 -m http.server 8080
   ```
   Buka URL berikut pada browser:
   `http://localhost:8080/bootstrap-version/index.html`
