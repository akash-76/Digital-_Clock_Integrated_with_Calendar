#---- DIGITAL CLOCK INTEGRATED WITH CALENDAR ----
import tkinter as tk
from time import strftime
from tkcalendar import Calendar

root=tk.Tk()
root.title("Digital Clock with Calendar")


root.configure(bg='black')

is_24_hour_format = True
def time():
    time_format = '%H:%M:%S' if is_24_hour_format else '%I:%M:%S %p'
    
    string=strftime(time_format+'\n%D')
    Label.config(text=string)
    Label.after(1000,time)

Label=tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='lime')
Label.pack(anchor='center',padx=40, pady=40)

calendar = Calendar(
    root,
    font=('calibri',20),
    selectmode='day', 
    background='black', 
    foreground='lime', 
    headersbackground='black', 
    headersforeground='lime', 
    bordercolor='lime', 
    selectbackground='lime', 
    normalbackground='white', 
    normalforeground='black', 
    weekendbackground='black', 
    weekendforeground='lime'
)
calendar.pack(anchor='center',padx=40,pady=40)

def toggle_time_format():
    global is_24_hour_format
    is_24_hour_format = not is_24_hour_format
    time()

toggle_button = tk.Button(root,text="Toggle Time Format", command=toggle_time_format, bg='lime', fg='black')
toggle_button.pack()
time()

root.mainloop()
                    
