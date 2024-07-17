import tkinter as tk
from tkinter import messagebox


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Maskey Grocery Mart POS")
        self.root.state('zoomed')  # Fullscreen

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="#2E4053")

        # Main frame to center content
        self.main_frame = tk.Frame(self.root, bg="#F4F6F7", padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        tk.Label(self.main_frame, text="Login to Maskey Grocery Mart POS", font=("Arial", 28, "bold"), bg="#1E3D59", fg="white").grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        # Username
        tk.Label(self.main_frame, text="Username", font=("Arial", 14), bg="#F4F6F7").grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.username_entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        # Password
        tk.Label(self.main_frame, text="Password", font=("Arial", 14), bg="#F4F6F7").grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.password_entry = tk.Entry(self.main_frame, show="*", font=("Arial", 14))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        # Login Button
        tk.Button(self.main_frame, text="Login", command=self.login, font=("Arial", 14), bg="#1E3D59", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check credentials (dummy example, replace with actual authentication logic)
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.root.destroy()  # Close login window after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()
