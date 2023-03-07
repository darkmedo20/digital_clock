import sys
from tkinter import*
import time
# used to display the time on the label
def Clock():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(100,Clock)

# making a window
window = Tk()
window.title('Dark Medo Clock')#adding title to the window
window
# giving name to our digital clock and styling it
message = Label(window,font = ("times",100,"bold"),
text = "Times",fg = "green")
message.grid(row=0,column=0)
clock = Label(window,
font=("Time",150,"bold"),fg="black",bg="yellow")
clock.grid(row=1,column=0)
Clock()
mainloop()