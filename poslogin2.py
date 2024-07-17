import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Maskey Grocery Mart POS")
        self.root.state('zoomed')  # Fullscreen

        # Set the green background color
        self.root.configure(bg="#4CAF50")

        self.create_widgets()

    def create_widgets(self):
        # Main frame to center content
        self.main_frame = tk.Frame(self.root, bg="#E0E0E0", padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        tk.Label(self.main_frame, text="Login to Maskey Grocery Mart POS", font=("Helvetica", 28, "bold"), bg="#283747", fg="#32CD32").grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        # Username
        tk.Label(self.main_frame, text="Username", font=("Helvetica", 14), bg="#E0E0E0").grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.username_entry = tk.Entry(self.main_frame, font=("Helvetica", 14))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        # Password
        tk.Label(self.main_frame, text="Password", font=("Helvetica", 14), bg="#E0E0E0").grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.password_entry = tk.Entry(self.main_frame, show="*", font=("Helvetica", 14))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Login Button
        tk.Button(self.main_frame, text="Login", command=self.login, font=("Helvetica", 14), bg="#32CD32", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check credentials (dummy example, replace with actual authentication logic)
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.root.destroy()  # Close login window after successful login
            self.open_pos_window()  # Open the POS window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()
