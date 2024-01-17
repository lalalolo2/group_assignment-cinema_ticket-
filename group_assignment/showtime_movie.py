import tkinter
from tkinter import ttk
from tkcalendar import DateEntry
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
root.title("Showtime Movie")
root.configure(background="#88AB8E")

class Showtime_movie(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add registration form widgets 
        frame = tkinter.Frame(root, background="#88AB8E")
        frame.pack()

        showtime_frame = tkinter.LabelFrame(frame, text = "Showtime", bg="#88AB8E")
        showtime_frame.grid (row= 0, column= 0, padx=5, pady= 5)

        def pick_date():
            top = tkinter.Toplevel(showtime_frame)
            cal = DateEntry(top, font="Arial 8", selectmode="day", locale="en_US")
            cal.pack(fill="both", expand=True)
        
            def on_date_selected():
                self.date_label.set(cal.get_date())
                top.destroy()

            button_ok = tkinter.Button(top, text="OK", command=on_date_selected)
            button_ok.pack()

        self.date_label = tkinter.StringVar()
        self.date_label.set("Select Date")
        self.date_entry = tkinter.Entry(showtime_frame,textvariable=self.date_label)
        self.date_entry.grid(row=2, column=0, padx=10, pady=10)

        self.button_pick_date = tkinter.Button(showtime_frame, text="Pick Date", background= "#EEE7DA", command=pick_date)
        self.button_pick_date.grid(row=3, column=0, padx=5, pady=5)

        #button to pick date    
        self.movie_label=tkinter.Label(showtime_frame,text="Movie Name", bg="#88AB8E")
        self.movie_label.grid(row=1, column= 1, padx=5, pady=5)
        self.mv_combobox = ttk.Combobox (showtime_frame, values = ["Aquaman", "Endless Journey"])
        self.mv_combobox.grid(row=2, column= 1, padx=5, pady=5)

       # list time
        self.time_label=tkinter.Label(showtime_frame, text='Time', bg="#88AB8E")
        self.time_label.grid(row=1, column=2, padx=5, pady=5)

        self.options_list = ["10:00 a.m - 12:15 p.m", "4:00 p.m - 6:00 p.m", "8:00 p.m-10:00 p.m", "9:00 p.m -12:00 p.m"] 
                
        self.value_inside = tkinter.StringVar(showtime_frame) 
        self.value_inside.set("Select Your Time") 
                
        self.time_menu = tkinter.OptionMenu(showtime_frame, self.value_inside,*self.options_list) 
        self.time_menu.grid(row=2,column=2, padx=5, pady=5)
        self.time_menu.config(bg="#EEE7DA")
        self.time_menu["menu"].config(bg="#EEE7DA")

        self.exp_label=tkinter.Label(showtime_frame, text='Experience', bg="#88AB8E") 
        self.exp_label.grid(row=1, column= 3, padx=5, pady=5)
        self.exp_combobox = ttk.Combobox (showtime_frame, values = ["Standard Class","SkyBox","PREMIERE","Onyx"])
        self.exp_combobox.grid(row=2, column= 3, padx=5, pady=5)

         # Prices List by using textbox
        self.note_text = tkinter.Text(showtime_frame, height=15, width=30,bg="#EEE7DA")
        self.note_text.grid(row= 0, column=1, padx=5,pady=5, sticky="nswe")

        # The defined list by using pricebox
        self.note_text.insert(tkinter.END, "Movie List and Time\n\n")
        self.note_text.insert(tkinter.END, " Aquaman\n Time : 10:00 a.m - 12:15 p.m\n\n")
        self.note_text.insert(tkinter.END, " Endless Journey\n Time : 4:00 p.m - 6:00 p.m\n\n")
        self.note_text.insert(tkinter.END, " Aquaman\n Time : 8:00 p.m-10:00 p.m \n\n")
        self.note_text.insert(tkinter.END, " Endless Journey\n Time : 9:00 p.m -12:00 p.m\n\n")
        self.note_text.configure(state='disabled')

        def submit_data():
            sql = "INSERT INTO showtime_selection (Date_label,Movie_label,Time_label,Experience_label) VALUES (%s, %s, %s, %s)"
            val = (self.date_entry.get(),self.mv_combobox.get(),self.value_inside.get(),self.exp_combobox.get())
            mycursor.execute(sql, val)
            mydb.commit()

        def update():
            date = self.date_entry.get()
            movie = self.mv_combobox.get()
            time = self.value_inside.get()
            experience = self.exp_combobox.get()

            mydb = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",  
            database="gsc_ticket" 
            )
            mycursor = mydb.cursor()

            # Get the total count of rows in the database
            mycursor.execute("SELECT COUNT(*) FROM showtime_selection")
            count = mycursor.fetchone()[0]

            if count > 0:
                 # Update the last row in the database
                sql = "UPDATE showtime_selection SET Date_label= %s, Movie_label = %s, Time_label= %s,Experience_label= %s WHERE Date_label= %s"
                val = (date,movie,time,experience)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Update Record.")
            else:
                print("No records to update.")

  
        def back_to_main_menu():
            self.root.destroy()
            

        self.submit_button = tkinter.Button(root, text='Submit', command=submit_data, bg="#EEE7DA") 
        self.submit_button.pack(side=LEFT,padx=5, pady=10)

        self.update_button = tkinter.Button(root, text='Update', command=update, bg="#EEE7DA") 
        self.update_button.pack(side=LEFT,padx=5, pady=10)

        self.back_button = tkinter.Button(root, text='Back to Main Menu', command=back_to_main_menu, bg="#EEE7DA") 
        self.back_button.pack(side=LEFT,padx=5, pady=10)


if __name__== "__main__":
    app = Showtime_movie(root)
    root.mainloop()

 