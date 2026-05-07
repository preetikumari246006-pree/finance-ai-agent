import anthropic
from tracker import Tracker

class Agent:
    def __init__(self):
        self.tracker = Tracker()
        self.messages = []
    def run(self):
        print("💸 Welcome to Finance AI Agent!")
        print("Just talk to me naturally!")
        while True:
            user_input = input("> ")
            if user_input == "quit":
                break
            self.process(user_input)
    def process(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.call_ai()
        self.messages.append({"role": "assistant", "content": response})
        self.execute(response)
    def call_ai(self):
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            system="""You are a finance tracking assistant.
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
    """,
            messages=self.messages
        )
        return response.content[0].text

    def execute(self, command):
        pass
