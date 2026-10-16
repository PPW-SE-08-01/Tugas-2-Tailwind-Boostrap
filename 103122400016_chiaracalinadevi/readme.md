# LAPORAN PRAKTIKUM
# PEMROGRAMAN PERANGKAT BERGERAK

<br>

<div align="center">

# MODUL 04
## LANDING PAGE WITH BOOTSTRAP

<br>

**Disusun Oleh :**

**Chiara Calina Devi**  
**NIM: 103122400016**  
**Kelas: SE08-01**

<br>

**Asisten Praktikum :**  
Abu Abdirrahman Humaid Al-Atsary  
Hamka Zainul Ardhi
<br>

**Dosen Pengampu :**  
Arif Amrullah, S.Kom., M.Kom.

<br>

**PROGRAM STUDI S1 SOFTWARE ENGINEERING**  
**FAKULTAS INFORMATIKA**  
**TELKOM UNIVERSITY PURWOKERTO**  
**2026**

</div>

---

# A. SOAL

Membuat sebuah landing page sederhana bertema jual beli boneka Barbie beserta perlengkapannya menggunakan framework CSS **Bootstrap**. Landing page menggunakan warna peach dan pink muda kalem, dilengkapi gambar produk, serta memiliki komponen dasar berupa navbar, hero section, section konten (keunggulan dan produk), dan footer. Tampilan harus rapi, responsif, dan dapat dibuka melalui browser.

# B. JAWABAN

## 1. Source Code

### a. `index.html`

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pinky Doll Shop — Bootstrap</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
  <link href="style.css" rel="stylesheet">
</head>
<body>
  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg bg-peach sticky-top shadow-sm">
    <div class="container">
      <a class="navbar-brand fw-bold text-pink" href="#">🎀 Pinky Doll Shop</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="menu">
        <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-2">
          <li class="nav-item"><a class="nav-link" href="#beranda">Beranda</a></li>
          <li class="nav-item"><a class="nav-link" href="#keunggulan">Keunggulan</a></li>
          <li class="nav-item"><a class="nav-link" href="#produk">Produk</a></li>
          <li class="nav-item"><a class="btn btn-pink btn-sm" href="#kontak">Hubungi Kami</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- HERO -->
  <header id="beranda" class="bg-hero py-5">
    <div class="container py-lg-4">
      <div class="row align-items-center g-4">
        <div class="col-lg-6 text-center text-lg-start">
          <span class="badge rounded-pill bg-white text-pink mb-3 px-3 py-2">✨ Jual Beli Boneka Fashion</span>
          <h1 class="display-4 fw-bold">Koleksi Boneka Barbie &amp; Perlengkapannya</h1>
          <p class="lead my-3">Temukan boneka, outfit, rumah, hingga aksesori impian dengan harga bersahabat. Bisa beli baru maupun jual kembali koleksimu!</p>
          <a href="#produk" class="btn btn-pink me-2">Belanja Sekarang</a>
          <a href="#kontak" class="btn btn-outline-pink">Jual Koleksimu</a>
        </div>
        <div class="col-lg-6">
          <img src="assets/hero.svg" class="img-fluid rounded-4 shadow" alt="Boneka fashion">
        </div>
      </div>
    </div>
  </header>

  <!-- KEUNGGULAN -->
  <section id="keunggulan" class="py-5">
    <div class="container py-3">
      <div class="text-center mb-5">
        <h2 class="fw-bold">Kenapa Belanja di Sini?</h2>
        <p>Tiga alasan kenapa koleksi kamu aman bersama kami.</p>
      </div>
      <div class="row g-4">
        <div class="col-md-4"><div class="card card-soft h-100 text-center p-4">
          <div class="icon-circle">💖</div><h5 class="fw-bold">Kondisi Terjamin</h5>
          <p class="mb-0">Setiap barang dicek dan dibersihkan sebelum dijual, baik baru maupun preloved.</p></div></div>
        <div class="col-md-4"><div class="card card-soft h-100 text-center p-4">
          <div class="icon-circle">🔄</div><h5 class="fw-bold">Jual &amp; Beli</h5>
          <p class="mb-0">Punya boneka yang sudah tidak dipakai? Kami bantu jualkan dengan harga adil.</p></div></div>
        <div class="col-md-4"><div class="card card-soft h-100 text-center p-4">
          <div class="icon-circle">🎁</div><h5 class="fw-bold">Packing Aman &amp; Cantik</h5>
          <p class="mb-0">Dikemas rapi dengan bubble wrap, siap dikirim atau jadi hadiah.</p></div></div>
      </div>
    </div>
  </section>

  <!-- PRODUK -->
  <section id="produk" class="py-5 bg-peach">
    <div class="container py-3">
      <div class="text-center mb-5">
        <h2 class="fw-bold">Produk Favorit</h2>
        <p>Pilihan terlaris minggu ini.</p>
      </div>
      <div class="row g-4">
        <div class="col-sm-6 col-lg-4"><div class="card card-soft h-100">
          <img src="assets/doll.svg" class="card-img-top" alt="Boneka">
          <div class="card-body"><h5 class="fw-bold">Boneka Fashion Classic</h5><p>Boneka dengan rambut pirang dan gaun pink.</p><p class="fw-bold text-pink mb-0">Rp 189.000</p></div></div></div>
        <div class="col-sm-6 col-lg-4"><div class="card card-soft h-100">
          <img src="assets/outfit.svg" class="card-img-top" alt="Outfit">
          <div class="card-body"><h5 class="fw-bold">Set Gaun &amp; Outfit</h5><p>Paket 5 pakaian pesta dan casual.</p><p class="fw-bold text-pink mb-0">Rp 75.000</p></div></div></div>
        <div class="col-sm-6 col-lg-4"><div class="card card-soft h-100">
          <img src="assets/house.svg" class="card-img-top" alt="Rumah">
          <div class="card-body"><h5 class="fw-bold">Rumah Impian Mini</h5><p>Rumah boneka dua lantai lengkap furnitur.</p><p class="fw-bold text-pink mb-0">Rp 450.000</p></div></div></div>
        <div class="col-sm-6 col-lg-6"><div class="card card-soft h-100">
          <img src="assets/car.svg" class="card-img-top" alt="Mobil">
          <div class="card-body"><h5 class="fw-bold">Mobil Pink Convertible</h5><p>Mobil mainan muat 2 boneka.</p><p class="fw-bold text-pink mb-0">Rp 220.000</p></div></div></div>
        <div class="col-sm-6 col-lg-6"><div class="card card-soft h-100">
          <img src="assets/accessories.svg" class="card-img-top" alt="Aksesori">
          <div class="card-body"><h5 class="fw-bold">Aksesori &amp; Sepatu</h5><p>Tas, sepatu, topi, dan perhiasan mini.</p><p class="fw-bold text-pink mb-0">Rp 45.000</p></div></div></div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer id="kontak" class="footer-pink py-5">
    <div class="container">
      <div class="row g-4">
        <div class="col-md-5"><h5 class="fw-bold">🎀 Pinky Doll Shop</h5><p>Toko jual beli boneka fashion beserta perlengkapannya.</p></div>
        <div class="col-md-3"><h6 class="fw-bold">Menu</h6><ul class="list-unstyled mb-0"><li><a class="text-decoration-none text-reset" href="#beranda">Beranda</a></li><li><a class="text-decoration-none text-reset" href="#keunggulan">Keunggulan</a></li><li><a class="text-decoration-none text-reset" href="#produk">Produk</a></li></ul></div>
        <div class="col-md-4"><h6 class="fw-bold">Kontak</h6><p class="mb-0">📱 WhatsApp: 0812-3456-7890<br>📧 hello@pinkydoll.id</p></div>
      </div>
      <hr>
      <p class="text-center small mb-0">&copy; 2026 Pinky Doll Shop. Dibuat dengan Bootstrap 5.</p>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### b. `style.css`

```css
:root{--peach:#FFE5D4;--peach-deep:#FFB88C;--pink:#F8C8DC;--pink-deep:#E98FA8;--ink:#6b4a55}
body{background:#FFF9F5;color:var(--ink);font-family:'Poppins',sans-serif}
.bg-peach{background:var(--peach)}
.bg-hero{background:linear-gradient(135deg,var(--peach),var(--pink))}
.text-pink{color:var(--pink-deep)}
.btn-pink{background:var(--pink-deep);color:#fff;border:0;border-radius:50rem;padding:.7rem 1.6rem}
.btn-pink:hover{background:#d97a95;color:#fff}
.btn-outline-pink{border:2px solid var(--pink-deep);color:var(--pink-deep);border-radius:50rem;padding:.65rem 1.6rem}
.btn-outline-pink:hover{background:var(--pink-deep);color:#fff}
.card-soft{border:0;border-radius:1.25rem;box-shadow:0 6px 20px rgba(233,143,168,.18);overflow:hidden;transition:transform .2s}
.card-soft:hover{transform:translateY(-6px)}
.icon-circle{width:64px;height:64px;border-radius:50%;background:var(--pink);display:flex;align-items:center;justify-content:center;font-size:1.8rem;margin:0 auto 1rem}
.footer-pink{background:var(--pink);color:var(--ink)}
```

## 2. Screenshot Output

### a. Beranda (Navbar & Hero Section)

![Screenshot Beranda](screenshots/beranda.png)

### b. Keunggulan

![Screenshot Keunggulan](screenshots/keunggulan.jpeg)

### c. Produk

![Screenshot Produk](screenshots/produk.jpeg)

### d. Contact (Footer)

![Screenshot Contact](screenshots/contact.jpeg)

## 3. Deskripsi Program

Program yang dibuat merupakan landing page toko jual beli boneka Barbie dan perlengkapannya bernama **Pinky Doll Shop** menggunakan framework **Bootstrap 5.3.3**. Bootstrap dimuat melalui CDN pada file `index.html`, sedangkan penyesuaian warna dan tampilan ditulis pada file `style.css`. Tema warna yang dipakai adalah peach dan pink muda kalem, yang didefinisikan sebagai CSS variable (`--peach`, `--pink`, `--pink-deep`, dan `--ink`) agar mudah diubah.

Halaman terdiri dari empat bagian utama. **Navbar** dibuat dengan komponen `navbar navbar-expand-lg` yang menempel di atas layar (`sticky-top`) dan otomatis berubah menjadi menu hamburger pada layar kecil melalui `navbar-toggler` dan `collapse`. **Hero section** menampilkan badge, judul utama, deskripsi singkat, dua tombol call-to-action ("Belanja Sekarang" dan "Jual Koleksimu"), serta gambar ilustrasi boneka, dengan layout dua kolom memakai sistem grid `row` dan `col-lg-6`. **Section Keunggulan** menjelaskan tiga nilai jual toko, yaitu kondisi barang terjamin, layanan jual dan beli, serta packing aman, dalam bentuk tiga kartu (`card`) yang tersusun dengan `col-md-4`. **Section Produk** menampilkan lima produk (boneka, set outfit, rumah, mobil, dan aksesori) lengkap dengan gambar, deskripsi, dan harga menggunakan komponen `card` dan grid `col-sm-6 col-lg-4`. Terakhir, **footer** berisi informasi singkat toko, menu navigasi, kontak, dan hak cipta.

Responsivitas didapat dari grid dan breakpoint bawaan Bootstrap (`sm`, `md`, `lg`) sehingga kolom otomatis tersusun vertikal pada layar kecil, serta gambar menggunakan class `img-fluid` agar menyesuaikan lebar layar. Class kustom seperti `btn-pink`, `card-soft`, dan `icon-circle` ditambahkan pada `style.css` untuk memberi warna pink, sudut membulat, bayangan lembut, dan efek hover pada kartu. Hasil akhirnya adalah landing page yang rapi, konsisten, responsif, dan dapat dibuka dengan baik melalui web browser.

---

## Struktur Folder Project

```text
week-4/
└── bootstrap-version/
    ├── README.md
    ├── index.html
    ├── style.css
    ├── assets/
    │   ├── hero.svg
    │   ├── doll.svg
    │   ├── outfit.svg
    │   ├── house.svg
    │   ├── car.svg
    │   └── accessories.svg
    └── screenshots/
        ├── beranda.png
        ├── keunggulan.jpeg
        ├── produk.jpeg
        └── contact.jpeg
```