# billing_app.py
import tkinter as tk
from tkinter import messagebox
from db import get_product, update_stock

def run():
    window = tk.Tk()
    window.title("Billing System")
    
    barcode_var = tk.StringVar()
    output_var = tk.StringVar()

    def search_product():
        barcode = barcode_var.get()
        product = get_product(barcode)
        if product:
            name, price, quantity = product
            output_var.set(f"{name} | Price: {price} | Stock: {quantity}")
        else:
            output_var.set("Product not found.")

    tk.Label(window, text="Scan Barcode:").pack()
    tk.Entry(window, textvariable=barcode_var).pack()
    tk.Button(window, text="Search", command=search_product).pack(pady=5)
    tk.Label(window, textvariable=output_var, fg='blue').pack()

    window.mainloop()
