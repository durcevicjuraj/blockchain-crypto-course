import hashlib
import json
from datetime import datetime
import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# ==================== WALLET CLASS ====================
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
        address = hashlib.sha256(pem).hexdigest()[:40]
        return address

# ==================== TRANSACTION CLASS ====================
class Transaction:
    def __init__(self, sender, recipient, quantity):
        self.sender = sender
        self.recipient = recipient
        self.quantity = quantity
    
    def to_dict(self):
        """Convert transaction to dictionary"""
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "quantity": self.quantity
        }

# ==================== BLOCK CLASS ====================
class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Calculate SHA-256 hash of the block"""
        # Convert data to string format
        if isinstance(self.data, Transaction):
            data_string = json.dumps(self.data.to_dict(), sort_keys=True)
        else:
            data_string = str(self.data)
        
        # Concatenate all block data
        block_string = str(self.index) + str(self.timestamp) + data_string + str(self.previous_hash)
        
        # Calculate SHA-256 hash
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
    def to_dict(self):
        """Convert block to dictionary for printing"""
        if isinstance(self.data, Transaction):
            data_dict = self.data.to_dict()
        else:
            data_dict = self.data
            
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": data_dict,
            "previousHash": self.previous_hash,
            "hash": self.hash
        }

# ==================== BLOCKCHAIN CLASS ====================
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block in the blockchain"""
        genesis_block = Block(0, datetime.now().strftime("%S:%H:%d:%m:%Y"), "Genesis blok", "")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        """Get the most recent block in the chain"""
        return self.chain[-1]
    
    def add_block(self, data, timestamp=None):
        """Add a new block to the blockchain"""
        if timestamp is None:
            timestamp = datetime.now().strftime("%S:%H:%d:%m:%Y")
        
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_block = Block(new_index, timestamp, data, previous_block.hash)
        self.chain.append(new_block)
    
    def is_valid(self):
        """Check if the blockchain is valid"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Check if current block points to correct previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def print_blockchain(self):
        """Print the entire blockchain in JSON format"""
        blockchain_dict = {
            "blockchain": [block.to_dict() for block in self.chain]
        }
        print(json.dumps(blockchain_dict, indent=2, ensure_ascii=False))

# ==================== MAIN PROGRAM ====================
def main():
    print("=" * 60)
    print("LABORATORIJSKA VJEŽBA 2 - Jednostavna Kriptovaluta")
    print("=" * 60)
    
    # Create 3 wallets
    print("\n1. Creating wallets...")
    profesor = Wallet("Profesor")
    student = Wallet("Student")
    cryptowhale = Wallet("Cryptowhale")
    
    print(f"   Profesor wallet address: {profesor.get_address()}")
    print(f"   Student wallet address: {student.get_address()}")
    print(f"   Cryptowhale wallet address: {cryptowhale.get_address()}")
    
    # Initialize blockchain
    print("\n2. Initializing blockchain...")
    blockchain = Blockchain()
    print("   Genesis block created!")
    
    # Create and add transactions
    print("\n3. Creating transactions...")
    time.sleep(1)
    
    # Transaction 1: Profesor -> Student
    print("   Transaction 1: Profesor -> Student (25 coins)")
    transaction1 = Transaction(
        sender=profesor.get_address(),
        recipient=student.get_address(),
        quantity=25
    )
    blockchain.add_block(transaction1)
    time.sleep(2)
    
    # Transaction 2: Student -> Cryptowhale
    print("   Transaction 2: Student -> Cryptowhale (34 coins)")
    transaction2 = Transaction(
        sender=student.get_address(),
        recipient=cryptowhale.get_address(),
        quantity=34
    )
    blockchain.add_block(transaction2)
    time.sleep(1)

    
    # Transaction 3: Cryptowhale -> Profesor
    print("   Transaction 3: Cryptowhale -> Profesor (34 coins)")
    transaction3 = Transaction(
        sender=cryptowhale.get_address(),
        recipient=profesor.get_address(),
        quantity=34
    )
    blockchain.add_block(transaction3)
    time.sleep(2)

    
    # Validate blockchain
    print("\n4. Validating blockchain...")
    is_valid = blockchain.is_valid()
    print(f"   Blockchain is valid: {is_valid}")
    
    # Print blockchain
    print("\n5. Blockchain contents:")
    print("=" * 60)
    blockchain.print_blockchain()
    print("=" * 60)
    
    print("\n✓ Assignment completed successfully!")

if __name__ == "__main__":
    main()