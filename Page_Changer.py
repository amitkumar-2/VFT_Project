import tkinter as tk
from tkinter import Tk
import tkinter as tk
import math
import json
import time
import os

from tkinter.ttk import Label, Progressbar, Button

import paho.mqtt.client as mqtt

import tkinter.ttk as ttk

from PIL import Image,ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import matplotlib

matplotlib.use("TkAgg")

from matplotlib.figure import Figure

import matplotlib.animation as animation

from matplotlib import style

import calibrationForLBF

import calibrationForRBF

import calibrationForAW

class Speedometer(tk.Canvas):
    def __init__(self, parent, min_value, max_value):
        super().__init__(parent, width=310, height=310)
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        
        self.center_x = 150
        self.center_y = 150

        self.configure(bg=self_background_color, highlightthickness=0)
        self.create_oval(0, 0, 300, 300, width=3, outline='white', fill='black', )
        self.create_text(150, 150, text='Speed', font=('Arial', 16))
        self.value_text = self.create_text(150, 180, text=str(self.value), font=('Arial', 24, 'bold'))
        
        # Add number indications
        num_ticks = 9  # Number of tick marks
        angle_range = 270  # Angle range for the tick marks
        angle_increment = angle_range / (num_ticks - 0)  # Angle increment between each tick mark

        for i in range(num_ticks):
            angle = -215 + i * angle_increment  # Calculate the angle for the tick mark
            radius = 110  # Radius for the tick mark

            x = 150 + radius * math.cos(math.radians(angle))
            y = 150 + radius * math.sin(math.radians(angle))

            value = int(min_value + (max_value - min_value) / (num_ticks - 1) * i)  # Calculate the value for the tick mark
            # values = [0,4,8,12,16,20,24,28,32,36,40]
            # value = values[i]

            self.create_text(x, y, text=str(value), font=('Arial', 10), fill='white')
            
        # Drawing big ticks on analog gauge
        for angle in range(-25, 225, 30):  # Draw ticks every 30 degrees
            radius1 =120
            angle_rad = math.radians(angle)
            x1 = self.center_x + (radius1 + 5) * math.cos(angle_rad)
            y1 = self.center_y - (radius1 + 5) * math.sin(angle_rad)
            x2 = self.center_x + (radius1 + 30) * math.cos(angle_rad)
            y2 = self.center_y - (radius1 + 30) * math.sin(angle_rad)
            self.create_line(x1, y1, x2, y2, fill='white', width=2)
        
        # Drawing big ticks on analog gauge
        for angle in range(-25, 220, 5):  # Draw ticks every 5 degrees
            radius1 =120
            angle_rad = math.radians(angle)
            x1 = self.center_x + (radius1 + 18) * math.cos(angle_rad)
            y1 = self.center_y - (radius1 + 18) * math.sin(angle_rad)
            x2 = self.center_x + (radius1 + 30) * math.cos(angle_rad)
            y2 = self.center_y - (radius1 + 30) * math.sin(angle_rad)
            self.create_line(x1, y1, x2, y2, fill='white', width=2)


    def update_speed(self, speed):
        self.value = speed
        self.itemconfigure(self.value_text, text=str(self.value))

        # Calculate the angle for the needle
        angle = (self.value - self.min_value) / (self.max_value - self.min_value) * 180 - 90
        angle = 55 + self.value

        # Calculate the coordinates of the quadrilateral points
        center_x = 150
        center_y = 150
        quad_width = 30
        quad_height = 80

        x1 = center_x - quad_width / 2
        y1 = center_y - quad_height / 2
        x2 = center_x + quad_width / 2
        y2 = center_y - quad_height / 2
        x3 = center_x + 1 / 2
        y3 = center_y + 240 / 2
        x4 = center_x - 1 / 2
        y4 = center_y + 240 / 2

        # Rotate the quadrilateral based on the angle
        rotated_points = rotate_points([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], center_x, center_y, angle)

        # Clear previous needle and draw the new quadrilateral
        self.delete('needle')
        self.create_polygon(rotated_points[0][0], rotated_points[0][1],
                            rotated_points[1][0], rotated_points[1][1],
                            rotated_points[2][0], rotated_points[2][1],
                            rotated_points[3][0], rotated_points[3][1],
                            fill='#ED7D1E', tags='needle')
        
    
    
            
                
                

def rotate_points(points, center_x, center_y, angle):
    rotated_points = []
    for x, y in points:
        rotated_x = center_x + (x - center_x) * math.cos(math.radians(angle)) - (y - center_y) * math.sin(math.radians(angle))
        rotated_y = center_y + (x - center_x) * math.sin(math.radians(angle)) + (y - center_y) * math.cos(math.radians(angle))
        rotated_points.append((rotated_x, rotated_y))
    return rotated_points





# Color variable to store color
self_background_color = '#9AD9EA'
dynamic_data_background_color = '#81D697'
dynamic_data_forground_color = '#000000'
information_text_background_color = '#4CF701'
information_text_forground_color = '#790140'
# Font family variable
font_family = 'Helvetica'


class MultiPageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CTI Vehicle Fitness Test")
        self.iconbitmap(r"C:\Users\cti-2\Downloads\R&D Team WhatsappFiles\CTIWhatsappForMe\WhatsApp-Image-2023-06-17-at-11.15.32-AM-_1_.ico")
        self.geometry("1500x770")
        self.minsize(1400,750)
        
        # Get the directory path where the script is located
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # Change the working directory to the script's directory
        os.chdir(self.script_directory)
        
        self.file_path1 = os.path.join(self.script_directory, 'sampleText.txt')
        self.file_path2 = os.path.join(self.script_directory, 'sampleText2.txt')
        
        # Create a container to hold all the pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.pages = {}  # Dictionary to store pages
        
        # Create and add pages to the dictionary
        for PageClass in [Page1, Page2]:
            page_name = PageClass.__name__
            page = PageClass(self.container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights for the container
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        
        # Show the initial page
        self.show_page("Page1")
        
        self.speed_list = [0]
        # MQTT All Process Code Is Here
        self.mqttBroker = "3.110.187.253"
        self.client = mqtt.Client("Smartphone")
        self.client.on_message = self.on_mqttMessage
        self.client.on_connect = self.on_mqttConnect
        self.client.connect(self.mqttBroker,1883,60)
        self.client.loop_start()
        
        
    def show_page(self, page_name):
        # Show the selected page
        page = self.pages[page_name]
        page.tkraise()
        
    # Function for increasment of j For Time Graph
    # j = 0.1
    def time_increasement(self):
        global j
        j = 0.1
        if j<300.1:
            j +=0.1
    
    def on_mqttMessage(self, client, userdata, msg):
        # Cleaning all data from rangeValues.txt file
        rangeValues_paths = ['rangeValuesForRPM.txt', 'rangeValuesForLBF.txt', 'rangeValuesForRBF.txt', 'rangeValuesForAW.txt']
        for rangeValues_path in rangeValues_paths:
            with open(rangeValues_path, "w") as file:
                file.write("")
        
        
        # Here you can update the labels based on the MQTT message
        if msg.topic == "001/TESTER/BREAK/BREAKFORCE":
            # self.pages['Page1'].label1.config(text=msg.payload.decode("utf-8"))
            message0 = str(msg.payload.decode("utf-8"))
            m_in = json.loads(message0)
            break_force_left = int(m_in['Break Force Left'])
            break_force_right = int(m_in['Break Force Right'])
            test_status = int(m_in['TestStatus'])
            axle_weight = int(m_in['Axle Weight'])
            rpm = int(m_in['rpm'])
            
            # Calling back function to increase time    
            self.time_increasement()
            
            # code to calibrate LBF values
            file_path = "calibrationConfigurationLBFFile.txt"
            mac_address = "AB:CD:EF:12:34:56"
            offset = 2
            coef = 9
            raw_data = break_force_left
            value = round(((raw_data - offset)/coef)*0.985, 2)
            if value > 0:
                calibrated_variable_lbf = calibrationForLBF.write_range_value(file_path, mac_address, value)
                m_lbf = calibrated_variable_lbf[0]
                c_lbf = calibrated_variable_lbf[1]
                # print(m_lbf,c_lbf)
                calibrated_lbf = m_lbf*value + c_lbf
            else:
                calibrated_lbf = value
                
            # write calibrate value on GUI screen and file
            self.pages['Page1'].lbl2.config(text=calibrated_lbf)
            file = open(self.file_path1, "a")
            file.writelines(repr(j) + ',' +repr(calibrated_lbf)+"\n")
            file.close()
            
            # code to calibrate RBF values
            file_path = "calibrationConfigurationRBFFile.txt"
            mac_address = "AB:CD:EF:12:34:56"
            offset = 20
            coef = 9
            raw_data = break_force_right
            value = round(((raw_data - offset)/coef)*0.985, 2)
            if value > 0:
                calibrated_variable_rbf = calibrationForRBF.write_range_value(file_path, mac_address, value)
                m_rbf = calibrated_variable_rbf[0]
                c_rbf = calibrated_variable_rbf[1]
                calibrated_rbf = m_rbf*value + c_rbf
            else:
                calibrated_rbf = value
            
            # write calibrate value on GUI screen and file
            self.pages['Page1'].lbl3.config(text=calibrated_rbf)
            file = open(self.file_path2, "a")
            file.writelines(repr(j) + ',' +repr(calibrated_rbf) +"\n")
            file.close()
            
            # Car Testing Status
            self.pages['Page1'].car_testing_status(test_status)
            
            # Code to calibrate Axle Weight values
            file_path = "calibrationConfigurationAWFile.txt"
            mac_address = "AB:CD:EF:12:34:56"
            offset = 320
            coef = 90
            raw_data = axle_weight
            value = round((raw_data - offset)/coef, 2)
            calibrated_variable_AW = calibrationForAW.write_range_value(file_path, mac_address, value)
            m_AW = calibrated_variable_AW[0]
            c_AW = calibrated_variable_AW[1]
            calibrated_AW = m_AW*value + c_AW
            
            # excelWeightlbl.config(text=axle_weight)
            self.pages['Page1'].excelWeightlbl.config(text=calibrated_AW)
                
            
            # speed_list = [0]
            self.speed_list.insert(0, rpm)
            for i in range(len(self.speed_list)):
                if len(self.speed_list) > 2:
                    self.speed_list.pop(2)
                else:
                    pass
            print(self.speed_list)
            
            actual_speed = [self.speed_list[1]]
            if self.speed_list[0] > self.speed_list[1]:
                for i in range(self.speed_list[0] - self.speed_list[1]):
                    actual_speed[0] += 1
                    self.pages['Page1'].speedometer.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            else:
                for i in range(self.speed_list[1] - self.speed_list[0]):
                    actual_speed[0] -= 1
                    self.speedometer.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            
            
        elif msg.topic == "topic2":
            self.pages['Page1'].label2.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic3":
            self.pages['Page2'].label3.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic4":
            self.pages['Page2'].label4.config(text=msg.payload.decode("utf-8"))
    
    
    def on_mqttConnect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("001/TESTER/BREAK/BREAKFORCE")
        
        
    



class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(background=self_background_color)
        
        # label = tk.Label(self, text="Page 1", font=("Arial", 20))
        # label.pack(pady=20)
        
        # Get the directory path where the script is located
        self.script_directory = os.path.dirname(os.path.abspath(__file__))

        # Change the working directory to the script's directory
        os.chdir(self.script_directory)
        
        # Adding background images to make rounded corner of labels
        self.image = Image.open("Green.png")
        width, height = 285, 70
        self.image = self.image.resize((width, height), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        labelimg = Label(self, image=self.image_tk, relief='flat', borderwidth=0, background=self_background_color)
        labelimg.place(x=440, y=100)

        self.image1 = Image.open("Green.png")
        width, height = 285, 70
        self.image1 = self.image1.resize((width, height), Image.ANTIALIAS)
        self.image1_tk = ImageTk.PhotoImage(self.image1)
        labelimg1 = Label(self, image=self.image1_tk, relief='flat', borderwidth=0, background=self_background_color)
        labelimg1.place(x=45, y=100)
        
        
        # Heading Labeling
        lbl1 = Label(self,text="Apply parking break to max and take a rest", foreground="white", background="black", font=(font_family, 25, 'bold'), width=100, padding=(250, 20))
        lbl1.pack()

        # Informating Text Labeling
        informationLeftlbl = Label(self, text="Break Force Left", foreground=information_text_forground_color, background=information_text_background_color, font=(font_family, 15,'bold'))
        informationLeftlbl.place(x=105, y=120)

        informationRightlbl = Label(self, text="Break Force Right", foreground=information_text_forground_color, background=information_text_background_color, font=(font_family, 15,'bold'))
        informationRightlbl.place(x=505, y=120)

        # Variable Data Measurment Labeling
        self.lbl2 = Label(self, text="0", foreground='#CC0CA1', background=dynamic_data_background_color, font=('font_family', 20,'bold'), padding=(50,15))
        self.lbl2.place(x=100, y=200)

        self.lbl3 = Label(self, text="0", foreground='#0187D5', background=dynamic_data_background_color, font=('font_family', 20,'bold'), padding=(50, 15))
        self.lbl3.place(x=500, y=200)
        
        
        # Code To show axle weight
        excelWeightlbl_text = Label(self, text="Axle Weight", foreground=information_text_forground_color, background=information_text_background_color, font=(font_family, 14,'bold'), padding=(20,10))
        excelWeightlbl_text.place(x=290, y=308)

        self.excelWeightlbl = Label(self, text="1500", foreground=dynamic_data_forground_color, background=dynamic_data_background_color, font=(font_family, 14,'bold'), padding=(20,10))
        self.excelWeightlbl.place(x=325, y=368)
        
        

        # Code to show variable data in graph
        style.use("ggplot")
        self.f = Figure(figsize=(5,5), dpi=60)
        self.a = self.f.add_subplot(111)
        
        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.get_tk_widget().place(x=850, y=220)

        # To show tool bar for graph on window
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.place(x=1100, y=160)

        # To update animate function at a interval of point of time
        # ani = animation.FuncAnimation(self.f, animate, interval=100)
        self.animate_animate()
        
        
        
        
        # Break efficient text and value
        break_efficient_text = Label(self, text="Break Efficiency:", font=(font_family, 18, 'bold'), background=information_text_background_color, foreground=information_text_forground_color, padding=(20,5))
        break_efficient_text.place(x=50, y=655)

        break_efficiency_variable = 90

        break_efficient_value = Label(self, text= repr(break_efficiency_variable)  + "%", font=(font_family, 18, 'bold'), background=dynamic_data_background_color, foreground=dynamic_data_forground_color, padding=(30, 5))
        break_efficient_value.place(x=300, y=655)

        # Car testing progress status
        testing_status_text = Label(self, text="Testing Status:", font=(font_family, 14, 'bold'), background=information_text_background_color, foreground=information_text_forground_color, padding=(20,5))
        testing_status_text.place(x=850, y=115)

        self.testing_status = Label(self, text="Ideal", font=(font_family, 14, 'bold'), background=dynamic_data_background_color, foreground=dynamic_data_forground_color, padding=(5,5))
        self.testing_status.place(x=1050, y=115)

        # Test result ok or not ok
        test_result_text = Label(self, text="Test Result:", font=(font_family, 18, 'bold'), background=information_text_background_color, foreground=information_text_forground_color, padding=(20,5))
        test_result_text.place(x=450, y=655)

        test_result = Label(self, text="NOT OK", font=(font_family, 16, 'bold'), background=dynamic_data_background_color, foreground=dynamic_data_forground_color, padding=(20,5))
        test_result.place(x=640, y=657)
        
        
        # Styling reset buttom with the help of style configuration
        s1 = ttk.Style()
        def on_enter(event):
            s1.configure("Custom.TButton", foreground=information_text_forground_color, background='white', font =
                    ('calibri', 15, 'bold'))
            
        def on_leave(event):
            s1.configure("Custom.TButton", foreground=information_text_forground_color, background='white', font =
                    ('calibri', 13, 'bold'))
            
        s1.configure("Custom.TButton", foreground=information_text_forground_color, background='white', font =
                    ('calibri', 13, 'bold'))

        button = Button(self, text="Reset", width=10, style="Custom.TButton") #, command=run
        button.place(x=1175, y=670)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        
        speed_list = [0]
        self.speedometer = Speedometer(self, min_value=0, max_value=160)
        speedometer1 = Speedometer(self, min_value=0, max_value=160)
        self.speedometer.place(x=10, y=300)
        speedometer1.place(x=400, y=300)
        speedometer1.update_speed(speed_list[0])
        self.speedometer.update_speed(speed_list[0])
        
        
        button = tk.Button(self, text="Next", width=10,font =
                    ('calibri', 13, 'bold'),  command=lambda: controller.show_page("Page2"))
        button.place(x=1375, y=670)
        
        
    def update_speedometer(self, speed):
        self.speedometer.update_speed(40)
        
    def animate_animate(self):
        # Call the animate function to update the graph
        self.animate()
        # Schedule the next animation after 100ms (adjust the interval as needed)
        self.after(100, self.animate_animate)
        # Function to update graph
    def animate(self):
        file_path1 = os.path.join(self.script_directory, 'sampleText.txt')
        file_path2 = os.path.join(self.script_directory, 'sampleText2.txt')
        pullData = open(file_path1,"r").read()
        pullData2 = open(file_path2,"r").read()
        dataList = pullData.split('\n')
        dataList2 = pullData2.split('\n')
        xList = []
        yList = []
        xList2 = []
        yList2 = []
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
        self.a.clear()
        self.a.plot(xList, yList, color='#CC0CA1')
        self.a.plot(xList2, yList2, color='#2BB3E1')
        self.a.tick_params(left = False)
        
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
    
    
    

    
    
# Function to reset page
# def run():
#     reset_first_page(root)
# def reset_first_page (root):  
#     publish_msg('001/OPERATOR/BREAK/REQ', 'START_TEST')
        
        

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="Page 2", font=("Arial", 20))
        label.pack(pady=20)
        
        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page("Page1"))
        button.pack()
        
        label = tk.Label(self, text="This is Page 2", font=("Arial", 20))
        label.place(x=400, y=200)








if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
