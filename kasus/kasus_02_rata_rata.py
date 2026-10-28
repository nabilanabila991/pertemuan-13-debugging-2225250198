def hitung_rata_rata(data):
    total = sum(data)
    # Bug awal: Pembagi hardcoded 5 dan tidak aman untuk list kosong
    return total / 5

if __name__ == "__main__":
    print("Rata-rata [80, 90, 70]:", hitung_rata_rata([80, 90, 70]))