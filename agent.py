from tracker import Tracker
import os

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
        pass

    def execute(self, command):
        pass
