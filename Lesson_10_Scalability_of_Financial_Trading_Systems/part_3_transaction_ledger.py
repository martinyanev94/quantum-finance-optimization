class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def validate(self):
        return self.amount > 0  # Example validation logic

class Ledger:
    def __init__(self):
        self.chain = []

    def add_transaction(self, transaction):
        if transaction.validate():
            self.chain.append(transaction)
            print(f"Transaction from {transaction.sender} to {transaction.receiver} of amount {transaction.amount} has been added to the ledger.")
        else:
            print("Invalid transaction!")

# Managing Transactions
ledger = Ledger()
txn1 = Transaction("Trader 1", "Trader 2", 1000)
txn2 = Transaction("Trader 3", "Trader 4", -500)  # Invalid transaction

ledger.add_transaction(txn1)
ledger.add_transaction(txn2)
