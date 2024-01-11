import paho.mqtt.client as mqtt
import time
import json
from random import randint
from handlers import needle
import requests

from handlers import Image1
import calibrationForAW
import calibrationForLBF
import calibrationForRBF
import calibrationForRange
import Find_Directory_Path

# define j variable for time increasement
j = 0.1

class mqtt_object:
    def __init__(self, frame, id):
        
        self.frame = frame
        self.id = id
        
        # Define the variables to update the GRAPH Files
        self.file_path1 = Find_Directory_Path.resource_path('Graph_Text_Files\\sampleText.txt')
        self.file_path2 = Find_Directory_Path.resource_path('Graph_Text_Files\\sampleText2.txt')
        
        # Define variable to update needle position
        self.speed_list = [0]
        self.lbf_list = [0]
        self.rbf_list = [0]
        self.axel_weight_list = [0]
        
        # MQTT All Process Code Is Here
        mqttBroker = "3.110.187.253"
        client = mqtt.Client("Smartphone")
        client.on_message = self.on_mqttMessage
        client.on_connect = self.on_mqttConnect
        client.connect(mqttBroker,1883,60)
        client.loop_start()
        
        self.testing_status= tk.Label(self.frame,text='pass', bg="#0E0E0E",fg='yellow',font=('','12'))
        self.testing_status.place(x=1000, y=105)
        
        
        
        self.speedometer_left = needle.Speedometer(self.frame, parent_width=252, parent_height=252, min_value=0, max_value=40, oval_radius_width=250, oval_radius_height=250, center_x=125, center_y=125, num_ticks_radius=95, ticks_radius=95, needle_quad_height=50, needle_quad_width=20, needle_quad_height_y3_y4 = 190, gauge_info_text="Left Break Force [kN]", gauge_info_text_x = 155, gauge_info_text_y = 230)
        self.speedometer_left.place(x=55, y=275)
        self.speedometer_left.update_speed(0)
        Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 20, 468)
        # entryfield left brake
        self.leftbrake_entryField = tk.Label(self.frame, width=10,text='0', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        self.leftbrake_entryField.place(x=125, y=480)
        
        self.speedometer_axle = needle.Speedometer(self.frame, parent_width=252, parent_height=252, min_value=10, max_value=2550, oval_radius_width=200, oval_radius_height=200, center_x=100, center_y=100, num_ticks_radius=70, ticks_radius=70, needle_quad_height=35, needle_quad_width=15, needle_quad_height_y3_y4 = 140, gauge_info_text="", gauge_info_text_x = 155, gauge_info_text_y = 230)
        self.speedometer_axle.place(x=415, y=225)
        self.speedometer_axle.update_speed(0)
        Image1.image_handler(self.frame, 'Images/speedo_base.png', 230, 50, 400, 380)
        self.axle_weight_entryfield = tk.Label(self.frame,text='0', width=8, font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        self.axle_weight_entryfield.place(x=480, y=387)
        
        
        
        self.speedometer_right = needle.Speedometer(self.frame, parent_width=252, parent_height=252, min_value=0, max_value=40, oval_radius_width=250, oval_radius_height=250, center_x=125, center_y=125, num_ticks_radius=95, ticks_radius=95, needle_quad_height=50, needle_quad_width=20, needle_quad_height_y3_y4 = 190, gauge_info_text="Right Break Force [kN]", gauge_info_text_x = 155, gauge_info_text_y = 230)
        self.speedometer_right.place(x=725, y=275)
        self.speedometer_right.update_speed(0)
        Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 690, 468)
        # entryfield 
        self.rightbrake_entryfield = tk.Label(self.frame,text='0', width=10, font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        self.rightbrake_entryfield.place(x=795, y=480)
        
        
        self.buttonnext = tk.Button(self.frame, text="Start",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',activeforeground='white',command=lambda: [self.get_tair_values()])
        self.buttonnext.place(x=900,y=680)
    
        self.tair_calibrated_lbf =  0
        self.tair_calibrated_rbf = 0
        self.tair_rpm = 0
        self.tair_calibrated_AW = 0
    
    
    def get_tair_values(self):
        self.tair_calibrated_lbf = self.calibrated_lbf_m_c
        # print(self.tair_calibrated_lbf)
        self.tair_calibrated_rbf = self.calibrated_rbf_m_c
        self.tair_rpm = self.rpm
        self.tair_calibrated_AW = self.calibrated_AW_m_c
    
    
    # Function for increasment of j For Time Graph
    def time_increasement(self):
        global j
        if j<300.1:
            j +=0.1
    
    def on_mqttConnect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("48:27:E2:45:64:1A")
    
    
    def on_mqttMessage(self, clien, userdata, msg):
        print('################################starting here########################################')
        # Cleaning all data from rangeValues.txt file
        rangeValuesForRPM=Find_Directory_Path.resource_path('Range_Values_Files\\rangeValuesForRPM.txt')
        rangeValuesForLBF=Find_Directory_Path.resource_path('Range_Values_Files\\rangeValuesForLBF.txt')
        rangeValuesForRBF=Find_Directory_Path.resource_path('Range_Values_Files\\rangeValuesForRBF.txt')
        rangeValuesForAW=Find_Directory_Path.resource_path('Range_Values_Files\\rangeValuesForAW.txt')

        rangeValues_paths = [rangeValuesForRPM, rangeValuesForLBF, rangeValuesForRBF, rangeValuesForAW]
        for rangeValues_path in rangeValues_paths:
            with open(rangeValues_path, "w") as file:
                file.write("")
        
        
        # Here you can update the labels based on the MQTT message
        if msg.topic == "48:27:E2:45:64:1A":
            # self.pages['Page1'].label1.config(text=msg.payload.decode("utf-8"))
            message0 = str(msg.payload.decode("utf-8"))
            m_in = json.loads(message0)
            # print(m_in  ['d'])
            self.break_force_left = int(m_in['LeftBrakeForce'])
            self.break_force_right = int(m_in['RightBrakeForce'])
            self.test_status = int(m_in['TestStart'])
            self.axle_weight = int(m_in['Weight'])
            self.rpm = int(m_in['RPM'])
            random = randint(1, 10)
            self.rpm = self.rpm*random
            
            
            # Calling back function to increase time    
            self.time_increasement()
            # print(j)
            
            # code to calibrate LBF values
            file_path = Find_Directory_Path.resource_path("Calibration_Files\\calibrationConfigurationLBFFile.txt")
            mac_address = "AB:CD:EF:12:34:56"
            offset = 2
            coef = 9
            raw_data = self.break_force_left
            value = round(((raw_data - offset)/coef)*0.985, 2)
            if value > 0:
                calibrated_variable_lbf = calibrationForLBF.write_range_value(file_path, mac_address, value)
                m_lbf = calibrated_variable_lbf[0]
                c_lbf = calibrated_variable_lbf[1]
                # print(m_lbf,c_lbf)
                self.calibrated_lbf_m_c = m_lbf*value + c_lbf
                self.calibrated_lbf = 0
                try:
                    if self.tair_calibrated_lbf:
                        self.calibrated_lbf = self.calibrated_lbf_m_c - self.tair_calibrated_lbf
                except:
                    pass
            else:
                # self.calibrated_lbf = value
                self.calibrated_lbf = 0
                
            # write calibrate value on GUI screen and file
            self.calibrated_lbf = float(f"{self.calibrated_lbf:.2f}")
            # self.pages['Page1'].lbl2.update_text(new_text=calibrated_lbf)
            # leftbrake_entryField = tk.Label(self.frame, text=calibrated_lbf)
            # leftbrake_entryField.place(x=125, y=480)
            # print("#############", calibrated_lbf)
            self.leftbrake_entryField.config(text=self.calibrated_lbf)
            
            file = open(self.file_path1, "a")
            file.writelines(repr(j) + ',' +repr(self.calibrated_lbf)+"\n")
            file.close()
            
            # code to calibrate RBF values
            file_path = Find_Directory_Path.resource_path("Calibration_Files\\calibrationConfigurationRBFFile.txt")
            mac_address = "AB:CD:EF:12:34:56"
            offset = 20
            coef = 9
            raw_data = self.break_force_right
            value = round(((raw_data - offset)/coef)*0.985, 2)
            if value > 0:
                calibrated_variable_rbf = calibrationForRBF.write_range_value(file_path, mac_address, value)
                m_rbf = calibrated_variable_rbf[0]
                c_rbf = calibrated_variable_rbf[1]
                self.calibrated_rbf_m_c = m_rbf*value + c_rbf
                self.calibrated_rbf = 0
                try:
                    if self.tair_calibrated_lbf:
                        self.calibrated_rbf = self.calibrated_rbf_m_c - self.tair_calibrated_rbf
                except:
                    pass
            else:
                # calibrated_rbf = value
                self.calibrated_rbf = 0
            
            # write calibrate value on GUI screen and file
            self.calibrated_rbf = float(f"{self.calibrated_rbf:.2f}") # formating calibrated_rbf with two decible points
            # self.pages['Page1'].lbl3.update_text(new_text=calibrated_rbf)
            # rightbrake_entryField = tk.Label(self.frame, text=calibrated_lbf)
            # rightbrake_entryField.place(x=795, y=480)
            # print("#############", calibrated_rbf)
            self.rightbrake_entryfield.config(text=self.calibrated_rbf)
            
            file = open(self.file_path2, "a")
            file.writelines(repr(j) + ',' +repr(self.calibrated_rbf) +"\n")
            file.close()
            
            # Car Testing Status
            self.car_testing_status(self.test_status, LBF=self.calibrated_lbf, RBF=self.calibrated_rbf)
            
            # Code to calibrate Axle Weight values
            file_path = file_path = Find_Directory_Path.resource_path("Calibration_Files\\calibrationConfigurationAWFile.txt")
            mac_address = "AB:CD:EF:12:34:56"
            offset = 320
            coef = 90
            raw_data = self.axle_weight
            value = round((raw_data - offset)/coef, 2)
            if value > 0:
                calibrated_variable_AW = calibrationForAW.write_range_value(file_path, mac_address, value)
                m_AW = calibrated_variable_AW[0]
                c_AW = calibrated_variable_AW[1]
                # calibrated_AW = m_AW*value + c_AW
                self.calibrated_AW_m_c = m_AW*raw_data + c_AW
                self.calibrated_AW = 0
                try:
                    if self.tair_calibrated_AW:
                        self.calibrated_AW = self.calibrated_AW_m_c - self.tair_calibrated_AW
                except:
                    pass
            else:
                # calibrated_AW = value
                self.calibrated_AW = 0
            
            self.calibrated_AW = float(f"{self.calibrated_AW:.2f}")
            # print(m_AW, c_AW, value)
            # print("#############", self.calibrated_AW)
            self.axle_weight_entryfield.config(text=self.calibrated_AW)
            # excelWeightlbl.config(text=axle_weight)
            # self.pages['Page1'].excelWeightlbl.config(text=calibrated_AW)
                
            
            ######################### GAUGE NEEDLE UPDATE on_message EVENT #####################################
            # Updating Gauge needle of Speed for page 2
            # self.speed_list.insert(0, self.rpm)
            # for i in range(len(self.speed_list)):
            #     if len(self.speed_list) > 2:
            #         self.speed_list.pop(2)
            #     else:
            #         pass
            # # print("speedList = ", self.speed_list)
            
            # actual_speed = [self.speed_list[1]]
            # if self.speed_list[0] > self.speed_list[1] and self.speed_list[0] < 250:
            #     for i in range(self.speed_list[0] - self.speed_list[1]):
            #         actual_speed[0] += 1
            #         if actual_speed[0] < 250:
            #             # self.pages['Page2'].speedometer.update_speed(actual_speed[0])
            #             pass
            #         else:
            #             pass
            #         time.sleep(0.0001)
            # elif self.speed_list[1] >= 0:
            #     for i in range(self.speed_list[1] - self.speed_list[0]):
            #         actual_speed[0] -= 1
            #         if actual_speed[0] < 250:
            #             # self.pages['Page2'].speedometer.update_speed(actual_speed[0])
            #             pass
            #         else:
            #             pass
            #         time.sleep(0.0001)
            
            # Updating Gauge needle of Left Break Force on page 1
            # speed_list = [0]
            int_calibrated_lbf = int(self.calibrated_lbf*(6))
            self.lbf_list.insert(0, int_calibrated_lbf)
            for i in range(len(self.lbf_list)):
                if len(self.lbf_list) > 2:
                    self.lbf_list.pop(2)
                else:
                    pass
            # print("lbfList = ", self.lbf_list)
            
            actual_speed = [self.lbf_list[1]]
            if self.lbf_list[0] > self.lbf_list[1] and self.lbf_list[0] < 250:
                for i in range(self.lbf_list[0] - self.lbf_list[1]):
                    actual_speed[0] += 1
                    if actual_speed[0] < 250:
                        # self.pages['Page1'].speedometer.update_speed(actual_speed[0])
                        self.speedometer_left.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            elif self.lbf_list[1] >= 0:
                for i in range(self.lbf_list[1] - self.lbf_list[0]):
                    actual_speed[0] -= 1
                    if actual_speed[0] > 0:
                        # self.pages['Page1'].speedometer.update_speed(actual_speed[0])
                        self.speedometer_left.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            
            # Updating Gauge needle of Right Break Force on page 1
            # speed_list = [0]
            int_calibrated_rbf = int(self.calibrated_rbf*(6))
            if int_calibrated_rbf < 0:
                int_calibrated_rbf = 0
            self.rbf_list.insert(0, int_calibrated_rbf)
            for i in range(len(self.rbf_list)):
                if len(self.rbf_list) > 2:
                    self.rbf_list.pop(2)
                else:
                    pass
            # print("rbfList = ", self.rbf_list)
            
            actual_speed = [self.rbf_list[1]]
            if self.rbf_list[0] > self.rbf_list[1] and self.rbf_list[0] < 250:
                for i in range(self.rbf_list[0] - self.rbf_list[1]):
                    actual_speed[0] += 1
                    if actual_speed[0] < 250:
                        # self.pages['Page1'].speedometer1.update_speed(actual_speed[0])
                        self.speedometer_right.update_speed(actual_speed[0])
                    else:
                        pass
                    time.sleep(0.0001)
            elif self.rbf_list[1] >= 0:
                for i in range(self.rbf_list[1] - self.rbf_list[0]):
                    actual_speed[0] -= 1
                    if actual_speed[0] > 0:
                        # self.pages['Page1'].speedometer1.update_speed(actual_speed[0])
                        self.speedometer_right.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            
            # Updating Gauge needle of Axle Weight on page 1
            # speed_list = [0]
            int_calibrated_AW = int(int(self.calibrated_AW)/10)
            self.axel_weight_list.insert(0, int_calibrated_AW)
            for i in range(len(self.axel_weight_list)):
                if len(self.axel_weight_list) > 2:
                    self.axel_weight_list.pop(2)
                else:
                    pass
            # print("axleWeight = ", self.axel_weight_list)
            
            actual_speed = [self.axel_weight_list[1]]
            if self.axel_weight_list[0] > self.axel_weight_list[1] and 0 <= self.axel_weight_list[0] < 250:
                for i in range(self.axel_weight_list[0] - self.axel_weight_list[1]):
                    actual_speed[0] += 1
                    if actual_speed[0] < 250:
                        # self.pages['Page1'].axle_speedometer.update_speed(actual_speed[0])
                        self.speedometer_axle.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            elif self.axel_weight_list[1] >= 0:
                for i in range(self.axel_weight_list[1] - self.axel_weight_list[0]):
                    actual_speed[0] -= 1
                    if actual_speed[0] > 0:
                        # self.pages['Page1'].axle_speedometer.update_speed(actual_speed[0])
                        self.speedometer_axle.update_speed(actual_speed[0])
                    time.sleep(0.0001)
            
            print('################################ending here########################################')
            
            
        elif msg.topic == "topic2":
            self.pages['Page1'].label2.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic3":
            self.pages['Page2'].label3.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic4":
            self.pages['Page2'].label4.config(text=msg.payload.decode("utf-8"))
    
    
    # Function to define car testing status
    def car_testing_status (self, status_code, LBF, RBF):
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
            self.break_efficiency_and_result(LBF, RBF)
        elif status_code == 5:
            self.testing_status.config(text="Test Failed", foreground='red')
            
            self.status = 'fail'
            
            api_url = f'https://6d26-2401-4900-1c7a-6587-5d75-6ba2-e2df-9aaa.ngrok-free.app/test/brake/{self.id}/{self.status}'  # Replace with your actual API endpoint
            # payload = {}
            try:
                response = requests.post(api_url)
                # print(response.text,"api")
                if response.status_code == 200:
                    # print('Searched successfully!') 
                    datas = response.json()
                    print(datas)
                else:
                    print(f'Error: Not Found')
                    
            except requests.RequestException as e:
                print(f'Error: {e}')
    
    # Run this function at level 4 to calculate the break efficiency and test result
    def break_efficiency_and_result(LBF, RBF):
        pass




import tkinter as tk

# app = tk.Tk()

# mqtt_instance = mqtt_object(frame=app)


# app.mainloop()









class mqtt_RPM_object:
    def __init__(self, frame, id):
        
        self.id = id
        self.frame = frame
        
        
        # Define variable to update needle position
        self.speed_list = [0]
        
        # MQTT All Process Code Is Here
        mqttBroker = "3.110.187.253"
        client = mqtt.Client("Smartphone")
        client.on_message = self.on_mqttMessage
        client.on_connect = self.on_mqttConnect
        client.connect(mqttBroker,1883,60)
        client.loop_start()
        
        self.testing_status= tk.Label(self.frame,text='pass', bg="#0E0E0E",fg='yellow',font=('','12'))
        self.testing_status.place(x=1000, y=105)
        
        self.speedometer_rpm = needle.Speedometer(self.frame, parent_width=322, parent_height=322, min_value=0, max_value=40, oval_radius_width=320, oval_radius_height=320, center_x=161, center_y=161, num_ticks_radius=130, ticks_radius=130, needle_quad_height=120, needle_quad_width=30, needle_quad_height_y3_y4 = 250, gauge_info_text="", gauge_info_text_x = 155, gauge_info_text_y = 230)
        self.speedometer_rpm.place(x=920, y=220)
        self.speedometer_rpm.update_speed(0)
        
        Image1.image_handler(self.frame, 'Images/speedo_base.png', 340, 80, 915, 468)
        # entryfield left brake
        self.rpm_entryField = tk.Label(self.frame, width=10,text='0', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        self.rpm_entryField.place(x=1040, y=490)
        
    
    
    # Function for increasment of j For Time Graph
    def time_increasement(self):
        global j
        if j<300.1:
            j +=0.1
    
    def on_mqttConnect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("48:27:E2:45:64:1A")
    
    
    def on_mqttMessage(self, clien, userdata, msg):
        # Cleaning all data from rangeValues.txt file
        rangeValuesForRPM=Find_Directory_Path.resource_path('Range_Values_Files\\rangeValuesForRPM.txt')

        rangeValues_paths = [rangeValuesForRPM]
        for rangeValues_path in rangeValues_paths:
            with open(rangeValues_path, "w") as file:
                file.write("")
        
        
        # Here you can update the labels based on the MQTT message
        if msg.topic == "48:27:E2:45:64:1A":
            # self.pages['Page1'].label1.config(text=msg.payload.decode("utf-8"))
            message0 = str(msg.payload.decode("utf-8"))
            m_in = json.loads(message0)
            test_status = int(m_in['d']['Test Status'])
            rpm = int(m_in['d']['rpm'])
            
            # Calling back function to increase time    
            self.time_increasement()
            print(j)
            
            
            # Car Testing Status
            self.car_testing_status(test_status)
            
            
            ######################### GAUGE NEEDLE UPDATE on_message EVENT #####################################
            # Updating Gauge needle of RPM
            self.speed_list.insert(0, rpm)
            for i in range(len(self.speed_list)):
                if len(self.speed_list) > 2:
                    self.speed_list.pop(2)
                else:
                    pass
            print("speedList = ", self.speed_list)
            
            actual_speed = [self.speed_list[1]]
            if self.speed_list[0] > self.speed_list[1] and self.speed_list[0] < 250:
                for i in range(self.speed_list[0] - self.speed_list[1]):
                    actual_speed[0] += 1
                    if actual_speed[0] < 250:
                        # self.pages['Page2'].speedometer.update_speed(actual_speed[0])
                        self.speedometer_rpm.update_speed(actual_speed[0])
                    else:
                        pass
                    time.sleep(0.0001)
            elif self.speed_list[1] < 250:
                for i in range(self.speed_list[1] - self.speed_list[0]):
                    actual_speed[0] -= 1
                    if actual_speed[0] < 250:
                        # self.pages['Page2'].speedometer.update_speed(actual_speed[0])
                        self.speedometer_rpm.update_speed(actual_speed[0])
                    else:
                        pass
                    time.sleep(0.0001)
            
        elif msg.topic == "topic2":
            self.pages['Page1'].label2.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic3":
            self.pages['Page2'].label3.config(text=msg.payload.decode("utf-8"))
        elif msg.topic == "topic4":
            self.pages['Page2'].label4.config(text=msg.payload.decode("utf-8"))
    
    
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
            
            self.status = 'fail'
            
            api_url = f'https://228e-2401-4900-1c1b-67bb-7d2f-432f-b851-5fcd.ngrok-free.app/test/brake/{self.id}/{self.status}'  # Replace with your actual API endpoint
            # payload = {}
            try:
                response = requests.post(api_url)
                # print(response.text,"api")
                if response.status_code == 200:
                    # print('Searched successfully!') 
                    datas = response.json()
                    print(datas)
                else:
                    print(f'Error: Not Found')

            except requests.RequestException as e:
                print(f'Error: {e}')
