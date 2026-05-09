import json

class Storage:
    def __init__(self):
        self.file = "data/expenses.json"
    def load_data(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"transactions": [], "balance": 0}
        
    def save_data(self, expenses):
        try:
            with open(self.file, "w") as f:
                json.dump(expenses, f)
        except Exception as e:
            print(f"❌ Could not save data: {e}")
