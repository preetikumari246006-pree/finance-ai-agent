from storage import Storage
class Tracker:
    def __init__(self):
        self.storage = Storage()
        self.data = self.storage.load_data()
      
    def add_expense(self, amount, category, description):
        transaction = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": description
        }
        
        self.data["transactions"].append(transaction)
        self.storage.save_data(self.data)
        
    def add_income(self, amount, description):
        transaction = {
            "type": "income",
            "amount": amount,
            "description": description
        }
        self.data["transactions"].append(transaction)
        self.storage.save_data(self.data)
        
    def view_transactions(self):
        for transaction in self.data["transactions"]:
            print(f"Type: {transaction['type']} | Amount: {transaction['amount']} | Category: {transaction.get('category', 'N/A')} | Description: {transaction['description']}")

    
    def get_summary(self):
        total_income = 0
        total_expenses = 0
        for transaction in self.data["transactions"]:
            if transaction["type"] == "income":
                total_income += transaction["amount"]
            else:
                total_expenses += transaction["amount"]
        balance = total_income - total_expenses
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Balance: {balance}")
                
