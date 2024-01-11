from tkinter import *
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import time
from threading import Thread
from handlers import mqtt_handler
import Find_Directory_Path

# FUNCTION FOR BUTTONS
def on_prev10_click():
    buttonprev.config(bg='red', fg='white')
    buttonnext.config(bg='white', fg='red')
    

def on_next10_click():
    buttonprev.config(bg='white', fg='red')
    buttonnext.config(bg='red',  fg='white')

root = Tk()
root.geometry('1000x1000')
root.title('VFT')
# set of first line
# carwtbg
bg10 = Image.open('Images/blackbg.png')
width, height = 1400, 750
image10 = bg10.resize((width, height))
image10_tk = ImageTk.PhotoImage(bg10)
frame = Frame(root)  # Set the dimensions as needed
frame.pack(expand=True, fill=BOTH)

img10_label= Label(frame,image=image10_tk)
img10_label.place(x=0, y=0)

# Brake heading
brakeheading = Image.open('Images/brake.png')
width, height = 600, 90
brake = brakeheading.resize((width,height))
brake_head= ImageTk.PhotoImage(brake)

brake_label= Label(frame,image=brake_head, bg="#0E0E0E",pady=100)
brake_label.place(x=10, y=20)

# Apply brake heading
apply_brake_heading = Image.open('Images/applybrake.png')
width, height = 500, 70
apply_brake =apply_brake_heading .resize((width,height))
apply_brake_head= ImageTk.PhotoImage(apply_brake)

apply_brake_label= Label(frame,image=apply_brake_head, bg="#0E0E0E",pady=100)
apply_brake_label.place(x=80, y=110)

# SPEEDOMETER IMAGE 1
MQTT = mqtt_handler.mqtt_object(frame=frame)

speedometers = Image.open('Images/speedo_base.png')
width, height = 300, 60
speedometer = speedometers.resize((width,height))
speedometer_head= ImageTk.PhotoImage(speedometer)

speedometer_label= Label(frame,image=speedometer_head, bg="#0E0E0E",pady=100)
speedometer_label.place(x=20, y=468)
# label 1 : left brake
label1 = Label(frame, text='Left Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
label1.place(x=95 ,y=530)
# entryfield left brake
leftbrake_entryField = Label(frame, width=10,text='0', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
leftbrake_entryField.place(x=125, y=480)

# SPEEDOMETER IMAGE 2
speedometers2 = Image.open('Images/speedo_base.png')
width, height = 230, 50
speedometer2 = speedometers2.resize((width,height))
speedometer2_head= ImageTk.PhotoImage(speedometer2)

speedometer2_label= Label(frame,image=speedometer2_head, bg="#0E0E0E",pady=100)
speedometer2_label.place(x=400, y=380)

# label 2: left brake
label2 = Label(frame, text='Weight',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
label2.place(x=490 ,y=436)
# entryfield WEIGHT
weight_entryfield = Label(frame, width=8,text='30', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
weight_entryfield.place(x=480, y=387)
# SPEEDOMETER IMAGE 3
speedometers3 = Image.open('Images/speedo_base.png')
width, height = 300, 60
speedometer3 = speedometers3.resize((width,height))
speedometer3_head= ImageTk.PhotoImage(speedometer3)

speedometer3_label= Label(frame,image=speedometer3_head, bg="#0E0E0E",pady=100)
speedometer3_label.place(x=690, y=468)
# label 3 : left brake
label3 = Label(frame, text='Right Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
label3.place(x=770 ,y=530)
# # entryfield 
rightbrake_entryfield = Label(frame,text='400', width=10, font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
rightbrake_entryfield.place(x=795, y=480)

# info
infoheading = Image.open('Images/info.png')
width, height = 20, 20
info = infoheading.resize((width,height))
info_head= ImageTk.PhotoImage(info)

info_label= Label(frame,image=info_head, bg="#0E0E0E",pady=100)
info_label.place(x=40, y=600)

procedure_label = Label(frame, text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
procedure_label.place(x=80 ,y=600)

procedure1_label = Label(frame, text='1.Wait for car to establish connection with sensor',font=('Helvetica',10),bg="#0E0E0E",fg="white")
procedure1_label.place(x=80 ,y=630)

procedure2_label = Label(frame, text='2.Ask Driver to press accelerato',font=('Helvetica',10),bg="#0E0E0E",fg="white")
procedure2_label.place(x=80 ,y=650)

# white bg of graph
whitebg = Image.open('Images/graphbg.png')
width, height = 500, 500
whitebg_img = whitebg.resize((width,height))
whitebgimg= ImageTk.PhotoImage(whitebg_img)

whitebg_label= Label(frame,image=whitebgimg, bg="#0E0E0E",pady=100)
whitebg_label.place(x=1050, y=140)
#  BUTTON PREV AND NEXT
buttonprev = Button(frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [on_prev10_click(), start_thread()], activeforeground='white',)
buttonprev.place(x=1000,y=680)

buttonnext = Button(frame, text="Next",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [on_next10_click(), stop_thread()],activeforeground='white')
buttonnext.place(x=1200,y=680)
# status
statusheading = Image.open('Images/status.png')
width, height = 80, 20
status = statusheading.resize((width,height))
status_head= ImageTk.PhotoImage(status)

status_label= Label(frame,image=status_head, bg="#0E0E0E",pady=100)
status_label.place(x=950, y=90)

# timer
timerheading = Image.open('Images/timer.png')
width, height = 40, 40
timer = timerheading.resize((width,height))
timer_head= ImageTk.PhotoImage(timer)

timer_label= Label(frame,image=timer_head, bg="#0E0E0E",pady=100)
timer_label.place(x=950, y=120)
timer1_label= Label(frame,text='pass', bg="#0E0E0E",fg='yellow',font=(10))
timer1_label.place(x=1000, y=125)


# speedometer = needle.Speedometer(root, parent_width=310, parent_height=310, min_value=0, max_value=40, oval_radius_width=300, oval_radius_height=300, center_x=150, center_y=150, num_ticks_radius=110, ticks_radius=120, needle_quad_height=80, needle_quad_width=30, needle_quad_height_y3_y4 = 240, gauge_info_text="Left Break Force [kN]", gauge_info_text_x = 155, gauge_info_text_y = 230)
# speedometer.place(x=40, y=250)
# speedometer.update_speed(40)

# Code to show variable data in graph
style.use("ggplot")
f = Figure(figsize=(5,5), dpi=77)
a = f.add_subplot(111)

# Adjust the appearance of axis labels
a.tick_params(axis='x', labelsize=15)  # Set x-axis label size
a.tick_params(axis='y', labelsize=15)  # Set y-axis label size

canvas = FigureCanvasTkAgg(f)
canvas.get_tk_widget().place(x=1110, y=195)


# To show tool bar for graph on window
# toolbar = NavigationToolbar2Tk(canvas)
# toolbar.update()
# canvas._tkcanvas.place(x=1100, y=260)

# To update animate function at a interval of point of time
# ani = animation.FuncAnimation(self.f, animate, interval=100)
# animate_animate()



def animate_animate():
    # Call the animate function to update the graph
    while True:
        animate()
        time.sleep(1)
    # Schedule the next animation after 100ms (adjust the interval as needed)
    # self.after(1000, self.animate_animate)

# Function to update graph
def animate():
    file_path1 = Find_Directory_Path.resource_path('Graph_Text_Files\\sampleText.txt')
    file_path2 = Find_Directory_Path.resource_path('Graph_Text_Files\\sampleText2.txt')
    pullData = open(file_path1,"r").read()
    pullData2 = open(file_path2,"r").read()
    dataList = pullData.split('\n')
    dataList2 = pullData2.split('\n')
    xList = []
    yList = []
    xList2 = []
    yList2 = []
    # print("Yes i am also execuring")
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(float(x))
            yList.append(float(y))
            
    for eachLine2 in dataList2:
        if len(eachLine2) > 1:
            x, y = eachLine2.split(',')
            xList2.append(float(x))
            yList2.append(float(y))
    a.clear()
    a.plot(xList, yList, color='#CC0CA1')
    a.plot(xList2, yList2, color='#2BB3E1')
    a.tick_params(left = False)
    # Refresh the canvas to show the updated plot
    canvas.draw()
    
# Function to define car testing status
def car_testing_status (self, status_code):
    if status_code == 0:
        self.testing_status.config(text="Ideal")
    elif status_code == 1:
        self.testing_status.config(text="Waiting For Vehicle")
    elif status_code == 2:
        self.testing_status.config(text="Starting Test")
    elif status_code == 3:  
        self.testing_status.config(text="Test Running")
    elif status_code == 4:
        self.testing_status.config(text="Test Finished")
    elif status_code == 5:
        self.testing_status.config(text="Test Failed", foreground='red')

# is_running = None
def start_thread():
    # is_running = True  # Set the flag to start the thread
    # thread = Thread(target=run_thread)
    thread = Thread(target=animate_animate())
    thread.start()

def stop_thread():
    # is_running = False  # Set the flag to stop the thread

# def run_thread():
#     while is_running:
#         print("Thread is running...")
#         thread = Thread(target=animate_animate())
#         time.sleep(1)
    
    print("Thread is stopped.")


animate()


root.mainloop()