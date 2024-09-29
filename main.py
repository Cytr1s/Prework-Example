print("Hello Code2College, Welcome to Fall!")
user_name = input ("What is your name?: ")
input(f"To conclude, your name is {user_name}?: ")
if user_name == "Yes" or "yes": # Corrected line
    print("Great! Let's move forward")
elif user_name == "No" or "no":
    input("What's your name then?: ")
else:
    print("I'm sorry. That is not an answer, please try again:")

def menu():
    print("1. Create a new account ")
    print("2. Lost username or password, no worries")
    print("2. How can I assist you? ")
    print("3. Exit")

def user_selection():
    in_use = true
    if user_choice == input("Enter the number into the system")