import tkinter as tk
import json
import tkinter.messagebox as messagebox

class Display(tk.Tk):
    def __init__(self, root, main_app):
        self.root = root
        self.main = main_app

        # Load existing pacemakers from pacemaker_data.json
        self.existing_pacemakers = self.load_existing_pacemakers()

        # Create a dropdown menu to select an existing pacemaker
        self.selected_pacemaker = tk.StringVar(root)
        self.pacemaker_dropdown = tk.OptionMenu(root, self.selected_pacemaker, *self.existing_pacemakers)
        self.pacemaker_dropdown.config(bg="blue", fg="white")
        self.pacemaker_dropdown["menu"].config(bg="blue", fg = 'white')
        self.pacemaker_dropdown.place(x=100,y=60)

        # Create a button to display parameters
        self.display_button = tk.Button(root, text="Display", font=("Inter", 10, 'bold'), fg='white', bg='green', cursor='hand2', command=self.display_parameters)
        self.display_button.place(x=200, y=60)

        self.log_out = tk.Button(root, width='10', border=2, text="Log Out", font=("Inter", 10, 'bold'), fg='white', bg='red', cursor='hand2', command=lambda: self.main.route(self.main.login_frame))
        self.log_out.place(x=1000, y=30)

        self.back_button = tk.Button(root, text="Back", width='10', border=2, font=("Inter", 10, 'bold'), fg='white', bg='black', cursor='hand2', command=lambda: self.main.route(self.main.mode_sel))
        self.back_button.place(x=900, y=30)



        # Create a label to display parameters
        self.label1 = tk.Label(root, text="Please Choose a Pacemaker in order to view past data", font=("Inter", 10, 'bold'), fg='black', bg='#F5E8B7')
        self.label1.place(x=100, y=30)
        self.label2 = tk.Label(root, text="Your data will appear below :", font=("Inter", 10, 'bold'), fg='black', bg='#F5E8B7')
        self.label2.place(x=100, y=150)
        self.label3 = tk.Label(root, text="", font=("Inter", 10), fg='black', bg='#F5E8B7')
        self.label3.place(x=100, y=200)
        self.label3.config(wraplength=1000)

    def load_existing_pacemakers(self):
        # Load existing pacemakers from pacemaker_data.json
        try:
            with open("DCM/DataStorage/pacemaker_data.json", "r") as file:
                json_data = json.load(file)
            # Get the list of pacemakers from the JSON data
            pacemakers = list(json_data.keys())
            return pacemakers
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Return an empty list if there's an issue with the JSON file
            return []

    def display_parameters(self):
        # Get the selected pacemaker
        selected_pacemaker = self.selected_pacemaker.get()
        if not selected_pacemaker:
            return  # No pacemaker selected

        # Load existing pacemakers from pacemaker_data.json
        try:
            with open("DCM/DataStorage/pacemaker_data.json", "r") as file:
                json_data = json.load(file)
            # Get the parameters for the selected pacemaker
            parameters = json_data.get(selected_pacemaker, {})
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            parameters = {}  # Set parameters as an empty dictionary if there's an issue with the JSON file

        # Display the parameters in the label
        self.label3.config(text=f"{parameters}")