import subprocess

# Function to list directory contents
def list_directory_contents():
    try:
        subprocess.run(["dir"], shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to list directory contents.")

# Function to print working directory
def print_working_directory():
    try:
        subprocess.run(["cd"], shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to print working directory.")

# Function to create a new directory
def create_new_directory():
    directory_name = input("Enter the name of the new directory: ")
    try:
        subprocess.run(["mkdir", directory_name], shell=True, check=True)
        print(f"Directory '{directory_name}' created successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to create directory.")

# Function to display a message
def display_message():
    message = input("Enter the message to display: ")
    print("Message:", message)

# Function to display file contents
def display_file_contents():
    file_name = input("Enter the name of the file to display: ")
    try:
        subprocess.run(["type", file_name], shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to display file contents.")

# Main function to display menu and handle user input
def main():
    while True:
        print("\nMenu:")
        print("1. List directory contents")
        print("2. Print working directory")
        print("3. Create a new directory")
        print("4. Display a message")
        print("5. Concatenate and display content of a file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_directory_contents()
        elif choice == "2":
            print_working_directory()
        elif choice == "3":
            create_new_directory()
        elif choice == "4":
            display_message()
        elif choice == "5":
            display_file_contents()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number from the menu.")

# Entry point of the program
if __name__ == "__main__":
    main()

