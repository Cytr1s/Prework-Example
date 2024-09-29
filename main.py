usernames[]:
    [{'username': amidvictoriouslybird, 'type': 'Shoes', 'price': 100.0, 'total': 20},
      {'username': amidaffectionatewoot, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
      {'username': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
      {'username': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},  
      {'username': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
      {'username': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
      {'username': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
    ]

print("Hello Code2College, Welcome to Fall!")
user_name = input ("What is your name?: ")
input(f"To conclude, your name is {user_name}?: ")
if user_name == "Yes" or "yes": # Corrected line
    print("Great! Let's move forward")
elif user_name == "No" or "no":
    input("What's your name then?: ")
else:
    print("I'm sorry. That is not an answer, please try again:")

def user(age, name, user, password):
    user_input = input("How old are you?: ")
    if user_age<15:
        print("Sorry. You\'re not old enough to Enter")
    if user_age>=15<18:
        print("Welcome to Chatbot") 
    if user_age = 15<age<18:
        print("Welcome to Chatbot")

def menu():
    print("1. Create a new account ")
    print("2. Lost username or password, no worries")
    print("2. How can I assist you? ")
    print("3. Exit")

def user_selection():
    in_use = true
    user_choice == int(input("Enter the number into the system: "))
    if user_choice == 1:
        create_a_new_account()
    elif user_choice == 2:
        lost_password_or_username()
    elif user_choice == 3:
        assistance()
    elif user_choice == 4:
        exit()
        in_use == false
    else:       
         print("\nSorry, Not a Valid Choice. Please try again!")
         return in_use


    