# Using library functions to use RSA, AES, SHA- 256 and show the result of encryption, Hashing etc
#pip install pycryptodome

import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random


# 1. SHA-256 Hashing
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


# 2. AES Encryption & Decryption (EAX Mode)
def aes_encrypt_decrypt(message, key):
    cipher_enc = AES.new(key, AES.MODE_EAX)
    nonce = cipher_enc.nonce

    ciphertext, tag = cipher_enc.encrypt_and_digest(message.encode())

    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag).decode()

    return ciphertext, plaintext


# 3. RSA Asymmetric Encryption & Decryption
def rsa_demo(message):
    key = RSA.generate(2048)

    private_key = key
    public_key = key.publickey()

    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(message.encode())

    decrypt_rsa = PKCS1_OAEP.new(private_key)
    plaintext = decrypt_rsa.decrypt(ciphertext).decode()

    return ciphertext, plaintext


if __name__ == "__main__":
    msg = "CyberSecurityLab2026"

    print(f"Original Text: {msg}\n")

    # SHA-256
    print("=== SHA-256 HASH ===")
    print(f"Hash: {sha256_hash(msg)}\n")

    # AES
    aes_key = Random.get_random_bytes(16)
    cipher_bytes, dec_msg = aes_encrypt_decrypt(msg, aes_key)

    print("=== AES ENCRYPTION ===")
    print(f"Ciphertext (Hex): {cipher_bytes.hex()}")
    print(f"Decrypted: {dec_msg}\n")

    # RSA
    rsa_cipher, rsa_dec = rsa_demo(msg)

    print("=== RSA ENCRYPTION ===")
    print(f"Ciphertext (Hex): {rsa_cipher[:32].hex()}...")
    print(f"Decrypted: {rsa_dec}")
