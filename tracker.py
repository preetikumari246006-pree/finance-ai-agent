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
        pass
    
    def get_summary(self):
        pass
