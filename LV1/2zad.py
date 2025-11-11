import hashlib

test_text = "FERIT"
expected = "0ec299f96b70e36bc823d0a546b725fccc97c00e00dba67f7322abc9ab6ce0eb"

hash_result = hashlib.sha256(test_text.encode('utf-8')).hexdigest()

print(f"Text: {test_text}")
print(f"sha-256: {hash_result}")
print(f"Expected: {expected}")
print(f"Correct? {hash_result == expected}")