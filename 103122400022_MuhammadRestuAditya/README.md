<div align="center">

# TUGAS PRAKTIKUM PEMROGRAMAN WEB
## TUGAS 3: FETCH API & ASYNCHRONOUS JAVASCRIPT
### Operasi CRUD (GET, POST, PUT, DELETE) JSONPlaceholder

<br>

<img src="logo.png" width="140" alt="Logo Telkom University Purwokerto">

<br>
<br>

**Disusun Oleh :**

**Muhammad Restu Aditya / 103122400022**  
**SE-08-01**

<br>

**Asisten Praktikum :**  
Abu Abdirrahman Humaid Al-Atsary  
Hamka Zainul Ardhi

<br>

**Dosen Pengampu :**  
Arif Amrulloh, S.Kom., M.Kom.

<br>
<br>

### PROGRAM STUDI S1 SOFTWARE ENGINEERING
### FAKULTAS INFORMATIKA
### TELKOM UNIVERSITY PURWOKERTO
### 2026

</div>

---

## 1. Penjelasan Program

Aplikasi ini merupakan program berbasis web yang dirancang untuk menguji sekaligus menerapkan pemanggilan Fetch API secara asinkron menggunakan sintaks `async/await` pada JavaScript.

Program ini terhubung langsung ke layanan REST API publik JSONPlaceholder melalui endpoint `/posts`. Melalui aplikasi ini, diimplementasikan alur kerja operasi CRUD secara utuh, yaitu pengambilan data menggunakan metode GET, pembuatan postingan baru menggunakan metode POST, pembaruan data yang sudah ada menggunakan metode PUT, serta penghapusan data menggunakan metode DELETE. Seluruh komunikasi data berlangsung di latar belakang tanpa memerlukan pemuatan ulang (reload) halaman peramban, sehingga interaksi pengguna terasa lebih cepat dan responsif.

---

## 2. Penjelasan 4 Metode HTTP dari Kode

Semua interaksi HTTP pada berkas `app.js` dibangun menggunakan fungsi asinkron (`async/await`) yang dibungkus oleh blok penanganan kesalahan `try...catch` agar setiap kegagalan jaringan atau respons error dapat ditangani secara aman.

### Metode GET (Mengambil Data)
Fungsi `getPosts()` bertugas meminta daftar data postingan ke endpoint API dengan parameter pembatas enam postingan awal (`?_limit=6`). Program memanfaatkan `await` untuk menunggu proses penerimaan respons server, lalu mengubah data mentah tersebut menjadi objek JavaScript melalui metode `res.json()`. Setelah objek JSON berhasil didapatkan, data disimpan ke dalam variabel lokal penampung dan diteruskan ke fungsi perenderan antarmuka untuk dimunculkan sebagai kartu-kartu postingan.

### Metode POST (Menambahkan Data)
Fungsi `createPost(e)` menangani penambahan konten baru berdasarkan data judul serta isi yang dimasukkan pengguna melalui formulir. Permintaan dikirim ke server dengan menentukan metode POST, menyertakan header `Content-Type: application/json`, dan melampirkan data masukan dalam format teks JSON. Ketika server merespons dengan status berhasil `201 Created` beserta ID data yang baru dibentuk, data tersebut disisipkan ke posisi paling awal pada daftar data lokal, lalu tampilan antarmuka di-render ulang secara seketika agar postingan baru langsung tampil di layar.

### Metode PUT (Memperbarui Data)
Fungsi `updatePost(e)` bekerja untuk memperbarui informasi postingan yang telah ada berdasarkan nomor ID spesifik yang dipilih. Fungsi mengirimkan request dengan metode PUT menuju endpoint `/posts/{id}` serta menyertakan data baru judul dan konten sebagai payload JSON. Begitu server mengembalikan status sukses `200 OK`, program mencari posisi indeks data tersebut di dalam array lokal, menimpanya dengan data yang telah diperbarui, dan menyegarkan tampilan halaman untuk memperlihatkan perubahan tersebut.

### Metode DELETE (Menghapus Data)
Fungsi `deletePost(e)` berfungsi untuk meniadakan data postingan dari server melalui pengiriman permintaan bermetode DELETE ke URL `/posts/{id}`. Setelah server memastikan proses penghapusan berhasil melalui status `200 OK`, fungsi akan menyaring dan menghapus postingan dengan ID yang sesuai dari daftar array lokal. Selanjutnya, fungsi penampil data dipanggil kembali sehingga elemen kartu postingan tersebut langsung terhapus dari tampilan visual.

---

## 3. Mapping Data ke HTML DOM

Fungsi `tampilkanData(data)` bertanggung jawab memetakan data array postingan menjadi elemen tampilan HTML secara dinamis. Fungsi ini terlebih dahulu mengosongkan kontainer penampung agar data sebelumnya tidak bertumpuk, kemudian menjalankan perulangan `forEach` terhadap setiap objek postingan. Pada setiap iterasi, dibuat elemen kartu baru (`post-card`), diisi konten judul dan badan postingan menggunakan properti `innerHTML`, lalu dimasukkan ke dalam elemen kontainer utama menggunakan perintah `appendChild()`. Dengan alur tersebut, setiap perubahan pada data lokal dapat langsung terlihat pada layar pengguna secara rapi dan konsisten.
