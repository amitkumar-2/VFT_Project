from tkinter import *
from PIL import Image, ImageTk

# FUNCTION FOR BUTTONS
def on_prev_click():
    buttonprev.config(bg='red', fg='white')
    buttonnext.config(bg='white', fg='red')
    

def on_next_click():
    buttonprev.config(bg='white', fg='red')
    buttonnext.config(bg='red',  fg='white')
    
root = Tk()
root.geometry('1000x1000')
root.title('VFT')
# set of first line
# carwtbg
bg9 = Image.open('Images/blackbg.png')
width, height = 1400, 750
image9 = bg9.resize((width, height))
image9_tk = ImageTk.PhotoImage(image9)
frame = Frame(root, width=1300, height=750)  # Set the dimensions as needed
frame.pack()

img9_label= Label(frame,image=image9_tk)
img9_label.place(x=0, y=0)

# speed heading
speedheading = Image.open('Images/speed.png')
width, height = 900, 90
speed = speedheading.resize((width,height))
speed_head= ImageTk.PhotoImage(speed)

speed_label= Label(frame,image=speed_head, bg="#0E0E0E",pady=100)
speed_label.place(x=3, y=40)

# ACCELERATE heading
accelerateheading = Image.open('Images/accelerate.png')
width, height = 600, 80
accelerate = accelerateheading.resize((width,height))
accelerate_head= ImageTk.PhotoImage(accelerate)

accelerate_label= Label(frame,image=accelerate_head, bg="#0E0E0E",pady=100)
accelerate_label.place(x=60, y=170)

# status
statusheading = Image.open('Images/status.png')
width, height = 100, 20
status = statusheading.resize((width,height))
status_head= ImageTk.PhotoImage(status)

status_label= Label(frame,image=status_head, bg="#0E0E0E",pady=100)
status_label.place(x=160, y=280)


# timer
timerheading = Image.open('Images/timer.png')
width, height = 40, 40
timer = timerheading.resize((width,height))
timer_head= ImageTk.PhotoImage(timer)

timer_label= Label(frame,image=timer_head, bg="#0E0E0E",pady=100)
timer_label.place(x=160, y=320)
status_input = Label(frame, width=8,text='pass', font=(12), fg='yellow',bg="#0E0E0E",borderwidth=0,relief='flat')
status_input.place(x=200, y=330)

# info
infoheading = Image.open('Images/info.png')
width, height = 25, 25
info = infoheading.resize((width,height))
info_head= ImageTk.PhotoImage(info)

info_label= Label(frame,image=info_head, bg="#0E0E0E",pady=100)
info_label.place(x=40, y=470)

procedure_label = Label(text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
procedure_label.place(x=80 ,y=473)

procedure1_label = Label(text='1.Wait for car to establish connection with sensor',font=('Helvetica',12),bg="#0E0E0E",fg="white")
procedure1_label.place(x=80 ,y=500)

procedure2_label = Label(text='2.Ask Driver to press accelerato',font=('Helvetica',12),bg="#0E0E0E",fg="white")
procedure2_label.place(x=80 ,y=530)

procedure3_label = Label(text='3. .....(your own instructions)',font=('Helvetica',12),bg="#0E0E0E",fg="white")
procedure3_label.place(x=80 ,y=560)

# SPEEDOMETER IMAGE
speedometers = Image.open('Images/speedometer.png')
width, height = 500, 450
speedometer = speedometers.resize((width,height))
speedometer_head= ImageTk.PhotoImage(speedometer)

speedometer_label= Label(frame,image=speedometer_head, bg="#0E0E0E",pady=100)
speedometer_label.place(x=650, y=100)
# ENTRY FIELD IN SPEEDOMETER
speedentryField = Label(frame, width=20,text='80kmph', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
speedentryField.place(x=810, y=460)

# BUTTON PREV AND NEXT
buttonprev = Button(frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=on_prev_click, activeforeground='white',)
buttonprev.place(x=850,y=580)

buttonnext = Button(frame, text="Next",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=on_next_click,activeforeground='white')
buttonnext.place(x=1050,y=580)

root.mainloop()