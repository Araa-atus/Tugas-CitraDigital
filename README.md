
# Pembuktian Citra Digital sebagai Susunan Angka

## Identitas Mahasiswa
- Nama: [Maratus Sholihah]
- NIM: [24260043]
- Program Studi: [Teknik Informatika]
- Mata Kuliah: [Pengolahan Citra Digital]

## 1. Deskripsi Proyek

Proyek ini dibuat untuk membuktikan bahwa citra digital
merupakan susunan pixel yang dapat direpresentasikan
dalam bentuk data numerik menggunakan bahasa pemrograman Python.

Program menganalisis foto objek nyata dengan membaca dimensi,
nilai pixel RGB, matriks numerik, dan metadata gambar.

## 2. Tujuan

1. Membuktikan bahwa gambar digital tersusun dari pixel.
2. Menampilkan nilai numerik setiap pixel.
3. Menjelaskan representasi warna RGB.
4. Menyimpan data pixel dalam bentuk CSV.
5. Mengekstrak metadata gambar.
6. Membuat visualisasi pixel dan matriks RGB.

## 3. Teknologi yang Digunakan

- Python
- Pillow
- NumPy
- Matplotlib
- Visual Studio Code
- GitHub

## 4. Struktur Proyek

```text
pembuktian-citra-digital/
├── data/
│   └── foto_objek.jpg
├── hasil/
│   ├── data_seluruh_pixel.csv
│   ├── matriks_rgb_10x10.csv
│   ├── metadata.json
│   └── visualisasi_pixel.png
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

File di dalam folder hasil dibuat otomatis setelah program
berhasil dijalankan.

## 5. Cara Kerja Program

### A. Membaca Gambar
Program membaca foto menggunakan library Pillow untuk
memperoleh format, dimensi, mode warna, dan ukuran file.

### B. Menghitung Pixel
Jumlah pixel dihitung dengan rumus:

Jumlah pixel = lebar gambar x tinggi gambar

### C. Mengubah Gambar Menjadi Angka
Gambar dikonversi ke format RGB dan diubah menjadi array
numerik menggunakan NumPy.

Setiap pixel memiliki tiga nilai kanal:
- R: Red (merah)
- G: Green (hijau)
- B: Blue (biru)

Dalam RGB standar 8-bit, setiap kanal memiliki nilai
dari 0 sampai 255.

Contoh:
- (255, 0, 0) = merah
- (0, 255, 0) = hijau
- (0, 0, 255) = biru
- (255, 255, 255) = putih
- (0, 0, 0) = hitam

### D. Mengekstrak Metadata
Program menyimpan informasi gambar, seperti format,
dimensi, jumlah pixel, ukuran file, dan metadata EXIF
jika tersedia.

### E. Membuat Visualisasi
Program menampilkan foto asli, area pixel yang diperbesar,
dan matriks angka RGB untuk menunjukkan hubungan
antara gambar dan data numeriknya.

## 6. Hasil Program

Program menghasilkan empat file:

1. `data_seluruh_pixel.csv`
   Berisi koordinat pixel dan nilai R, G, B untuk seluruh
   pixel gambar.

2. `matriks_rgb_10x10.csv`
   Berisi nilai RGB untuk maksimal 10 x 10 pixel pertama.

3. `metadata.json`
   Berisi informasi gambar dan metadata EXIF jika tersedia.

4. `visualisasi_pixel.png`
   Berisi visualisasi foto, pixel yang diperbesar,
   dan matriks nilai RGB.

## 7. Cara Menjalankan Program

### Persyaratan
Python harus sudah terpasang di komputer.

### Instalasi Library

Jalankan perintah:

```bash
python -m pip install -r requirements.txt
```

### Menyiapkan Foto
Letakkan foto objek nyata di folder `data` dan beri nama
`foto_objek.jpg`.

### Menjalankan Program

Jalankan perintah:

```bash
python main.py
```

Hasil analisis akan disimpan dalam folder `hasil`.

## 8. Kesimpulan

Citra digital dapat direpresentasikan sebagai susunan pixel
yang memiliki koordinat dan nilai numerik.

Dalam representasi RGB, setiap pixel mempunyai tiga nilai
kanal warna, yaitu merah, hijau, dan biru.

Melalui Python, gambar dapat dibaca sebagai array numerik,
dianalisis berdasarkan koordinat pixel, dan disimpan sebagai
matriks angka. Visualisasi serta data hasil analisis menjadi
bukti bahwa citra digital dapat direpresentasikan secara
numerik.

Metadata memberikan informasi tambahan tentang file gambar,
sedangkan ketersediaan EXIF bergantung pada gambar yang digunakan.
