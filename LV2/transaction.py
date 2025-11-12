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