from tracker import Tracker
def main():
    tracker = Tracker()
    print("Welcome!")
    while True:
        user_input = input("> ")
        if user_input == "quit":
            break
if __name__ == "__main__":
    main()
