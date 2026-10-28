def status_lulus(nilai):
    # Versi perbaikan: menggunakan '>='
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

if __name__ == "__main__":
    print("Test Case 59:", status_lulus(59))  # Expected: Tidak lulus
    print("Test Case 60:", status_lulus(60))  # Expected: Lulus
    print("Test Case 61:", status_lulus(61))  # Expected: Lulus