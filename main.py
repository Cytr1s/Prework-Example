print("Hello Code2College, Welcome to Fall!")
user_name = input ("What is your name?: ")
input(f"To conclude, your name is {user_name}?: ")
if user_name == "Yes" or "yes": # Corrected line
    print("Great! Let's move forward")
elif user_name == "No" or "no":
    input("What's your name then?: ")
else:
    print("I'm sorry. That is not an answer, please try again:")

def assistance():
      print("\n **GenZ STORE INVENTORY SYSTEM**")  
        print("1. View Store Inventory ") 
        print("2. Add A New Product")   
        print("3. Remove Products")  
        print("4. Exit\n")  