from storage import Storage
class Tracker:
    def __init__(self):
        self.storage = Storage()
        self.data = self.storage.load_data()
      
    def add_expense(self, amount, category, description):
        pass
    
    def add_income(self, amount, description):
        pass
    
    def view_transactions(self):
        pass
    
    def get_summary(self):
        pass
