
import hashlib
from Crypto.Cipher import AES

def encrypt(plaintext, key):
    # Generate a 256-bit key from the given key using SHA-256 hashing
    key = hashlib.sha256(key.encode()).digest()
    # Pad the plaintext to a multiple of 16 bytes
    plaintext = plaintext + " " * (16 - len(plaintext) % 16)
    # Initialize the AES cipher with the key
    cipher = AES.new(key, AES.MODE_ECB)
    # Encrypt the padded plaintext using AES in ECB mode
    ciphertext = cipher.encrypt(plaintext.encode())
    # Return the ciphertext in base64-encoded format
    return ciphertext.hex()

def decrypt(ciphertext, key):
    # Generate a 256-bit key from the given key using SHA-256 hashing
    key = hashlib.sha256(key.encode()).digest()
    # Initialize the AES cipher with the key
    cipher = AES.new(key, AES.MODE_ECB)
    # Decrypt the ciphertext using AES in ECB mode
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext)).decode().rstrip()
    # Return the decrypted plaintext
    return plaintext

# Example usage
key = "mysecretkey"
plaintext = "Hello, world!"
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)