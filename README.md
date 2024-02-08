### Program Functionality:
1. **Menu Display**: The program starts by displaying a menu with the following options:
   - List directory contents
   - Print working directory
   - Create a new directory
   - Display a message
   - Concatenate and display content of a file
   - Exit
2. **User Input**: The user is prompted to enter a number corresponding to the action they want to perform.
3. **Action Execution**:
   - If the user selects an option from the menu, the corresponding action is executed.
   - For example, if the user selects "List directory contents," the program executes the `dir` command to list the contents of the current directory.
4. **Error Handling**: Proper error handling is implemented to handle any errors that may occur during command execution. If an error occurs, an appropriate error message is displayed to the user.
5. **Repeat Process**: After executing the selected action, the program returns to the main menu, allowing the user to choose another action or exit the program.

### Instructions for Execution:
1. **Environment**: The program is designed to run in a Windows environment due to the use of Windows shell commands (`dir`, `cd`, `mkdir`, `type`). Ensure that you are running the program on a Windows system.
2. **Code Execution**:
   - Copy the provided Python code into a text editor or an Integrated Development Environment (IDE) such as VSCode, PyCharm, or IDLE.
   - Save the file with a `.py` extension, for example, `shell_commands.py`.
   - Open a command prompt or terminal window.
3. **Navigate to Directory**: Use the `cd` command in the command prompt or terminal to navigate to the directory where you saved the Python file.
4. **Execute the Program**:
   - In the command prompt or terminal, type `python shell_commands.py` and press Enter.
   - The program will start running, and the menu will be displayed.
5. **Interact with the Program**:
   - Follow the on-screen instructions to choose a specific shell command from the menu.
   - Enter the corresponding number for the action you want to perform and press Enter.
   - The program will execute the selected command and display the output or perform the action accordingly.
6. **Repeat or Exit**:
   - After executing an action, the program will return to the main menu.
   - You can choose another action by entering the corresponding number or choose to exit the program by entering `6`.
7. **Exiting the Program**:
   - To exit the program at any time, select option `6` from the menu, and the program will terminate.

