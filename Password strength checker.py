import sys

def check_password_strength(password: str) -> str:
    """
    Evaluates password strength using O(n) linear scan logic.
    """

    if len(password) < 8:
        return "Weak"

 
    has_uppercase = any(char.isupper() for char in password)
    has_digit     = any(char.isdigit() for char in password)

    has_symbol    = any(not char.isalnum() and not char.isspace() for char in password)


    conditions_met = sum([has_uppercase, has_digit, has_symbol])

    if conditions_met == 3:
        return "Strong"
    elif conditions_met == 2:
        return "Medium"
    else:
        return "Weak"


def main():
  
    print("Type 'exit' or 'quit' to terminate the program.\n")

    while True:
        try:
           
            user_password = input("Enter a password to evaluate: ").strip()
            
          
            if user_password.lower() in ['exit', 'quit']:
                print("\nExiting analyst module. Secure checkpoint closed.")
                break
                
            if not user_password:
                print("[-] Input cannot be empty. Please try again.\n")
                continue

            category = check_password_strength(user_password)
    
            print(f"[>] Result: The password falls into the [{category.upper()}] category.")
            print("-" * 50 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n[-] Interrupted. Exiting safely.")
            sys.exit(0)

if __name__ == "__main__":
    main()