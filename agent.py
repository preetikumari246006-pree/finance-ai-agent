from google import genai
from tracker import Tracker

class Agent:
    def __init__(self):
        self.tracker = Tracker()
        self.client = genai.Client(api_key="AIzaSyCNwc0If1fymnEtoGKNOvO9n2BM3VYeRx8")
        self.history = []
        self.system = """You are a finance tracking assistant.
Extract the intent and reply with ONLY one of these commands:
- ADD_EXPENSE amount category description
- ADD_INCOME amount description
- VIEW_TRANSACTIONS
- GET_SUMMARY
- UNKNOWN"""

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
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=self.system + "\nUser: " + user_input
        )
        return response.text.strip()

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
