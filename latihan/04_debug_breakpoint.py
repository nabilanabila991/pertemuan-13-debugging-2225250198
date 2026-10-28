def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)

if __name__ == "__main__":
    print("Test 1:", rata_rata([80, 90, 70]))
    print("Test 2:", rata_rata([100, 80]))
    print("Test 3 (Kosong):", rata_rata([]))