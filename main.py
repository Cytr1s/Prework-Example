print("Hello Code2College, Welcome to Fall!")
user_name = input ("What is your name?: ")
input(f"To conclude, your name is {user_name}?: ")
if user_name == "Yes" or "yes": # Corrected line
    print("Great! Let's move forward")
if user_name == "No" or "no":
    input("What's your name then?: ")
else:
    print("I'm sorry. That is not an answer, please try again:" )
    
     