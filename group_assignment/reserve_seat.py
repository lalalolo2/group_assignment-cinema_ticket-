# Import the required libraries
import tkinter 
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gsc_ticket"
    )


mycursor = mydb.cursor()

root = tkinter.Tk()
root.title("Selected Seat")
root.configure(background="#88AB8E")


class Reserve_seat(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.my_img = None
        self.pack()
        self.create_widgets()

    def calculate_total(self):
        quantity_adult = int(self.adult_quantity_box.get())
        adult_prices= quantity_adult * 40

        children= int(self.children_quantity_box.get())

        if children > 1:
            child_prices= children * 20
            total_price= (adult_prices + child_prices)

        else:
            total_price= (adult_prices)

        self.total_output_label.config(text=f"Total Price: RM {total_price}")

    def save_data(self):
        reserve_seat = self.type_of_seat_combo.get()
        quantity_adult = int(self.adult_quantity_box.get())
        quantity_children = int(self.children_quantity_box.get())

        self.calculate_total()

        # To insert data into database, modify the following lines:
        sql = "INSERT INTO customer_seat_cinema (reserve_seat, quantity_of_adult , quantity_of_children, total_price) VALUES (%s, %s, %s, %s)"
        val = (self.type_of_seat_combo.get(), self.adult_quantity_box.get(), self.children_quantity_box.get(), self.total_output_label.cget("text"))

        mycursor.execute(sql, val)
        mydb.commit()


    def create_widgets(self):

        image=Image.open('icing_noyen.jpg')
        img=image.resize((350, 250))
        self.my_img=ImageTk.PhotoImage(img)
        label=Label(self.root, image=self.my_img)
        label.pack()

        self.frame= tkinter.Frame(self.root, bg="#88AB8E")
        self.frame.pack()

        self.reserve_seat_frame =tkinter.LabelFrame(self.frame, text="Seat on Cinema", bg="#88AB8E")
        self.reserve_seat_frame.grid(row= 1, column=0, padx=20, pady=20)


        self.reserve_seat_label= tkinter.Label(self.reserve_seat_frame, text="Reserve Seat", bg="#88AB8E")
        self.reserve_seat_label.grid(row=0, column= 1,padx=5, pady=5)
        number_of_seat=tkinter.StringVar()
        self.type_of_seat_combo = ttk.Combobox(self.reserve_seat_frame, values=["A1", "A2", "A3", "A4", "A5","A6","B1","B2","B3","B4","B5","B6","B7","B8"])
        self.type_of_seat_combo.grid(row=1, column=1, padx=5, pady=5)

        self.quantity_adult_label = tkinter.Label(self.reserve_seat_frame, text ='Adult', bg="#88AB8E")  
        self.quantity_adult_label.grid(row=0, column=3, padx=5, pady=5)
        self.adult_quantity_box = tkinter.Spinbox(self.reserve_seat_frame, from_= 1, to = 30, bg="#EEE7DA") 
        self.adult_quantity_box.grid(row=1, column=3, padx=5, pady=5)

        self.quantity_children_label = tkinter.Label(self.reserve_seat_frame, text ='Children', bg="#88AB8E")  
        self.quantity_children_label.grid(row=0, column=2, padx=5, pady=5) 
        self.children_quantity_box = tkinter.Spinbox(self.reserve_seat_frame, from_= 0, to = 10, bg="#EEE7DA") 
        self.children_quantity_box.grid(row=1, column=2, padx=5, pady=5)

        self.calculate_button = tkinter.Button(text = "Calculate", width=15, command=self.calculate_total, bg="#EEE7DA")
        self.calculate_button.pack(side=LEFT, padx=(10,5), pady=10)

        self.save_button = tkinter.Button(text = "Submit", width=15, command=self.save_data, bg="#EEE7DA")
        self.save_button.pack(side=LEFT, padx=5, pady=10)

        self.total_output_label = tkinter.Label(self.reserve_seat_frame, text="", bg="#88AB8E")
        self.total_output_label.grid(row=3, column=2, padx=5, pady=5)

        self.back_button = tkinter.Button(text="Back to Main Menu", width=15, command=self.back_to_main_menu, bg="#EEE7DA")
        self.back_button.pack(side=LEFT, padx=(5,10), pady=10)
        

    def back_to_main_menu(self):
            self.root.destroy()

if __name__== "__main__":
    app = Reserve_seat(root)
    root.mainloop()
