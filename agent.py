from groq import Groq
from tracker import Tracker
from dotenv import load_dotenv
import os

load_dotenv()

class Agent:
    def __init__(self):
        self.tracker = Tracker()
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.system = """You are a finance tracking assistant.
Extract the intent and reply with ONLY one of these commands:
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
        print(f"🤖 Agent: {response}")
        self.execute(response)

    def call_ai(self, user_input):
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()

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
            print("❌ Sorry I didn't understand!")
