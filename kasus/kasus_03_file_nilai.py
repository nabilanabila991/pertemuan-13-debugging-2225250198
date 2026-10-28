def baca_file_nilai(nama_file):
    try:
        with open(nama_file, 'r') as file:
            baris = file.readlines()
            nilai = [int(b.strip()) for b in baris if b.strip().isdigit()]
            return nilai
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return []
    except ValueError:
        print("Error: Terdapat format nilai yang tidak valid di dalam file.")
        return []

if __name__ == "__main__":
    # Uji coba pembacaan file (pastikan file nilai.txt tersedia jika ingin diuji riil)
    hasil = baca_file_nilai("nilai.txt")
    print("Data nilai dari file:", hasil)