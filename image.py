from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad
from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Initialize the DES cipher with the provided key
    cipher = DES.new(key, DES.MODE_ECB)

    # Read the input image
    image = Image.open(input_path)
    image = image.convert("RGB")

    # Convert the image to a byte array
    image_array = bytearray(image.tobytes())

    # Pad the image array to match the block size
    padded_array = pad(image_array, DES.block_size)

    # Encrypt the padded image array
    encrypted_array = cipher.encrypt(padded_array)

    # Save the encrypted image array to the output file
    with open(output_path, 'wb') as file:
        file.write(encrypted_array)

    print("Image encrypted successfully.")

# Example usage
input_image = "images.jpeg"
output_image = "images_enc.jpeg"
encryption_key = b"01234567"  # 8-byte key for DES

encrypt_image(input_image, output_image, encryption_key)