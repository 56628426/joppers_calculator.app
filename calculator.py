# creating simple calculator using tkinter
# importing the required libraries
import tkinter as tk
from tkinter import messagebox


# creating a class for the calculator
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator Joppers mw")
        self.master.geometry("310x490")  # Made slightly taller for the extra row
        self.master.resizable(0, 0)

        # creating the display for the calculator
        self.display = tk.Entry(self.master, width=16, font=("Arial", 24), bd=10, insertwidth=2, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # creating buttons for the calculator
        self.create_buttons()

    def create_buttons(self):
        # creating number buttons and operation buttons
        button_texts = [
            'C', '←', '%', '/',  # Added Clear (C) and Backspace (←) buttons
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '00', '0', '.', '='
        ]

        row_val = 1
        col_val = 0
        for text in button_texts:
            button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            
            # Make the equals button span two columns
            if text == '=':
                button.grid(row=row_val, column=col_val)
            else:
                button.grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                # Check if the expression is valid before evaluating
                current_text = self.display.get()
                if current_text.endswith(('+', '-', '*', '/', '%')):
                    messagebox.showinfo("Warning", "Please complete the expression")
                    return
                
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {str(e)}")
                self.display.delete(0, tk.END)
        elif char == 'C':
            # Clear the display
            self.display.delete(0, tk.END)
        elif char == '←':
            # Backspace functionality
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text[:-1])
        elif char == '%':
            # Implement percentage
            try:
                current_value = float(self.display.get())
                result = current_value / 100
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input for Percentage")
                self.display.delete(0, tk.END)
        else:
            current_text = self.display.get()
            new_text = current_text + char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, new_text)


if __name__ == "__main__":  
    root = tk.Tk()  
    calc = Calculator(root)  
    root.mainloop()
