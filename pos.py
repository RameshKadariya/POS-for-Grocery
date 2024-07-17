import tkinter as tk
from tkinter import messagebox, Toplevel
from datetime import datetime

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
        self.root.configure(bg="#4CAF50")

        # Main frame to center content
        self.main_frame = tk.Frame(self.root, bg="#E0E0E0", padx=20, pady=20)
        self.main_frame.pack(pady=50)  # Adjust pady for vertical positioning

        # Title and Date/Time
        tk.Label(self.main_frame, text="Maskey Grocery Mart POS", font=("Helvetica", 28, "bold"), bg="#283747", fg="#32CD32").grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky="ew")
        self.date_label = tk.Label(self.main_frame, text="", font=("Helvetica", 14), bg="#E0E0E0")
        self.date_label.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")
        self.update_datetime()  # Call to update date/time label

        # Product Name
        tk.Label(self.main_frame, text="Product Name", font=("Helvetica", 14), bg="#E0E0E0").grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.product_name = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.product_name.grid(row=2, column=1, padx=10, pady=10)

        # Product Price
        tk.Label(self.main_frame, text="Product Price", font=("Helvetica", 14), bg="#E0E0E0").grid(row=2, column=2, padx=10, pady=10, sticky='e')  # Adjusted column position
        self.product_price = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.product_price.grid(row=2, column=3, padx=10, pady=10)  # Adjusted column position

        # Add Product Button
        tk.Button(self.main_frame, text="Add Product", command=self.add_product, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=2, column=4, padx=10, pady=10)  # Adjusted column position

        # Sales List
        tk.Label(self.main_frame, text="Sales", font=("Helvetica", 14, "bold"), bg="#E0E0E0").grid(row=3, column=0, columnspan=5, pady=10)
        self.sales_text = tk.Text(self.main_frame, height=10, width=60, font=("Courier", 12))
        self.sales_text.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

        # Cash Payment
        tk.Label(self.main_frame, text="Cash Payment", font=("Helvetica", 14), bg="#E0E0E0").grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.cash_payment = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.cash_payment.grid(row=5, column=1, padx=10, pady=10)

        # Calculate Total Button
        tk.Button(self.main_frame, text="Calculate Total", command=self.calculate_total, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=5, column=2, padx=10, pady=10)

        # Display Total
        self.total_label = tk.Label(self.main_frame, text="Total: $0.00", font=("Helvetica", 14), bg="#E0E0E0")
        self.total_label.grid(row=5, column=3, padx=10, pady=10)

        # Print Receipt Button
        tk.Button(self.main_frame, text="Print Receipt", command=self.print_receipt, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=5, column=4, padx=10, pady=10)

        # Amount to be Returned
        self.return_amount_label = tk.Label(self.main_frame, text="Amount to be Returned: $0.00", font=("Helvetica", 14), bg="#E0E0E0")
        self.return_amount_label.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

        # Reset Button
        tk.Button(self.main_frame, text="Reset", command=self.reset_system, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=7, column=0, columnspan=5, pady=10)

    def update_datetime(self):
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y %H:%M:%S")
        self.date_label.config(text=date_str)
        self.root.after(1000, self.update_datetime)  # Update every second

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
        receipt_frame.pack(pady=50)

        # Company Name and Date/Time
        tk.Label(receipt_frame, text="Maskey Grocery Mart", font=("Helvetica", 28, "bold"), bg="#283747", fg="#32CD32").pack(pady=20)
        receipt_date_label = tk.Label(receipt_frame, text="", font=("Helvetica", 14), bg="#E0E0E0")
        receipt_date_label.pack(pady=5)
        self.update_receipt_datetime(receipt_date_label)  # Call to update receipt date/time label

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

    def update_receipt_datetime(self, label):
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y %H:%M:%S")
        label.config(text=date_str)

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

