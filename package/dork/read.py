
import os
def display_file_lines(filename):
    # Determine the directory containing the read.py script
    script_directory = os.path.dirname(os.getcwd())

    # Specify the relative path to the directory where the text files are located
    text_files_directory = 'webwizard/package/dork/'

    # Construct the full file path by joining the script directory and the text files directory
    file_path = os.path.join(script_directory, text_files_directory, filename) 
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)
            current_line = 0

            while current_line < total_lines:
                for i in range(10):
                    if current_line < total_lines:
                        print(lines[current_line], end='')
                        current_line += 1
                    else:
                        break

                user_input = input("\nDo you want to continue printing? (y/n): ")
                if user_input.lower() != 'y':
                    break

                if user_input.lower() == 'n':
                    break
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_file(choice):
    file_mapping = {
        1: "dork_500.txt",
        2: "dork_1k.txt",
        3: "dork_2k.txt",
        4: "dork_3k.txt",
        5: "dork_4k.txt",
    }
    
    
    if choice in file_mapping:
        filename = file_mapping[choice]
        display_file_lines(filename)
    else:
        print("Invalid choice. Please select a valid option (1, 2, 3, 4, 5).")

#if __name__ == "__main__":
def dorkshow():
    while True:
        print("Select a file:")
        print("1. dork_500")
        print("2. dork_1k")
        print("3. dork_2k")
        print("4. dork_3k")
        print("5. dork_4k")
        print("0. Spider...")
        
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        elif choice.isdigit():
            choice = int(choice)
            select_file(choice)
        else:
            print("Invalid input. Please enter a number.")

