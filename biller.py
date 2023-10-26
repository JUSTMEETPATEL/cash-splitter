import tkinter as tk
import tkinter.ttk as ttk
import json

class SplitBillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Split Bill App")
        self.root.geometry("400x400")  # Set the initial window size

        # Set a lively background color
        self.root.configure(bg="lightblue")  # You can change "lightblue" to any color you prefer

        # Create variables to store data
        self.data = []

        # Create and configure the main frame
        self.main_frame = ttk.Frame(root, style="Main.TFrame")
        self.main_frame.grid(column=0, row=0, padx=20, pady=20)

        # Style settings
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", foreground="black", background="black")  # Change both text and button color to black
        style.configure("TLabel", padding=10, background="lightgray")
        style.configure("Main.TFrame", background="lightblue")  # Background color for the main frame

        # Create and configure the input fields
        ttk.Label(self.main_frame, text="Name:", style="TLabel").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Label(self.main_frame, text="Item:", style="TLabel").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.item_entry = ttk.Entry(self.main_frame)
        self.item_entry.grid(row=1, column=1, padx=10, pady=10)
        
        ttk.Label(self.main_frame, text="Price:", style="TLabel").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.price_entry = ttk.Entry(self.main_frame)
        self.price_entry.grid(row=0, column=3, padx=10, pady=10)

        ttk.Label(self.main_frame, text="Quantity:", style="TLabel").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.quantity_entry = ttk.Entry(self.main_frame)
        self.quantity_entry.grid(row=1, column=3, padx=10, pady=10)

        # Create buttons with custom style
        ttk.Button(self.main_frame, text="Add Item", style="TButton", command=self.add_item).grid(row=2, column=0, columnspan=4, padx=10, pady=20)
        ttk.Button(self.main_frame, text="Calculate Total", style="TButton", command=self.calculate_total).grid(row=3, column=0, columnspan=4, padx=10, pady=20)

        # Create and configure the results Label
        self.result_label = ttk.Label(self.main_frame, text="", style="TLabel")
        self.result_label.grid(row=4, column=0, padx=10, pady=10, columnspan=4, sticky="w")

        # Create and configure the saved data label
        self.saved_data_label = ttk.Label(self.main_frame, text="", style="TLabel")
        self.saved_data_label.grid(row=5, column=0, padx=10, pady=10, columnspan=4, sticky="w")

        # Create and configure the save and load buttons with custom style
        ttk.Button(self.main_frame, text="Save Data", style="TButton", command=self.save_data).grid(row=6, column=0, padx=10, pady=20)
        ttk.Button(self.main_frame, text="Load Data", style="TButton", command=self.load_data).grid(row=6, column=1, padx=10, pady=20)

    def add_item(self):
        name = self.name_entry.get()
        item = self.item_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        self.data.append({
            "Name": name,
            "Item": item,
            "Price": price,
            "Quantity": quantity
        })

        self.clear_input_fields()
        self.calculate_total()

    def clear_input_fields(self):
        self.name_entry.delete(0, 'end')
        self.item_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')

    def calculate_total(self):
        total_str = "Details:\n"
        total_str += f"{'Name':<15}{'Item':<25}{'Price':<15}{'Quantity':<15}{'Total':<15}\n"

        for entry in self.data:
            total = entry["Price"] * entry["Quantity"]
            total_str += f"{entry['Name']:<15}{entry['Item']:<25}{entry['Price']:<15.2f}{entry['Quantity']:<15}{total:<15.2f}\n"

        self.result_label.config(text=total_str)

    def save_data(self):
        with open("split_bill_data.json", "w") as file:
            json.dump(self.data, file)
        self.saved_data_label.config(text="Data saved to split_bill_data.json", style="TLabel.Success")

    def load_data(self):
        try:
            with open("split_bill_data.json", "r") as file:
                self.data = json.load(file)
            self.calculate_total()
            self.saved_data_label.config(text="Data loaded from split_bill_data.json", style="TLabel.Success")
        except FileNotFoundError:
            self.saved_data_label.config(text="No data file found.", style="TLabel.Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = SplitBillApp(root)
    root.mainloop()
