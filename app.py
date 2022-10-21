#Importing tkinter for GUI
from tkinter import *
#Importing time module to get current time
import time
#importing datetime module to get current date
import datetime

#using time module to get current time and storing it in current_time variable inside the updateTime Function
#using after() method to run the function every .5 second to update time in the clock.
def update():
    #using strftime to get time
    current_time = time.strftime("%H:%M:%S", time.localtime())
    #using datetime.now() to get time and setting it into diffrent variables
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    time_label["text"] = current_time
    date_label["text"] = "{}/{}/{}".format(day,month,year)
    time_label.after(500, update)

#Creating the GUI window using tkinter
window = Tk()
window.geometry('250x90')
window.title("Clock")

#Setting resizeable to false to prevent user from resizing the window
window.resizable(0,0)

#Changing the background and foreground colors of GUI 
window.configure(bg="black")

#Creating a label to display time
time_label = Label(window, font = ("Aerial", 36), bg="black", fg="lightgreen")
time_label.pack()

#Creating a label to display date
date_label = Label(window, font = ("Aerial", 18), bg = "black", fg = "lightgreen")
date_label.pack()
#Calling the update function 
update()

#Initializing mainloop
window.mainloop()