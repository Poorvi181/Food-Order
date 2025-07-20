import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.configure(bg='red')

tk.Label(win, text="Email", bg='red').pack()
tk.Entry(win).pack()

tk.Label(win, text="Password", bg='red').pack()
tk.Entry(win, show='*').pack()

tk.Label(win, text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich? or None", bg='red').pack()
ttk.Combobox(win, values=["Chicken sandwich", "B.L.T", "Veg sandwich", "None"]).pack()

tk.Label(win, text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?", bg='red').pack()
ttk.Combobox(win, values=["Cola", "Fanta", "Orange Juice", "Water", "None"]).pack()

tk.Label(win, text="What dessert would you like: An Ice Cream, an Ice Lolly or a Chocolate Cake or None?", bg='red').pack()
ttk.Combobox(win, values=["Ice Cream", "Ice Lolly", "Chocolate Cake", "None"]).pack()

tk.Button(win, text="Submit Order").pack(pady=10)

win.mainloop()
