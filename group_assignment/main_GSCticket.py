import tkinter as tk
from tkinter import ttk
import subprocess


class RootApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("GSC Ticket Booking")
        self.root.geometry("300x200")
        self.root.configure(background="#88AB8E")

       

        welcome_label = tk.Label(root, text='WELCOME TO THE GSC', font=("Times New Romans", 9, "bold"), bg="#88AB8E")
        welcome_label.pack()

        registration_button = tk.Button(root, text="User Registration", command=self.on_register_click, bg="#EEE7DA")
        registration_button.pack(pady=10)

        showtime_button = tk.Button(root, text="Showtime", command=self.on_showtime_click, bg="#EEE7DA")
        showtime_button.pack(pady=10)

        seat_button = tk.Button(root, text="Select Seat", command=self.on_select_seat_click, bg="#EEE7DA")
        seat_button.pack(pady=10)


        

    def on_register_click(self):
        subprocess.run(["python", "registration_module.py"])

    def on_showtime_click(self):
        subprocess.run(["python", "showtime_movie.py"])

    def on_select_seat_click(self):
        subprocess.run(["python", "reserve_seat.py"])


       
    

if __name__ == "__main__":
    root = tk.Tk()
    app = RootApp(root)
    root.mainloop()
