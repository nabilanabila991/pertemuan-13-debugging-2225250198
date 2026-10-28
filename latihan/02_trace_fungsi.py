def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

if __name__ == "__main__":
    print("Hasil setelah diskon:", hitung_diskon(200000, 10))