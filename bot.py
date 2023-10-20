def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2 :
        return "Please enter name and phone number!"
    else :
        name, phone = args

    if name in contacts.keys() :
        return f"Contact {name} already exist. Please try again!"
    else :
        contacts[name] = phone
        return "Contact added."
    
def change_contact(args, contacts):
    if len(args) != 2 :
        return "Please enter name and phone number!"
    else :
        name, phone = args
    
    if name not in contacts.keys() :
        return f"Contact {name} does not exist. Please try again!"
    else :
        contacts[name] = phone
        return "Contact updated."

def show_phone(args, contacts) :
    if len(args) != 1 :
        return "Please enter only name!"
    else :
        name = args[0]

    if name not in contacts.keys() :
        return f"Contact {name} does not exist. Please try again!"
    else :
        return contacts[name]
    
def show_all(contacts) :
    all = ""
    if not contacts :
        return "There are no contacts yet!"
    else :
        for k, v in contacts.items() :
            all += f"{k} {v}\n"
    return all.rstrip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()