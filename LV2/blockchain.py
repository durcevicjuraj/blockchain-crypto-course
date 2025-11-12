from datetime import datetime
from block import Block
import json

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