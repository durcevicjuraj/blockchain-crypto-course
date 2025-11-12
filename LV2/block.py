import hashlib
from transaction import Transaction
import json

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