def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            if func.__name__ == 'show_phone' and len(args[0]) != 1 :
                return "Enter user name"
            elif func.__name__ == 'add_contact' and args[0][0] in args[1] :
                return f"Contact {args[0][0]} already exist. To update contact enter 'change name phone'!"
            elif func.__name__ == 'change_contact' and args[0][0] not in args[1] :
                return f"Contact {args[0][0]} does not exist. Nothing to update!"
            elif not args[0] :
                return "There are no contacts yet!"
            else:
                return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist. Please try again!"
    return wrapper

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    
    return "Contact added."
    
@input_error   
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact updated."

@input_error
def show_phone(args, contacts) :
    name = args[0]

    return contacts[name]

@input_error    
def show_all(contacts) :
    all = ""
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