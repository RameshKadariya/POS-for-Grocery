import tkinter as tk
from tkinter import messagebox, Toplevel

class POSSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Maskey Grocery Mart POS")
        self.root.state('zoomed')  # To make the window fullscreen

        self.products = []
        self.total_amount = 0.0
        self.tax_rate = 0.07

        self.create_widgets()

    def create_widgets(self):
        # Set background color for root
        self.root.configure(bg="#4D4D4D")

        # Main frame to center content
        self.main_frame = tk.Frame(self.root, bg="#E0E0E0", padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        tk.Label(self.main_frame, text="Maskey Grocery Mart POS", font=("Helvetica", 28, "bold"), bg="#283747", fg="#32CD32").grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        # Product Name
        tk.Label(self.main_frame, text="Product Name", font=("Helvetica", 14), bg="#E0E0E0").grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.product_name = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.product_name.grid(row=1, column=1, padx=10, pady=10)

        # Product Price
        tk.Label(self.main_frame, text="Product Price", font=("Helvetica", 14), bg="#E0E0E0").grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.product_price = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.product_price.grid(row=2, column=1, padx=10, pady=10)

        # Add Product Button
        tk.Button(self.main_frame, text="Add Product", command=self.add_product, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

        # Sales List
        tk.Label(self.main_frame, text="Sales", font=("Helvetica", 14, "bold"), bg="#E0E0E0").grid(row=4, column=0, columnspan=2)
        self.sales_text = tk.Text(self.main_frame, height=10, width=30, font=("Courier", 12))
        self.sales_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Cash Payment
        tk.Label(self.main_frame, text="Cash Payment", font=("Helvetica", 14), bg="#E0E0E0").grid(row=6, column=0, padx=10, pady=10, sticky='e')
        self.cash_payment = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.cash_payment.grid(row=6, column=1, padx=10, pady=10)

        # Buttons and labels frame
        self.button_frame = tk.Frame(self.main_frame, bg="#E0E0E0")
        self.button_frame.grid(row=7, column=0, columnspan=2, pady=10)

        # Calculate Total Button
        tk.Button(self.button_frame, text="Calculate Total", command=self.calculate_total, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=0, column=0, pady=10, padx=5)

        # Display Total
        self.total_label = tk.Label(self.button_frame, text="Total: $0.00", font=("Helvetica", 14), bg="#E0E0E0")
        self.total_label.grid(row=0, column=1, padx=5)

        # Print Receipt Button
        tk.Button(self.button_frame, text="Print Receipt", command=self.print_receipt, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=1, column=0, pady=10, padx=5)

        # Amount to be Returned
        self.return_amount_label = tk.Label(self.button_frame, text="Amount to be Returned: $0.00", font=("Helvetica", 14), bg="#E0E0E0")
        self.return_amount_label.grid(row=1, column=1, padx=5)

        # Reset Button
        tk.Button(self.button_frame, text="Reset", command=self.reset_system, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

    def add_product(self):
        name = self.product_name.get()
        try:
            price = float(self.product_price.get())
            self.products.append((name, price))
            self.sales_text.insert(tk.END, f"{name}: ${price:.2f}\n")
            self.product_name.delete(0, tk.END)
            self.product_price.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid price.")

    def calculate_total(self):
        self.total_amount = sum(price for _, price in self.products)
        tax_amount = self.total_amount * self.tax_rate
        grand_total = self.total_amount + tax_amount
        self.total_label.config(text=f"Total: ${grand_total:.2f}")

        try:
            cash_paid = float(self.cash_payment.get())
            return_amount = cash_paid - grand_total
            self.return_amount_label.config(text=f"Amount to be Returned: ${return_amount:.2f}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid cash amount.")

    def print_receipt(self):
        receipt_window = Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_window.state('zoomed')  # Fullscreen the receipt window
        receipt_window.configure(bg="#4D4D4D")

        receipt_frame = tk.Frame(receipt_window, bg="#E0E0E0", padx=20, pady=20)
        receipt_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Company Name
        tk.Label(receipt_frame, text="Maskey Grocery Mart", font=("Helvetica", 28, "bold"), bg="#283747", fg="#32CD32").pack(pady=20)

        receipt_text = tk.Text(receipt_frame, font=("Courier", 14), padx=20, pady=20, bg="#E0E0E0")
        receipt_text.pack(expand=True, fill='both')

        receipt = "Receipt:\n"
        receipt += "=============================\n"
        for name, price in self.products:
            receipt += f"{name}: ${price:.2f}\n"
        receipt += "=============================\n"

        subtotal = self.total_amount
        tax_amount = subtotal * self.tax_rate
        grand_total = subtotal + tax_amount

        receipt += f"\nSubtotal: ${subtotal:.2f}"
        receipt += f"\nTax: ${tax_amount:.2f}"
        receipt += f"\nGrand Total: ${grand_total:.2f}"

        try:
            cash_paid = float(self.cash_payment.get())
            return_amount = cash_paid - grand_total
            receipt += f"\nCash Paid: ${cash_paid:.2f}"
            receipt += f"\nAmount to be Returned: ${return_amount:.2f}"
        except ValueError:
            receipt += "\nCash Paid: Invalid"
            receipt += "\nAmount to be Returned: Invalid"

        receipt_text.insert(tk.END, receipt)
        receipt_text.config(state=tk.DISABLED)

        tk.Button(receipt_frame, text="Close", command=receipt_window.destroy, font=("Helvetica", 14), bg="#32CD32", fg="white").pack(pady=20)

    def reset_system(self):
        self.product_name.delete(0, tk.END)
        self.product_price.delete(0, tk.END)
        self.sales_text.delete('1.0', tk.END)
        self.cash_payment.delete(0, tk.END)
        self.total_label.config(text="Total: $0.00")
        self.return_amount_label.config(text="Amount to be Returned: $0.00")
        self.products = []
        self.total_amount = 0.0

if __name__ == "__main__":
    root = tk.Tk()
    app = POSSystem(root)
    root.mainloop()