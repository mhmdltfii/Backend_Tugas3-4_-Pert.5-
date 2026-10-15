
# REST API Barang dan Kategori

## Deskripsi
REST API menggunakan Flask untuk mengelola data barang
dan kategori dengan metode CRUD.

## Teknologi
- Python
- Flask
- Flask Blueprint
- Application Factory
- Repository Pattern
- Service Layer

## Struktur Arsitektur

Client
  |
  v
Blueprint Route / Controller
  |
  v
Service
  |
  v
Repository
  |
  v
Data Sementara (List Python)

Respons dikembalikan melalui jalur sebaliknya.

## Instalasi

1. Buat virtual environment:

   python -m venv venv

2. Aktifkan virtual environment di Windows:

   venv\Scripts\activate

3. Instal Flask:

   pip install Flask

## Menjalankan Aplikasi

python run.py

Server berjalan di:
http://127.0.0.1:5000

## Endpoint Kategori

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | /api/v1/categories | Semua kategori |
| GET | /api/v1/categories/1 | Detail kategori |
| POST | /api/v1/categories | Tambah kategori |
| PUT | /api/v1/categories/1 | Ubah kategori |
| DELETE | /api/v1/categories/1 | Hapus kategori |

## Endpoint Barang

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | /api/v1/items | Semua barang |
| GET | /api/v1/items/1 | Detail barang |
| POST | /api/v1/items | Tambah barang |
| PUT | /api/v1/items/1 | Ubah barang |
| DELETE | /api/v1/items/1 | Hapus barang |

## Filter Barang

- /api/v1/items?min_price=100000
- /api/v1/items?category=2
- /api/v1/items?min_price=100000&category=2

## Aturan Bisnis

1. Nama barang wajib diisi.
2. Harga harus berupa bilangan bulat nonnegatif.
3. Kategori barang harus tersedia.
4. Nama kategori wajib diisi dan tidak boleh duplikat.
5. Kategori yang masih digunakan barang tidak dapat dihapus.

## Catatan

Data disimpan dalam list Python sehingga akan kembali
ke data awal ketika aplikasi dijalankan ulang.
