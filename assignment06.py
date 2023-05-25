# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,Created started script
# Rohini Nawale,25/05/2023 ,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processor (Business Logic) ----------------------------------------------- #
class Processor:
    """Performs processing tasks"""

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """Read data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) to read data into
        :return: (list) of dictionary rows
        """
        try:
            file = open(file_name, "r")
            for line in file:
                task, priority = line.strip().split(",")
                list_of_rows.append({"Task": task, "Priority": priority})
            file.close()
            status = "Success"
        except FileNotFoundError:
            status = "File not found"
        except Exception as e:
            status = str(e)
        return list_of_rows, status

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """Add a new task and priority to the list of dictionary rows

        :param task: (string) with task description
        :param priority: (string) with task priority
        :param list_of_rows: (list) to add data to
        :return: (list) of dictionary rows
        """
        list_of_rows.append({"Task": task, "Priority": priority})
        return list_of_rows, "Success"

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """Remove a task from the list of dictionary rows

        :param task: (string) with task description
        :param list_of_rows: (list) to remove data from
        :return: (list) of dictionary rows
        """
        list_of_rows = [row for row in list_of_rows if row["Task"] != task]
        return list_of_rows, "Success"

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """Write data from the list of dictionary rows to a file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) to write data from
        :return: (list) of dictionary rows
        """
        try:
            file = open(file_name, "w")
            for row in list_of_rows:
                file.write(f"{row['Task']},{row['Priority']}\n")
            file.close()
            status = "Success"
        except Exception as e:
            status = str(e)
        return list_of_rows, status


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input and output tasks"""

    @staticmethod
    def print_menu_tasks():
        """Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """Shows the current Tasks in the list of dictionary rows

        :param list_of_rows: (list) of dictionary rows
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(f"{row['Task']} ({row['Priority']})")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """Gets a yes or no choice from the user

        :param message: (string) prompt message
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=""):
        """Pause program and show a message before continuing

        :param optional_message: (string) optional message to display
        :return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")

    @staticmethod
    def input_new_task_and_priority():
        """Gets user input for a new task and priority

        :return: (string, string) task and priority
        """
        task = input("Enter a task: ")
        priority = input("Enter a priority: ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """Gets user input for a task to remove

        :return: string
        """
        task = input("Enter a task to be removed: ")
        return task


# Main Body of Script  ------------------------------------------------------ #

# Data
strFileName = "ToDoList.txt"
lstTable = []
strChoice = ""

# Step 1 - When the program starts, load data from a file
lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 - Show current data
    IO.print_current_tasks_in_list(lstTable)
    IO.print_menu_tasks()
    strChoice = IO.input_menu_choice()

    # Step 4 - Process user's menu choice
    if strChoice == "1":  # Add a new Task
        lstTable, strStatus = Processor.add_data_to_list(*IO.input_new_task_and_priority(), lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == "2":  # Remove an existing Task
        lstTable, strStatus = Processor.remove_data_from_list(IO.input_task_to_remove(), lstTable)
        IO.input_press_to_continue(strStatus)

    elif strChoice == "3":  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")

    elif strChoice == "4":  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) - ")
        if strChoice == "y":
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")

    elif strChoice == "5":  # Exit Program
        print("Goodbye!")
        break  # Exit the loop

    else:
        print(f"You entered {strChoice}, but this is not a valid option.")
        IO.input_press_to_continue
