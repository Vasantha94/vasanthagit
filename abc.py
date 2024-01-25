user_database = {
    "ravi": 25,
    "happy": 15,
    "ram": 30,
}

def main():
   
    user_name = input("Enter your name: ")
    
    if user_name in user_database:
        user_age = user_database[user_name]
        print(f"Hello {user_name}! Your age is {user_age}.")
        
       
        age_input = int(input("How old are you? "))
        
        if age_input >= 18:
            print("Great! You are eligible to buy alcohol.")
        else:
            
            print("Sorry, you are not eligible to buy alcohol. How about something else?")
    else:
        
        print(f"User {user_name} not found in the database.")
    
    
    print(f"Hello {user_name}, welcome!")

    
    leave_choice = input("Do you want to leave? (yes/no) ").lower()
    
    if leave_choice == "yes":
        print("Goodbye! Have a great day.")
    else:
        print("Enjoy your time!")

if __name__ == "__main__":
    main()