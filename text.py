from Cryptodome.Cipher import DES

def pad_text(text, block_size):
    # Pad the text to be a multiple of the block size
    padding_size = block_size - (len(text) % block_size)
    padding = bytes([padding_size] * padding_size)
    return text + padding

def encrypt_file(input_path, output_path, key):
    # Initialize the DES cipher with the provided key
    cipher = DES.new(key, DES.MODE_ECB)

    # Read the input file
    with open(input_path, 'rb') as file:
        plaintext = file.read()

    # Pad the plaintext
    padded_plaintext = pad_text(plaintext, DES.block_size)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the encrypted ciphertext to the output file
    with open(output_path, 'wb') as file:
        file.write(ciphertext)

    print("File encrypted successfully.")

# Example usage
input_file = "hello.txt"
output_file = "hello1.txt"
encryption_key = b"01234567"  # 8-byte key for DES

encrypt_file(input_file, output_file, encryption_key)