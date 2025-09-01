class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Prompt the user for a valid positive amount.
    
    Parameters:
    prompt (str): The message to display to the user
    
    Returns:
    float: Valid positive amount entered by the user
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 100 or 50.25).")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower().strip()
        
        if action == 'exit':
            print("Thank you for using the checkbook program. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()