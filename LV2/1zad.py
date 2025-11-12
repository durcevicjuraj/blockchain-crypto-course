import time
from wallet import Wallet
from transaction import Transaction
from blockchain import Blockchain

def main():
    
    # Create wallets
    print("\nCreating wallets...")
    profesor = Wallet("Profesor")
    student = Wallet("Student")
    cryptowhale = Wallet("Cryptowhale")
    
    print(f"   Profesor wallet address: {profesor.get_address()}")
    print(f"   Student wallet address: {student.get_address()}")
    print(f"   Cryptowhale wallet address: {cryptowhale.get_address()}")
    
    # Initialize blockchain
    print("\nInitializing blockchain...")
    blockchain = Blockchain()
    print("   Genesis block created!")
    
    # Create and add transactions
    print("\nCreating transactions...")
    time.sleep(1)
    
    # Transaction 1 Profesor - Student
    print("   Transaction 1: Profesor -> Student (25 coins)")
    transaction1 = Transaction(
        sender=profesor.get_address(),
        recipient=student.get_address(),
        quantity=25
    )
    blockchain.add_block(transaction1)
    time.sleep(2)
    
    # Transaction 2  Student - Cryptowhale
    print("   Transaction 2: Student -> Cryptowhale (34 coins)")
    transaction2 = Transaction(
        sender=student.get_address(),
        recipient=cryptowhale.get_address(),
        quantity=34
    )
    blockchain.add_block(transaction2)
    time.sleep(1)

    
    # Transaction 3 Cryptowhale - Profesor
    print("   Transaction 3: Cryptowhale -> Profesor (34 coins)")
    transaction3 = Transaction(
        sender=cryptowhale.get_address(),
        recipient=profesor.get_address(),
        quantity=34
    )
    blockchain.add_block(transaction3)
    time.sleep(2)

    
    # Validate blockchain
    print("\nValidating blockchain...")
    is_valid = blockchain.is_valid()
    print(f"   Blockchain is valid: {is_valid}")
    
    # Print blockchain
    print("\nBlockchain contents:")
    print("=" * 60)
    blockchain.print_blockchain()
    print("=" * 60)
    
if __name__ == "__main__":
    main()