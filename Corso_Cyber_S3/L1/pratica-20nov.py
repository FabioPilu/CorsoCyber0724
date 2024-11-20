def caesar_decrypt(ciphertext, shift, alphabet):
    decrypted_text = ""
    alphabet_length = len(alphabet)
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index - shift) % alphabet_length
            decrypted_text += alphabet[shifted_index]
        else:
            decrypted_text += char
    return decrypted_text
alphabet = "ABCDEFGHILMNOPQRSTUVZ"
ciphertext = "HSNFRGH"

for shift in range(1, 22):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift, alphabet)}")