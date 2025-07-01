def linear_search_multiple(arr, key):
    result = []
    for i in range(len(arr)):
        if arr[i] == key:
            result.append(i)
    return result

# Input dari pengguna
input_str = input("Masukkan deretan angka (pisahkan dengan spasi): ")
data = list(map(int, input_str.split()))

key = int(input("Masukkan nilai yang ingin dicari: "))
hasil = linear_search_multiple(data, key)

if hasil:
    print(f"Nilai {key} ditemukan di indeks: {', '.join(map(str, hasil))}")
else:
    print(f"Nilai {key} tidak ditemukan.")