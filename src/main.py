import sys
from translate import translate

def get_user_choice(language_code: str, project_path: str, output_file_path: str):
    
    print("Please choose an option:")
    print(f"1. Set language code\tCurrent: {language_code}")
    print(f"2. Set project path\tCurrent: {project_path}")
    print(f"3. Set output file path\tCurrent: {output_file_path}")
    print(f"4. Translate")
    print("5. Exit")
    
    # Get user input and validate it
    while True:
        user_input = input("\nEnter your choice (1-5) >> ")
        if user_input.isdigit() and int(user_input) in range(1, 6):
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Main function to run the program
def main():
    
    language_code = "not set"
    output_file_path = "not set"
    project_path = "not set"
    
    print("\nWelcome to SwiftLocalizationGenerator\n\n")
    
    while True:
        # Display the menu and get user input
        choice = get_user_choice(language_code=language_code, project_path=project_path, output_file_path=output_file_path)
        
        # Call the appropriate function based on the user's choice
        if choice == 1:
            language_code = input(">> ")
        elif choice == 2:
            project_path = input(">> ")
        elif choice == 3:
            output_file_path = input(">> ")
        elif choice == 4:
            translate(project_path, language_code, output_file_path)
        else:
            # Exit the program
            print("Exiting...")
            sys.exit()

# Call the main function to run the program
if __name__ == "__main__":
    main()
