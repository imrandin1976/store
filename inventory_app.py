# inventory_app.py
import tkinter as tk
from tkinter import messagebox
from db import add_or_update_product

def run():
    window = tk.Tk()
    window.title("Inventory Updater")
    #another variable to track the window size
    print("hello")
    
    # UI Variables
    barcode_var = tk.StringVar()
    name_var = tk.StringVar()
    price_var = tk.StringVar()
    qty_var = tk.StringVar()

    # Save to DB
    def save_product():
        barcode = barcode_var.get()
        name = name_var.get()
        try:
            price = float(price_var.get())
            qty = int(qty_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Price must be a number and quantity an integer.")
            return

        if not barcode or not name:
            messagebox.showerror("Missing data", "Barcode and name are required.")
            return

        add_or_update_product(barcode, name, price, qty)
        messagebox.showinfo("Success", f"Product '{name}' saved.")
        barcode_var.set("")
        name_var.set("")
        price_var.set("")
        qty_var.set("")


    # Form UI
    tk.Label(window, text="Barcode:").pack()
    tk.Entry(window, textvariable=barcode_var).pack()

    tk.Label(window, text="Product Name:").pack()
    tk.Entry(window, textvariable=name_var).pack()

    tk.Label(window, text="Price:").pack()
    tk.Entry(window, textvariable=price_var).pack()

    tk.Label(window, text="Quantity (new stock):").pack()
    tk.Entry(window, textvariable=qty_var).pack()

    tk.Button(window, text="Save Product", command=save_product).pack(pady=10)

    window.mainloop()
