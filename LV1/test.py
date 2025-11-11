from cryptography.hazmat.primitives.asymmetric import rsa, padding

print("Generate keys")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()
print("Keys generated\n")

message = "jurajFERITdurcevic"
print(f"Message: {message}")

encrypted = public_key.encrypt(
    message.encode('utf-8'),
    padding.PKCS1v15() 
)
print(f"Encrypted: {encrypted.hex()}\n")

decrypted = private_key.decrypt(
    encrypted,
    padding.PKCS1v15()
)
decrypted_message = decrypted.decode('utf-8')
print(f"Decrypted: {decrypted_message}")
print(f"\nCorrect? {message == decrypted_message}")
