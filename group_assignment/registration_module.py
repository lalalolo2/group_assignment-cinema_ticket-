import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import mysql.connector 



# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gsc_ticket"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


root = tkinter.Tk()

root.title("User Registration")
root.geometry("400x230")
root.configure(background="#88AB8E")


class register(tkinter.Frame):
   
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add registration form widgets 
        frame = tkinter.Frame(root)
        frame.pack()

        # user detail
        user_info_frame = tkinter.LabelFrame(frame, text="User Registration", bg="#88AB8E")
        user_info_frame.grid(row=0, column=0)

        self.name_label = tkinter.Label(user_info_frame, text=" Name", bg="#88AB8E")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tkinter.Entry(user_info_frame, bg="#EEE7DA")
        self.name_entry.grid(row=1, column=0)

        self.age_label = tkinter.Label(user_info_frame, text=" Age", bg="#88AB8E")
        self.age_label.grid(row=0, column=1)
        self.age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=55, bg="#EEE7DA")
        self.age_spinbox.grid(row=1, column=1)

        self.gender_label = tkinter.Label(user_info_frame, text="Gender", bg="#88AB8E")
        self.gender_label.grid(row=0, column=2)

        # Use IntVar to store the state of the Checkbutton
        self.gender_var = tkinter.IntVar()
        self.gender_check_male = tkinter.Checkbutton(user_info_frame, text="Male", variable=self.gender_var, bg="#88AB8E")
        self.gender_check_male.grid(row=1, column=2)

        self.gender_check_female = tkinter.Checkbutton(user_info_frame, text="Female", bg="#88AB8E")
        self.gender_check_female.grid(row=1, column=4)

        self.no_phone_label = tkinter.Label(user_info_frame, text="Phone Number", bg="#88AB8E")
        self.no_phone_label.grid(row=2, column=0)
        self.no_phone_entry = tkinter.Entry(user_info_frame, bg="#EEE7DA")
        self.no_phone_entry.grid(row=3, column=0)

        self.email_label = tkinter.Label(user_info_frame, text="Email", bg="#88AB8E")
        self.email_label.grid(row=2, column=1)
        self.email_entry = tkinter.Entry(user_info_frame, bg="#EEE7DA")
        self.email_entry.grid(row=3, column=1)

        self.submit_button = tkinter.Button(root, text="Submit", background="gray", command=self.submit_data, bg="#EEE7DA")
        self.submit_button.pack(side=LEFT, padx=(10,5), pady=10)

        self.delete_button = tkinter.Button(root, text="Delete", command=self.delete_data, bg="#EEE7DA")
        self.delete_button.pack(side=LEFT, padx=5, pady=10)

        self.back_button = tkinter.Button(root, text="Back to Main Menu", command=self.back_to_main_menu, bg="#EEE7DA")
        self.back_button.pack(side=LEFT, padx=(5,10), pady=10)

    def delete_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="gsc_ticket" 
        )

        mycursor = mydb.cursor()

        # Get the total count of rows in the database
        mycursor.execute("SELECT COUNT(*) FROM user_registration")
        count = mycursor.fetchone()[0]

        if count > 0:
            # Delete the last row in the database
            sql = "DELETE FROM user_registration ORDER BY name DESC LIMIT 1"
            mycursor.execute(sql)
            mydb.commit()
            print("Last record deleted.")
        else:
            print("No records to delete.")

        mycursor.close()
        mydb.close()



    def submit_data(self):

        
        if not self.name_entry.get():
            tkinter.messagebox.showwarning(title="Error", message="Name is required.")
            return

        age_int = self.age_spinbox.get()

        age = int(age_int)

        if age >= 18:
            note_label = tkinter.Label (root, text="You are allowed to proceed!", font=("Times New Roman", 10, "italic"))
            note_label.pack(pady=5)
        else:
            note_label = tkinter.Label(root, text="Under 18 years old need to bring your parents.", font=("Times New Roman", 10, "italic"))
            note_label.pack(pady=5)

        print("Name:", self.name_entry.get())
        print("Age:",self.age_spinbox.get())
        print("Gender:",self.gender_var.get())
        print("Phone Number:",self.no_phone_entry.get())
        print("Email:",self.email_entry.get())


        # Get the value of the Checkbutton using get()
        gender = "Male" if self.gender_var.get() else "Female"

        # To insert your Data to your database
        sql = "INSERT INTO user_registration (Name, Age, Gender, Phone_Number, Email) VALUES (%s, %s, %s, %s, %s)"
        val = (self.name_entry.get(), self.age_spinbox.get(), gender, self.no_phone_entry.get(), self.email_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()


        mycursor.close()
        mydb.close()

        
    def back_to_main_menu(self):
        self.root.destroy() 


if __name__== "__main__":
    app = register(root)
    root.mainloop()


