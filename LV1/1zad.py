import base58

test_text = "FERIT"
expected = "8vpytW7"

print("Encoded\n")
encoded = base58.b58encode(test_text.encode('utf-8')).decode('utf-8')
print(f"Text: {test_text}")
print(f"base58: {encoded}")
print(f"Expected {expected}")
print(f"Correctly encoded? {encoded == expected}")

print("\nDecoded")
decoded = base58.b58decode(encoded).decode('utf-8')
print(f"\nDecoded: {decoded}")
print(f"Correct? {decoded == test_text}")