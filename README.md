# HANYA.DocReview - Aplikasi Review Dokumen PDF

## HANYA.DocReview 
adalah aplikasi yang dirancang untuk membantu pengguna mereview dokumen PDF berdasarkan kriteria yang dapat disesuaikan. Dengan memanfaatkan kecerdasan buatan (AI) dari Ollama, aplikasi ini mampu menganalisis teks yang diekstrak dari PDF dan memberikan feedback terperinci, saran revisi, serta mengidentifikasi masalah pada setiap halaman dokumen. Antarmuka yang intuitif dan struktur modular menjadikan aplikasi ini mudah digunakan dan dikembangkan lebih lanjut.

## Tujuan
HANYA.DocReview bertujuan untuk menyediakan alat yang efisien dan fleksibel bagi pengguna yang ingin mereview dokumen PDF dengan kriteria tertentu. Aplikasi ini cocok untuk editor, penulis, akademisi, atau siapa saja yang membutuhkan analisis dokumen yang mendalam dan terstruktur, didukung oleh teknologi AI untuk hasil yang lebih akurat dan bermanfaat.

## Fitur
- Autentikasi Pengguna: Sistem registrasi dan login dengan username dan password yang aman (password di-hash).
- Konfigurasi Kriteria: Pengguna dapat menentukan kriteria review, seperti "Cek tata bahasa" atau "Cek kelengkapan isi".
- Unggah dan Analisis PDF: Unggah file PDF dan dapatkan analisis teks per halaman.
- Hasil Review Terperinci: Feedback, saran revisi, dan identifikasi masalah ditampilkan untuk setiap halaman.
- Antarmuka Ramah Pengguna: Terdapat tab "Config" untuk pengaturan dan tab "Action" untuk menjalankan review.
- Modular dan Mudah Dikembangkan: Struktur kode yang terorganisir mempermudah penyesuaian dan pengembangan.

## Instalasi
### Prasyarat
Sebelum memulai, pastikan Anda memiliki:
- Python 3.10 atau lebih baru: Terinstal di sistem Anda.
- Ollama: Terinstal dan berjalan dengan model yang diinginkan (contoh: ollama run llama3).
- Miniconda: Akan diinstal otomatis oleh skrip jika belum ada.

### Langkah Instalasi
- Clone Repository:
    ''' bash
    git clone https://github.com/your-repo/HANYA.DocReview.git
    cd HANYA.DocReview

- Jalankan Skrip Instalasi:
Berikan izin eksekusi pada skrip run.sh:
    '''bash
    chmod +x run.sh

- Jalankan skrip:
    '''bash
    run.sh

Skrip ini akan:
- Memeriksa sistem Anda (path dan arsitektur).
- Menginstal Miniconda jika belum ada.
- Membuat environment Conda dengan Python 3.10.
- Menginstal semua dependensi dari requirements.txt.
- Menjalankan aplikasi secara otomatis.

### Akses Aplikasi:
- Buka browser dan kunjungi http://localhost:7860.

## Penggunaan
Berikut adalah langkah-langkah untuk menggunakan HANYA.DocReview:
- Daftar atau Login:
- Buka tab "Login" di aplikasi.
- Masukkan username dan password untuk login.
- Jika belum memiliki akun, klik "Register" untuk membuat akun baru.

## Konfigurasi Kriteria Review:
- Setelah login, buka tab "Config".
- Tulis kriteria review yang Anda inginkan (contoh: "Cek tata bahasa dan ejaan").
- Klik "Simpan Kriteria" untuk menyimpan pengaturan.

## Unggah dan Review PDF:
- Buka tab "Action".
- Unggah file PDF yang ingin Anda review.
- Klik tombol "Review" untuk memulai proses analisis.
- Tunggu hingga proses selesai, lalu lihat hasil review yang mencakup feedback dan saran per halaman.

## Konfigurasi
- Database: Aplikasi menggunakan SQLite untuk menyimpan data pengguna dan konfigurasi. File database (app.db) akan otomatis dibuat di direktori proyek.
- Model AI: Secara default, HANYA.DocReview menggunakan model llama3 dari Ollama. Untuk mengganti model, ubah pengaturan di file ai_reviewer.py.