# Pertemuan 13 - Debugging dan Testing

Nama: Mafatihun Nabila
NIM: 2225250198 
Kelas:3B 

## Kasus
Program ini menguji pengolahan data nilai mahasiswa yang mencakup fungsi perhitungan rata-rata, penentuan status kelulusan berdasarkan batas nilai, serta pencarian nilai tertinggi dalam suatu list.

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
|----|--------|-------|----------|-------------|--------|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 75.0 | PASS |
| T2 | rata-rata | [100, 80] | 90.0 | 90.0 | PASS |
| T3 | status | 60 | Lulus | Tidak Lulus (Sebelum Fix) | PASS |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 0 (Sebelum Fix) | PASS |

## Bug Report
1. **B01 (Fungsi Rata-rata)**: Menggunakan pembagi konstan `/ 5` alih-alih `len(nilai)`. Perbaikan: Mengganti pembagi dengan panjang list dinamis dan menambahkan validasi list kosong.
2. **B02 (Fungsi Status)**: Menggunakan operator `>` untuk batas 60 sehingga nilai 60 gagal. Perbaikan: Mengubah operator menjadi `>=`.
3. **B03 (Fungsi Nilai Tertinggi)**: Variabel `tertinggi` diinisialisasi dengan `0` dan menggunakan perbandingan `x < tertinggi`. Perbaikan: Inisialisasi dengan `nilai[0]` dan menggunakan perbandingan `x > tertinggi`.

## Retest
Seluruh pengujian ulang setelah perbaikan menghasilkan status **PASS** dan tidak ditemukan adanya regresi pada modul lain.

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py

REFLEKSI PRAKTIK 13:
1. Teknik debugging yang paling membantu:
   Penggunaan breakpoint interaktif di VS Code serta tabel test case 
   (Expected vs Actual). Hal ini sangat membantu karena kita dapat mengamati 
   perubahan nilai variabel secara langsung (real-time) dan menguji batas nilai 
   secara sistematis tanpa harus menebak-nebak letak kesalahan.

2. Mengapa bug logika lebih sulit daripada syntax error?
   Karena program dengan bug logika tetap dapat berjalan (tidak memicu exception 
   atau syntax error), namun menghasilkan output yang salah secara perhitungan 
   atau aturan bisnis (seperti kasus batas nilai 60 atau inisialisasi maksimum 
   yang salah).

3. Test case batas yang baik untuk program nilai:
   Menguji nilai tepat di ambang batas ketentuan (misalnya nilai 60 untuk lulus, 
   59 untuk tidak lulus), nilai kosong (list kosong), serta nilai ekstrem atau 
   di luar rentang normal.

4. Kebiasaan debugging yang dibawa ke proyek Pertemuan 14:
   Selalu merancang test case awal (termasuk kasus batas dan data kosong) sebelum 
   menulis kode atau melakukan perbaikan, serta mendokumentasikan setiap perubahan 
   menggunakan commit bertahap (menggunakan pesan git commit fix/test).
"""

def hitung_rata_rata(nilai):
    # Penanganan list kosong untuk mencegah ZeroDivisionError
    if len(nilai) == 0:
        return 0
    # Perbaikan: Menggunakan len(nilai) agar dinamis, bukan pembagi konstan 5
    return sum(nilai) / len(nilai)

def status(nilai):
    # Perbaikan: Menggunakan operator '>=' agar nilai 60 terbaca Lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    # Penanganan list kosong
    if len(nilai) == 0:
        return None
    
    # Perbaikan: Inisialisasi dengan elemen pertama list, bukan 0
    tertinggi = nilai[0]
    for x in nilai[1:]:
        # Perbaikan: Menggunakan operator '>' untuk mencari nilai maksimum
        if x > tertinggi:
            tertinggi = x
    return tertinggi

if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    
    print("=== HASIL PENGUJIAN SETELAH REVISI (RETEST) ===")
    print("Rata-rata [80, 60, 90, 70] :", hitung_rata_rata(nilai))
    print("Status nilai 60             :", status(60))
    print("Nilai Tertinggi             :", nilai_tertinggi(nilai))