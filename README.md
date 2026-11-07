# Kareem.net - Sistem Manajemen Work Order & Pendukung Keputusan Prioritas (SAW Method)

Kareem.net adalah aplikasi web berbasis Flask yang dirancang untuk mengelola dan memprioritaskan perintah kerja (Work Order) layanan internet (ISP). Aplikasi ini dilengkapi dengan Sistem Pendukung Keputusan (SPK) menggunakan metode **Simple Additive Weighting (SAW)** untuk menentukan prioritas penanganan Work Order oleh teknisi berdasarkan kriteria-kriteria tertentu.

---

## 🚀 Fitur Utama

1. **Manajemen Work Order Terintegrasi**:
   - Mendukung 3 jenis Work Order:
     - **Instalasi (Pemasangan Baru)**: Membutuhkan data KTP pelanggan, foto rumah, paket internet, dan harga paket.
     - **Maintenance (Gangguan Jaringan)**: Membutuhkan detail masalah/alasan gangguan.
     - **Terminate (Pemutusan Layanan)**: Membutuhkan detail alasan pemutusan.
   - Pelacakan status real-time: `Pending`, `Proses`, dan `Selesai`.

2. **Sistem Pendukung Keputusan SAW (Simple Additive Weighting)**:
   - Mengkalkulasi nilai prioritas untuk Work Order yang belum diselesaikan (`Pending` & `Proses`).
   - Kriteria yang digunakan:
     - **C1: Tingkat Urgensi** (Benefit, Bobot 30%) - Ditentukan dari jenis Work Order (Maintenance memiliki prioritas lebih tinggi dibanding Instalasi dan Terminate).
     - **C2: Jarak Lokasi** (Cost, Bobot 25%) - Jarak geografis dari Head Office (HQ) ke lokasi pelanggan dihitung secara dinamis menggunakan formula *Haversine*.
     - **C3: Jenis Gangguan** (Benefit, Bobot 25%) - Prioritas gangguan teknis.
     - **C4: Waktu Pelaporan** (Benefit, Bobot 20%) - Dihitung berdasarkan lama waktu tunggu sejak pelaporan dibuat.
   - Menampilkan detail langkah perhitungan: Matriks Keputusan (X), Matriks Ternormalisasi (R), hingga Ranking Preferensi (V).

3. **Multi-Role Authentication & Workflow Khusus**:
   - **Sales**:
     - Menginput pengajuan Work Order Instalasi baru (data calon pelanggan, paket, koordinat, foto KTP, foto rumah).
     - Status awal pengajuan: `Menunggu Konfirmasi Admin`.
     - Memantau daftar pengajuan dan status verifikasi.
     - Melihat alasan penolakan jika ditolak oleh Admin, serta dapat memperbaiki data dan mengajukannya kembali.
   - **Admin / Dispatcher**:
     - Memverifikasi pengajuan WO Instalasi dari Sales:
       - **Konfirmasi**: Memilih Teknisi 1 atau Teknisi 2 $\rightarrow$ status menjadi `Ditugaskan`.
       - **Tolak**: Wajib mengisi alasan penolakan $\rightarrow$ status menjadi `Ditolak`.
     - Mengelola Work Order Maintenance dan Terminate.
     - Memantau seluruh aktivitas, Data Pelanggan Aktif, Cetak Data Pelanggan (dengan fitur checkbox pilihan), WebGIS Monitoring Peta, dan Perhitungan Prioritas SAW.
   - **Teknisi (Teknisi 1 & Teknisi 2 - Role: `teknisi`)**:
     - Setiap akun teknisi hanya dapat melihat tugas yang ditugaskan kepadanya.
     - Mengubah status pekerjaan (`Ditugaskan` $\rightarrow$ `Proses` $\rightarrow$ `Selesai`).
     - Mengunggah 4 dokumentasi teknis instalasi lapangan (Redaman ODP, Label ODP, Redaman ONT, dan Foto Perangkat ONT).
     - Mengakses Monitoring Peta lokasi tugas dan History Pengerjaan.

---

## 🛠️ Tech Stack

Aplikasi ini dibangun menggunakan teknologi modern:
- **Backend & Web Framework**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Database ORM**: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- **Database Engine**: SQLite (Development) / MySQL (Production) via PyMySQL
- **User Authentication**: [Flask-Login](https://flask-login.readthedocs.io/)
- **Environment Management**: [python-dotenv](https://github.com/theofidry/django-dotenv)
- **Desain UI**: Modern Vanilla CSS, Responsive Layout, Glassmorphism elements.

---

## 📂 Struktur Direktori Project

```text
Kareem.net/
│
├── app/                        # Paket utama aplikasi Flask
│   ├── models/                 # Model database (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── user.py             # Model Data User (Admin, Teknisi, dll)
│   │   ├── work_order.py       # Model Data Work Order & Progres Lapangan
│   │   └── criterion.py        # Model Kriteria SAW (C1 - C4)
│   │
│   ├── routes/                 # Blueprint / Controller Routing
│   │   ├── admin.py            # Halaman Dashboard Admin & Penugasan
│   │   ├── auth.py             # Login, Logout, dan Session Management
│   │   ├── main.py             # Halaman Beranda / Landing Page
│   │   ├── technician.py       # Halaman Dashboard Teknisi & Laporan Lapangan
│   │   └── work_order.py       # CRUD & Detail Work Order
│   │
│   ├── services/               # Logika Bisnis & Perhitungan
│   │   ├── saw.py              # Logika Dasar SAW
│   │   └── saw_service.py      # Implementasi Perhitungan SAW & Jarak Haversine
│   │
│   ├── static/                 # Aset Statis (CSS, JS, Uploaded Photos)
│   │   └── uploads/            # Direktori penyimpanan foto KTP, rumah, progress
│   │
│   └── templates/              # File HTML dengan Jinja2 Templating
│
├── config.py                   # Konfigurasi Aplikasi (SQLite/MySQL, Upload Folder, dll)
├── app.py                      # File Utama Entrypoint untuk Menjalankan Aplikasi
├── requirements.txt            # Daftar Dependency Python
├── .env                        # Konfigurasi Environment & Kredensial
└── README.md                   # Dokumentasi Project (File Ini)
```

---

## ⚙️ Cara Instalasi & Konfigurasi

Ikuti langkah-langkah berikut untuk menjalankan project ini di komputer lokal Anda:

### 1. Prasyarat
Pastikan komputer Anda sudah terinstal:
- **Python 3.8** atau versi di atasnya
- **Git**
- **MySQL** (Opsional, jika ingin beralih dari SQLite ke MySQL)

### 2. Kloning Repositori
```bash
git clone https://github.com/username/Kareem.net.git
cd Kareem.net
```

### 3. Buat Virtual Environment & Aktifkan
- **Windows**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 4. Instalasi Dependency
```bash
pip install -r requirements.txt
```

### 5. Konfigurasi Environment (`.env`)
Buat sebuah file baru bernama `.env` di direktori utama proyek (jika belum ada) lalu sesuaikan konfigurasinya:
```ini
SECRET_KEY=kareem-net-super-secret-key-12345
USE_SQLITE=True

# Konfigurasi MySQL (Ubah USE_SQLITE ke False jika menggunakan MySQL)
# DB_USER=root
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=3306
# DB_NAME=kareem_monitoring
```

### 6. Jalankan Aplikasi
Jalankan file `app.py` untuk menginisialisasi database dan menjalankan web server lokal:
```bash
python app.py
```
Aplikasi akan secara otomatis membuat tabel database baru (SQLite/MySQL) dan menyuntikkan data kriteria default beserta akun demo.

Buka browser Anda dan akses:
`http://127.0.0.1:8000` atau `http://localhost:8000`

---

## 🔑 Akun Demo Bawaan (Default Credentials)

Saat pertama kali dijalankan, sistem secara otomatis membuat akun demo berikut untuk memudahkan pengujian:

| Role | Username | Password | Deskripsi |
| :--- | :--- | :--- | :--- |
| **Sales** | `sales` | `sales123` | Input WO Instalasi baru, memantau status, perbaiki data jika ditolak |
| **Admin** | `admin` | `admin123` | Verifikasi WO Instalasi (Konfirmasi ke Teknisi / Tolak berikan alasan), WO Maintenance & Terminate, Data Pelanggan, Prioritas SAW |
| **Teknisi** | `teknisi1` | `teknisi123` | Akun Teknisi 1: Menerima WO yang ditugaskan kepadanya, upload foto progres, selesaikan WO |
| **Teknisi** | `teknisi2` | `teknisi123` | Akun Teknisi 2: Menerima WO yang ditugaskan kepadanya, upload foto progres, selesaikan WO |

---

## 📐 Metode SAW (Simple Additive Weighting)
Proses prioritisasi Work Order dihitung dengan langkah-langkah berikut:
1. **Penyusunan Matriks Keputusan ($X$)**:
   Mengambil data Work Order berstatus `Pending` / `Proses` dan memetakan nilainya ke kriteria C1, C2, C3, dan C4.
2. **Normalisasi Matriks ($R$)**:
   - Kriteria tipe **benefit** (C1, C3, C4):
     $$r_{ij} = \frac{x_{ij}}{\text{max}(x_{ij})}$$
   - Kriteria tipe **cost** (C2 - Jarak):
     $$r_{ij} = \frac{\text{min}(x_{ij})}{x_{ij}}$$
3. **Perhitungan Preferensi ($V$)**:
   Mengalikan matriks ternormalisasi dengan bobot kriteria masing-masing:
   $$V_i = \sum_{j=1}^{n} w_j \cdot r_{ij}$$
   Work Order dengan nilai preferensi $V_i$ tertinggi akan ditempatkan pada ranking teratas untuk diselesaikan terlebih dahulu oleh teknisi.

---

## 📝 Catatan Penting
- Koordinat Kantor Pusat (HQ) Kareem.net didefinisikan secara default pada koordinat Jakarta (`Latitude: -6.2088`, `Longitude: 106.8456`) di file `app/services/saw_service.py`. Anda dapat menyesuaikannya dengan koordinat kantor Anda jika diperlukan.
- Foto-foto yang diunggah oleh Admin/Teknisi akan tersimpan di dalam folder `app/static/uploads/`. Pastikan folder ini memiliki hak akses menulis (*write permission*).
