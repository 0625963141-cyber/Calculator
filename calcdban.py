import tkinter as tk
from tkinter import PhotoImage
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Définir une icône personnalisée
        self.master.iconphoto(False, PhotoImage(file='images/calc.png'))

        self.expression = ""

        # Zone d'affichage
        self.display = tk.Entry(master, font=('Arial', 20), bd=10, insertwidth=2, width=16, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=6)

        # Boutons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'sqrt',
            '(', ')', 'C', 'pi',
            'Vol C', 'Vol S', 'Area R', 'Area C', 
            'K to C', 'C to K', 'C to F', 'F to C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 15),
                      command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression.replace('pi', str(math.pi))))
            except Exception:
                self.expression = "Erreur"
        elif char in ['sin', 'cos', 'tan', 'sqrt']:
            try:
                if char == 'sin':
                    self.expression = str(math.sin(math.radians(float(self.expression))))
                elif char == 'cos':
                    self.expression = str(math.cos(math.radians(float(self.expression))))
                elif char == 'tan':
                    self.expression = str(math.tan(math.radians(float(self.expression))))
                elif char == 'sqrt':
                    self.expression = str(math.sqrt(float(self.expression)))
            except Exception:
                self.expression = "Erreur"
        elif char == 'Vol C':
            self.calculate_volume_cylinder()
        elif char == 'Vol S':
            self.calculate_volume_sphere()
        elif char == 'Area R':
            self.calculate_area_rectangle()
        elif char == 'Area C':
            self.calculate_area_circle()
        elif char == 'K to C':
            self.convert_k_to_c()
        elif char == 'C to K':
            self.convert_c_to_k()
        elif char == 'C to F':
            self.convert_c_to_f()
        elif char == 'F to C':
            self.convert_f_to_c()
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
