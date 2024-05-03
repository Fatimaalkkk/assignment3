# Importing the tkinter module and ManagementGUI class from management_system_gui module.
import tkinter as tk
from management_system_gui import ManagementGUI

# Main function to run the GUI.
def main():
    # Create a Tkinter root window.
    root = tk.Tk()
    # Instantiate the ManagementGUI class with the root window.
    app = ManagementGUI(root)
    # Run the Tkinter event loop.
    root.mainloop()

# If this script is executed directly:
if __name__ == "__main__":
    # Call the main function.
    main()
