def caesar_cipher_encrypt(text, shift):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher.
    text: string teks yang akan dienkripsi.
    shift: jumlah pergeseran huruf.
    """
    result = ""  # Variabel untuk menyimpan hasil enkripsi
    
    # Loop untuk memproses setiap karakter dalam teks
    for char in text:
        # Periksa apakah karakter adalah huruf
        if char.isalpha():
            # Hitung huruf awal (A atau a) berdasarkan huruf kapital atau kecil
            start = ord('A') if char.isupper() else ord('a')
            
            # Geser huruf dan wrap-around menggunakan modulus
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted_char
        else:
            # Jika bukan huruf, tambahkan karakter asli (misalnya spasi, angka)
            result += char

    return result


def caesar_cipher_decrypt(text, shift):
    """
    Fungsi untuk mendekripsi teks yang telah dienkripsi menggunakan Caesar Cipher.
    text: string teks yang akan didekripsi.
    shift: jumlah pergeseran huruf (sama dengan saat enkripsi).
    """
    # Dekripsi hanya kebalikan dari enkripsi, jadi shift menjadi negatif
    return caesar_cipher_encrypt(text, -shift)


# Contoh Penggunaan
plaintext = "Halo Dunia 123!"
shift = 3

# Enkripsi
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print("Teks Asli:       ", plaintext)
print("Teks Terenkripsi:", encrypted_text)

# Dekripsi
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Teks Didekripsi: ", decrypted_text)
