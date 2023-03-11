# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 01:07:55 2023

@author: user1
"""

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=30, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(master, text=button, width=5, height=2, command=command).grid(row=row, column=col, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif key == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, key)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
