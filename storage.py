import json

class Storage:
    def __init__(self):
        self.file = "data/expenses.json"
    def load_data(self):
        with open(self.file, "r") as f:
            return json.load(f)
        
    def save_data(self, expenses):
        with open(self.file, "w") as f:
            json.dump(expenses, f)
