import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora GUI")
        self.display = tk.Entry(root, width=25, font=("Arial", 16), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4)
        self.current_expression = ""
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 16),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
        clear_button = tk.Button(self.root, text='C', width=5, height=2, font=("Arial", 16),
                                 command=self.clear_display)
        clear_button.grid(row=4, column=0, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            self.calculate_expression()
        else:
            self.current_expression += str(char)
            self.update_display()

    def clear_display(self):
        self.current_expression = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)

    def calculate_expression(self):
        try:
            result = eval(self.current_expression)
            self.current_expression = str(result)
            self.update_display()
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculadora(root)
    root.mainloop()
