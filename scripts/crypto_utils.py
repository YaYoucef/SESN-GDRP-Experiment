"""Cryptographic utilities using OpenSSL.
Implements key generation, encryption/decryption, and crypto-shredding.
"""

import subprocess
import os

KEY_DIR = "keys"
os.makedirs(KEY_DIR, exist_ok=True)


def generate_keypair(user_id: str):
    private_key = f"{KEY_DIR}/{user_id}_private.pem"
    public_key = f"{KEY_DIR}/{user_id}_public.pem"

    subprocess.run([
        "openssl", "genpkey", "-algorithm", "RSA",
        "-out", private_key, "-pkeyopt", "rsa_keygen_bits:2048"
    ], check=True)

    subprocess.run([
        "openssl", "rsa", "-pubout",
        "-in", private_key, "-out", public_key
    ], check=True)

    return private_key, public_key


def crypto_shred(user_id: str):
    """GDPR Art.17 – destroy cryptographic keys."""
    for f in os.listdir(KEY_DIR):
        if user_id in f:
            os.remove(os.path.join(KEY_DIR, f))