from tracker import Tracker

def main():
    tracker = Tracker()
    print("Welcome!")
    while True:
        user_input = input("> ")
        parts = user_input.split()
        
        if user_input == "quit":
            break
        elif user_input == "view":
            tracker.view_transactions()
        elif user_input == "summary":
            tracker.get_summary()
        elif parts[0] == "expense":
            amount = float(parts[1])
            category = parts[2]
            description = parts[3]
            tracker.add_expense(amount, category, description)
        elif parts[0] == "income":
            amount = float(parts[1])
            description = parts[2]
            tracker.add_income(amount, description)

if __name__ == "__main__":
    main()
