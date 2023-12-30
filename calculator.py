import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget for displaying and entering numbers
        self.display_entry = tk.Entry(root, width=20, font=('Arial', 14), bd=5, insertwidth=4, justify='right')
        self.display_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # Clear button
        ]

        # Create and place buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_display = self.display_entry.get()

        if button == '=':
            try:
                result = eval(current_display)
                self.display_entry.delete(0, tk.END)
                self.display_entry.insert(tk.END, str(result))
            except Exception as e:
                self.display_entry.delete(0, tk.END)
                self.display_entry.insert(tk.END, "Error")

        elif button == 'C':
            self.display_entry.delete(0, tk.END)

        else:
            self.display_entry.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
