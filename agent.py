import google.generativeai as genai
from tracker import Tracker

class Agent:
    def __init__(self):
        self.tracker = Tracker()
        genai.configure(api_key="")
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="""You are a finance tracking assistant.
Extract the intent from user message and reply with ONLY one of these commands:
- ADD_EXPENSE amount category description
- ADD_INCOME amount description
- VIEW_TRANSACTIONS
- GET_SUMMARY
- UNKNOWN

Examples:
User: I spent 500 on food → ADD_EXPENSE 500 food groceries
User: earned 10000 salary → ADD_INCOME 10000 salary
User: show transactions → VIEW_TRANSACTIONS
User: get summary → GET_SUMMARY"""
        )
        self.chat = self.model.start_chat()

    def run(self):
        print("💸 Welcome to Finance AI Agent!")
        print("Just talk to me naturally!")
        while True:
            user_input = input("> ")
            if user_input == "quit":
                break
            self.process(user_input)

    def process(self, user_input):
        response = self.call_ai(user_input)
        self.execute(response)

    def call_ai(self, user_input):
        response = self.chat.send_message(user_input)
        return response.text

    def execute(self, command):
        parts = command.strip().split()
        action = parts[0]
        if action == "ADD_EXPENSE":
            self.tracker.add_expense(float(parts[1]), parts[2], parts[3])
            print("✅ Expense added!")
        elif action == "ADD_INCOME":
            self.tracker.add_income(float(parts[1]), parts[2])
            print("✅ Income added!")
        elif action == "VIEW_TRANSACTIONS":
            self.tracker.view_transactions()
        elif action == "GET_SUMMARY":
            self.tracker.get_summary()
        else:
            print("❌ Sorry I didn't understand that!")
