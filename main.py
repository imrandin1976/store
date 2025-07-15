import tkinter as tk
from tkinter import messagebox
from db import init_db
import billing_app
import inventory_app

def launch_billing():
    billing_app.run()

def launch_inventory():
    inventory_app.run()

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    root.title("Store Management")
    tk.Button(root, text="Start Billing", width=25, command=launch_billing).pack(pady=20)
    tk.Button(root, text="Update Inventory", width=25, command=launch_inventory).pack(pady=20)
    root.mainloop()
