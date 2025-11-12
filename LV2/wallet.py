from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import hashlib

class Wallet:
    def __init__(self, name):
        self.name = name
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        # Generate public key
        self.public_key = self.private_key.public_key()
        
    def get_address(self):
        """Returns wallet address (simplified version using public key)"""
        # Convert public key to PEM format and use as address
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        # Create a shorter address by hashing the public key
        address = hashlib.sha256(pem).hexdigest()
        return address