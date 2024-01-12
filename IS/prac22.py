def encrypt(plain_text, key):
    # Create a matrix using the key
    matrix = [[0] * len(key) for _ in range(len(plain_text) // len(key) + 1)]

    # Populate the matrix with the plain text
    index = 0
    for i in range(len(matrix)):
        for j in range(len(key)):
            if index < len(plain_text):
                matrix[i][j] = plain_text[index]
                index += 1
            else:
                matrix[i][j] = ' '

    # Rearrange the matrix columns based on the key order
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    matrix = [[row[i] for i, _ in sorted_key] for row in matrix]

    # Extract the encrypted text from the matrix
    encrypted_text = ''.join(''.join(row) for row in matrix)

    return encrypted_text

def decrypt(ciphertext, key):
    # Create a matrix using the key
    matrix = [[''] * len(key) for _ in range(len(ciphertext) // len(key) + 1)]

    # Rearrange the matrix columns based on the key order
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    original_indices = [i for i, _ in sorted_key]

    # Populate the matrix with the encrypted text
    index = 0
    for i in range(len(matrix)):
        for j in original_indices:
            if index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    # Extract the decrypted text from the matrix
    decrypted_text = ''.join(''.join(row) for row in matrix)

    return decrypted_text.rstrip()

# Example usage
plain_text = input("Enter plain text: ").replace(" ", "")  # Remove spaces for simplicity
key = input("Enter key: ").replace(" ", "")  # Remove spaces for simplicity

encrypted_text = encrypt(plain_text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
