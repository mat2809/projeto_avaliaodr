import tkinter as tk
from app.views.login_view import LoginView

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
