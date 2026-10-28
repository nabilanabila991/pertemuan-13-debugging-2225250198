def status_lulus(nilai):
    # Bug awal: Menggunakan operator '>' sehingga nilai 60 dianggap tidak lulus
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    print("Test nilai 75:", status_lulus(75))
    print("Test nilai 60:", status_lulus(60))  # Bug: Menghasilkan 'Tidak lulus'
    print("Test nilai 59:", status_lulus(59))