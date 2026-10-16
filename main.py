
from pathlib import Path
from PIL import Image, ExifTags # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import json
import csv

# ==========================================
# 1. PERSIAPAN PROYEK
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "data" / "foto_objek.jpg"
OUTPUT_DIR = BASE_DIR / "hasil"
OUTPUT_DIR.mkdir(exist_ok=True)

if not IMAGE_PATH.exists():
    raise FileNotFoundError(
        "Foto tidak ditemukan! Masukkan foto ke folder "
        "'data' dan beri nama 'foto_objek.jpg'."
    )

# ==========================================
# 2. MEMBACA GAMBAR DAN METADATA
# ==========================================

with Image.open(IMAGE_PATH) as img:
    format_gambar = img.format
    mode_asli = img.mode
    lebar, tinggi = img.size
    ukuran_file = IMAGE_PATH.stat().st_size

    # Mengambil metadata EXIF jika tersedia
    metadata_exif = {}

    for tag_id, nilai in img.getexif().items():
        nama_tag = ExifTags.TAGS.get(tag_id, str(tag_id))
        metadata_exif[nama_tag] = str(nilai)

    # Mengubah gambar menjadi RGB
    gambar = img.convert("RGB")
    array_pixel = np.array(gambar)

# ==========================================
# 3. MEMBUKTIKAN GAMBAR TERSUSUN DARI ANGKA
# ==========================================

jumlah_pixel = lebar * tinggi
jumlah_angka_rgb = jumlah_pixel * 3

print("=" * 55)
print("PEMBUKTIAN CITRA DIGITAL SEBAGAI SUSUNAN ANGKA")
print("=" * 55)

print(f"Nama file       : {IMAGE_PATH.name}")
print(f"Format          : {format_gambar}")
print(f"Mode asli       : {mode_asli}")
print(f"Dimensi         : {lebar} x {tinggi} pixel")
print(f"Jumlah pixel    : {jumlah_pixel:,}")
print(f"Jumlah kanal    : 3 (RGB)")
print(f"Jumlah nilai RGB: {jumlah_angka_rgb:,}")
print(f"Ukuran file     : {ukuran_file:,} byte")
print(f"Bentuk array    : {array_pixel.shape}")

print("\nCONTOH NILAI PIXEL")
print("-" * 55)

for y in range(min(5, tinggi)):
    for x in range(min(5, lebar)):
        r, g, b = map(int, array_pixel[y, x])
        print(f"Pixel (x={x}, y={y}) = ({r}, {g}, {b})")

# ==========================================
# 4. MENYIMPAN DATA SELURUH PIXEL KE CSV
# ==========================================

file_pixel = OUTPUT_DIR / "data_seluruh_pixel.csv"

with file_pixel.open(
    "w", newline="", encoding="utf-8-sig"
) as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y", "R", "G", "B"])

    for y in range(tinggi):
        for x in range(lebar):
            r, g, b = map(int, array_pixel[y, x])
            writer.writerow([x, y, r, g, b])

# ==========================================
# 5. MEMBUAT MATRIKS RGB 10 x 10
# ==========================================

tinggi_sampel = min(10, tinggi)
lebar_sampel = min(10, lebar)
matriks = array_pixel[:tinggi_sampel, :lebar_sampel]

file_matriks = OUTPUT_DIR / "matriks_rgb_10x10.csv"

with file_matriks.open(
    "w", newline="", encoding="utf-8-sig"
) as file:
    writer = csv.writer(file)
    writer.writerow(["y/x"] + list(range(lebar_sampel)))

    for y in range(tinggi_sampel):
        baris = [y]

        for x in range(lebar_sampel):
            rgb = tuple(map(int, matriks[y, x]))
            baris.append(str(rgb))

        writer.writerow(baris)

print("\nContoh matriks RGB:")
print(matriks)

# ==========================================
# 6. MENYIMPAN METADATA KE JSON
# ==========================================

metadata = {
    "nama_file": IMAGE_PATH.name,
    "format": format_gambar,
    "mode_asli": mode_asli,
    "lebar_pixel": lebar,
    "tinggi_pixel": tinggi,
    "jumlah_pixel": jumlah_pixel,
    "mode_analisis": "RGB",
    "jumlah_kanal": 3,
    "jumlah_nilai_kanal": jumlah_angka_rgb,
    "rentang_nilai_rgb": "0 sampai 255",
    "ukuran_file_byte": ukuran_file,
    "metadata_exif": metadata_exif
}

file_metadata = OUTPUT_DIR / "metadata.json"
file_metadata.write_text(
    json.dumps(metadata, indent=4, ensure_ascii=False),
    encoding="utf-8"
)

print("\nMETADATA GAMBAR")
print("-" * 55)
print(json.dumps(metadata, indent=4, ensure_ascii=False))

# ==========================================
# 7. VISUALISASI FOTO, PIXEL, DAN ANGKA
# ==========================================

fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# Foto asli
axes[0].imshow(array_pixel)
axes[0].set_title("1. Foto Objek Asli")
axes[0].axis("off")

# Pixel diperbesar
tinggi_zoom = min(12, tinggi)
lebar_zoom = min(12, lebar)
area_zoom = array_pixel[:tinggi_zoom, :lebar_zoom]

axes[1].imshow(area_zoom, interpolation="nearest")
axes[1].set_title("2. Susunan Pixel")
axes[1].set_xticks(range(lebar_zoom))
axes[1].set_yticks(range(tinggi_zoom))
axes[1].set_xticks(
    np.arange(-0.5, lebar_zoom, 1), minor=True
)
axes[1].set_yticks(
    np.arange(-0.5, tinggi_zoom, 1), minor=True
)
axes[1].grid(which="minor", color="white", linewidth=1)
axes[1].tick_params(which="minor", bottom=False, left=False)

# Matriks angka RGB
axes[2].imshow(matriks, interpolation="nearest")
axes[2].set_title("3. Nilai RGB per Pixel")
axes[2].axis("off")

for y in range(tinggi_sampel):
    for x in range(lebar_sampel):
        r, g, b = map(int, matriks[y, x])
        kecerahan = (r + g + b) / 3
        warna_teks = "black" if kecerahan > 150 else "white"

        axes[2].text(
            x, y,
            f"{r}\n{g}\n{b}",
            ha="center",
            va="center",
            fontsize=5,
            color=warna_teks
        )

plt.tight_layout()

file_visualisasi = OUTPUT_DIR / "visualisasi_pixel.png"
plt.savefig(file_visualisasi, dpi=200, bbox_inches="tight")
plt.show()

# ==========================================
# 8. RINGKASAN HASIL
# ==========================================

print("\n" + "=" * 55)
print("ANALISIS SELESAI!")
print("=" * 55)
print("File hasil yang dibuat:")
print("- hasil/data_seluruh_pixel.csv")
print("- hasil/matriks_rgb_10x10.csv")
print("- hasil/metadata.json")
print("- hasil/visualisasi_pixel.png")
print("\nKesimpulan: gambar berhasil dibaca sebagai")
print("array numerik yang berisi nilai RGB setiap pixel.")
