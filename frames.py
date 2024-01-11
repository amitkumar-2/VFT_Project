import tkinter as tk
from PIL import Image, ImageTk
import requests
from threading import Thread
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from handlers import Image1
from config import settings
from handlers import api_model, mqtt_handler
# import Find_Directory_Path
from Find_Directory_Path import resource_path


m_base_url = settings.m_base_url

class VFTApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a single frame
        self.frame = tk.Frame(root, width=1300, height=750, bg="#0E0E0E")
        self.frame.pack()

        # Display the background image
        # self.show_image('Images/crbg2.png', 1400, 750, 0, 0, "black")
        Image1.image_handler(self.frame, 'Images/crbg2.png', 1400, 750, 0, 0, "#0E0E0E")

        # Set up the initial content (vft head, welcome heading, etc.)
        self.setup_initial_content()

    def setup_initial_content(self):
        Image1.image_handler(self.frame, 'Images/vftgft.png', 900, 120, 40, 40, "#0E0E0E")
        Image1.image_handler(self.frame, 'Images/WVT.png', 500, 100, 60, 280, "#0E0E0E")

        notrgstr = tk.Label(self.frame, text='New user ?', bg="#0E0E0E", fg='white', font=('Helvetica', 12))
        notrgstr.place(x=80, y=450)

        fgtpsd = tk.Label(self.frame, text='Setup', bg="#0E0E0E", fg='yellow', font=('Helvetica', 12))
        fgtpsd.place(x=170, y=450)
        fgtpsd.bind("<Button-1>", self.on_setup_click)

        loginbtn = Image.open(resource_path('Images/login.png'))
        width, height = 180, 42
        loginbtn_resize = loginbtn.resize((width, height))
        self.loginbtn_head = ImageTk.PhotoImage(loginbtn_resize)

        button = tk.Button(self.frame, image=self.loginbtn_head, bg="#0E0E0E", command=self.switch_to_signin,
                           borderwidth=0, relief='flat', activebackground="#0E0E0E", activeforeground='black')
        button.place(x=400, y=500)

    def on_setup_click(self, event):
        print('SETUP')

    def switch_to_signin(self):
        # Destroy the current frame
        self.frame.destroy()

        # Create and display the SignInApp frame
        # signin_frame = SignInApp(self.root)
        break_test = Break_Test(self.root,id='A3', centre='CTI')

class SignInApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a frame
        self.frame = tk.Frame(root, width=1500, height=750)
        self.frame.pack()

        # Load and display the background image
        Image1.image_handler(self.frame, 'Images/newcrbg.png', 1600, 750, 0, 0,command=None)

        # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_initial_content()

    def setup_initial_content(self):
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/signin.png', 170, 60, 60, 160, self.on_SIGNIN_click)
        Image1.image_handler(self.frame, 'Images/userid.png', 300, 60, 60, 240)
        Image1.image_handler(self.frame, 'Images/psswrd.png', 300, 60, 60, 310)
        Image1.image_handler(self.frame, 'Images/signbtn.png', 180, 42, 150, 400, self.on_SIGNIN_click)

        # Create Entry fields
        self.entryFieldid = tk.Entry(self.frame, width=20, font=("Arial", 13), fg='black', bg='#E5E5E5')
        self.entryFieldid.place(x=90, y=268)

        self.entryField_passwd = tk.Entry(self.frame, width=20, font=("Arial", 13), fg='black', bg='#E5E5E5', show='*')
        self.entryField_passwd.place(x=90, y=335)

        # Create labels for 'Not Registered?' and 'Forgot Password?'
        notrgstr = tk.Label(self.frame, text='Not Registered ?', bg="#0E0E0E", fg='white', font=('Helvetica', 12))
        notrgstr.place(x=60, y=520)
        notrgstr.bind("<Button-1>", self.on_text_click1)

        fgtpsd = tk.Label(self.frame, text='Forgot Password ?', bg="#0E0E0E", fg='yellow', font=('Helvetica', 12))
        fgtpsd.place(x=185, y=520)
        fgtpsd.bind("<Button-1>", self.on_text_click2)

    def on_SIGNIN_click(self):
        # Get username and password from entry fields
        username=  str(self.entryFieldid.get())
        password =  str(self.entryField_passwd.get())
        # username = 'amzad'
        # password = 'abc123'
        center = "CTI1"

        # Make an API request with the provided username and password
        api_url = f'{m_base_url}/user/loginpc/{username}/{password}/{center}'  # Replace with your actual API endpoint
        payload = {'username': username, 'password': password, 'center': 'CTI1'}
        print(username,"user")
        print(api_url,"url")
        try:
            response = requests.get(api_url, data=payload)

            if response.status_code == 200:
                print('Signed in successfully!')
                
        # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                ScanApp(self.root)

                # You can handle further actions here, e.g., navigate to a new frame
            else:
                print(f'Error: {response.status_code,response.text}')
        except requests.RequestException as e:
            print(f'Error: {e}')

    def on_text_click1(self, event):
        print('Not registered')

    def on_text_click2(self, event):
        print('Forgot password')


class ScanApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a frame
        self.frame = tk.Frame(root, width=1500, height=750)
        self.frame.pack()

        # Load and display the background image
        Image1.image_handler(self.frame, 'Images/newcrbg.png', 1600, 750, 0, 0)

        # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_scan_content()

    def setup_scan_content(self):
        

        # VFT heading for scanning page
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/waiting.png', 600, 50, 40, 200)
        Image1.image_handler(self.frame, 'Images/dot.png', 70, 15, 300, 250 )
        Image1.image_handler(self.frame, 'Images/scan.png', 180, 42, 50, 380 , self.on_scan_click)
        Image1.image_handler(self.frame, 'Images/vehicleno.png', 300, 60,40, 470 )
        Image1.image_handler(self.frame, 'Images/search.png', 180, 42,340,490 , self.on_search_click)
         # Start scanning text
        self.scaningtext_scan = tk.Label(self.frame, text='Start Scanning Vehicle Number Plate', bg='#0E0E0E', fg='white', font=('Helvetica', 12))
        self.scaningtext_scan.place(x=40, y=340)
       #  enter manually 
        scaningtext = tk.Label(self.frame,text='or Enter Manually',bg='#0E0E0E',fg='white',font=('Helvetica',12))
        scaningtext.place(x=40,y=440)
       # vehicleidid entry field
        self.entryField = tk.Entry(self.frame, width=20, font=("Arial", 13), fg='black', bg='#E5E5E5')
        self.entryField.place(x=80, y=495)

    def on_scan_click(self):
        print('Scanning...')  # Add your scanning logic here

    def on_search_click(self):
        vehicalnumber=  str(self.entryField.get())
        # vehicalnumber='DL 3C AU 0375'
        vehicaltype = '4'
        id = 'A1'

        testcenter = "CTI1"
        name="Rahul"
        fueltype = "Diesel"
        date= "Sat, 18 Nov 2023 15:30:45 GMT"
        appointmentscol= "no"


      # Make an API request with the provided username and password
        api_url = f'{m_base_url}/authorize/vehicle/{vehicalnumber}'  # Replace with your actual API endpoint
        payload = {'vehicalnumber':vehicalnumber}
         
        
        try:
            response = requests.get(api_url,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                print(datas)
                 # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                vehicleDetail(self.root,datas)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')

class vehicleDetail:
    def __init__(self, root,datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root, width=1500, height=750)
        self.frame.pack()
    # Load and display the background image
        Image1.image_handler(self.frame, 'Images/newbg5.png', 1600, 750, 0, 0) 
        
        

        #Extract data
        self.name = datas['payload']['name']
        self.regnNo = datas['payload']['vehicalnumber']
        self.regdUpto = datas['payload']['date']
        self.RC = datas['payload']['rcstatus']
        self.fuel = datas['payload']['fueltype']
        self.chassis = datas['payload']['chassis']
        self.engNo = datas['payload']['enginenumber']
        self.mfg = datas['payload']['mfgdate']
        self.wt = datas['payload']['wt']
        self.vtype = datas['payload']['vehicaltype']
        self.mfr = datas['payload']['mfr']
        self.model = datas['payload']['model']
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']
        print(self.center)
    # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_scan_content(datas)

    def setup_scan_content(self,datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/Vehicledetail.png', 500, 50, 60, 150)
        Image1.image_handler(self.frame, 'Images/whitebord.png', 650, 380, 10, 250 )
        self.show_image1(resource_path('Images/redline.png'), 400,20,30,400)
        Image1.image_handler(self.frame, 'Images/strttesting.png', 180, 42, 900, 550 , command=lambda:self.on_strttesting_click(datas=datas))
        
       
       # Text on white board
        # 1st line
        maintext = tk.Label(self.frame,text='Following are the details:',bg='#E5E5E5',fg='black',font=('Helvetica',12))
        maintext.place(x=30,y=275)

        # 2nd line
        text1 = tk.Label(self.frame,text='Owner name:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text1.place(x=30,y=305)
        self.text1_input = tk.Label(self.frame,text=self.name,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text1_input.place(x=140,y=305)
        # 3rd line
        text2 = tk.Label(self.frame,text='Regn. No:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text2.place(x=30,y=330)
        self.text2_input = tk.Label(self.frame,text=self.regnNo,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text2_input.place(x=140,y=330)
        # 4th line
        text3 = tk.Label(self.frame,text='Regd. upto:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text3.place(x=30,y=355)
        self.text3_input = tk.Label(self.frame,text=self.regdUpto,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text3_input.place(x=140,y=355)
        # 5th line
        text4 = tk.Label(self.frame,text='RC status:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text4.place(x=30,y=380)
        self.text4_input = tk.Label(self.frame,text=self.RC,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text4_input.place(x=140,y=380)
       

        # 6th line
        text5 = tk.Label(self.frame,text='Fuel Type:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text5.place(x=30,y=420)
        self.text5_input = tk.Label(self.frame,text=self.fuel,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text5_input.place(x=140,y=420)
        # 7th line
        text6 = tk.Label(self.frame,text='Chassis No:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text6.place(x=30,y=444)
        self.text6_input = tk.Label(self.frame,text=self.chassis,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text6_input.place(x=140,y=444)
        #  # 8th line
        text7 = tk.Label(self.frame,text='Engine No.:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text7.place(x=30,y=465)
        self.text7_input = tk.Label(self.frame,text=self.engNo,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text7_input.place(x=140,y=465)
        # # 9th line
        text8 = tk.Label(self.frame,text='MFG. DT. No.:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text8.place(x=30,y=489)
        self.text8_input = tk.Label(self.frame,text=self.mfg,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text8_input.place(x=140,y=489)
        # 10th line
        text9 = tk.Label(self.frame,text='Unladen WT:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text9.place(x=30,y=510)
        self.text9_input = tk.Label(self.frame,text=self.wt,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text9_input.place(x=140,y=510)
        # # 11th line
        text10 = tk.Label(self.frame,text='Vehicle Type:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text10.place(x=30,y=532)
        self.text10_input = tk.Label(self.frame,text=self.vtype,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text10_input.place(x=140,y=532)
        # # 12th line
        text11 = tk.Label(self.frame,text='MFR:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text11.place(x=30,y=555)
        self.text11_input = tk.Label(self.frame,text=self.mfr,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text11_input.place(x=140,y=555)
        # # # 13th line
        text12 = tk.Label(self.frame,text='Model:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',12,'italic'))
        text12.place(x=30,y=576)
        self.text12_input = tk.Label(self.frame,text=self.model,bg='#E5E5E5',fg='black',font=('Helvetica',12,'italic','bold'))
        self.text12_input.place(x=140,y=576) 

    def show_image1(self, image_path, width, height, x, y):
            img = Image.open(image_path)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.frame, image=img_tk, bg='#E5E5E5')
            img_label.image = img_tk
            img_label.place(x=x, y=y)

            
    def on_strttesting_click(self, datas):
        
        api_url = f'{m_base_url}/test/check/{self.id}/{self.center}'  # Replace with your actual API endpoint
        # payload = {}
         
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                # datas = response.json()
                # print(datas)
                 # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                start_testing(self.root, datas)
            else:
                print(f'Error: Not Found')
                # self.manual_label =tk.Label(self.frame,text="Manual Test is Running...",bg='#E5E5E5',fg='red',font=('Helvetica',14,'bold','italic'))
                # self.manual_label.place(x=300,y=275)
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))
                self.frame.destroy()
                start_testing(self.root, datas)

        except requests.RequestException as e:
            print(f'Error: {e}')

class start_testing:
    def __init__(self, root, datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root, width=1300, height=750)
        self.frame.pack()
    # Load and display the background image
        Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0) 
        # EXTRACT DATA
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']

     # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_test_content(datas=datas)

        self.start_thread()

    def setup_test_content(self, datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/logocompleting.png', 540, 70, 40, 170)
        Image1.image_handler(self.frame, 'Images/whiteline.png', 20, 470, 650, 260)
        # Image1.image_handler(self.frame, 'Images/strttesting.png', 180, 80, 800, 600, command=lambda:self.stop_thread())
        
        
        labels=['Headlamp Assembly','Top Light','Supressure Cap','Horn','Silencer', 'Wiper Blades','Wiper System']
         
        # Create labels dynamically
        label_y_position = 275
        for label_text in labels:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=120, y=label_y_position)
            label_y_position += 70 
       
         # Print 'wheel.png' images 10 times at different y positions
        for i in range(7):
            y_position = 270 + i * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30, 50, y_position)
        
        # Print 'DETAILS.png' button 10 times at different y positions
        # for i in range(5):
        #     y_position = 270 + i * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 500, y_position, command=lambda:self.on_detail_click(x=500, y=y_position, datas=datas))
    # SECOND PART
        for j in range(6):
            y_position = 270 + j * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30,700, y_position)
        # for j in range(4):
        #     y_position =270 + j * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 1130, y_position, command=lambda:self.on_detail_click(x=1130, y=y_position, datas=datas))
         # Create labels2 dynamically
        labels2=['Dashboard','Safety Glass', 'Stop Light','Parking Light','Fog Lamp','Warning Light']
        label_y_position = 275
        for label_text in labels2:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=770, y=label_y_position)
            label_y_position += 70
        
        Image1.image_handler(self.root, 'Images/next.png', 180, 50, 1200, 700,command=lambda:(self.stop_thread(), self.Go_To_manual_testing_1(datas)))
    
    
    #  detail function
    def m_param_detail(self, datas, m_test_name, id, topHeading, m_page):
        topHeading = topHeading
        try:
            self.stop_thread()
            self.frame.destroy()
            Detail_page(self.root, datas=datas, topHeading=topHeading, m_test_name = m_test_name, id = id, m_page=m_page)
        except requests.RequestException as e:
            print(f'Error: {e}')
    

        
    

    def automatic_fetching(self, id, center):
        
        api_url = f'{m_base_url}/test/checkdata/{id}/{center}'  # Replace with your actual API endpoint
        # payload = {}
        # print('datas',datas)
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                #Manualy insert the data in response back datas
                datas['payload']['testcenter'] = center
                print(datas)
                print(datas['payload']['testheadlamp'])
               
            # TEST CASE 1:
                if datas['payload']['testheadlamp'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='headlamp', id=self.id, topHeading='Headlamp Assembly', m_page=0))
                elif datas['payload']['testheadlamp'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='headlamp', id=self.id, topHeading='Headlamp Assembly', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270)
            # TEST CASE 2:
                if datas['payload']['testtoplight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='toplight', id=self.id, topHeading='Top Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/right.png')
                elif datas['payload']['testtoplight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='toplight', id=self.id, topHeading='Top Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340)
             # TEST CASE 3:
                if datas['payload']['testsupressor'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='Supressor', id=self.id, topHeading=' Supressor', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/right.png')
                elif datas['payload']['testsupressor'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='Supressor', id=self.id, topHeading=' Supressor', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410)
             # TEST CASE 4:
                if datas['payload']['testhorn'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='horn', id=self.id, topHeading='Horn ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/right.png')
                elif datas['payload']['testhorn'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='horn', id=self.id, topHeading='Horn ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480)
            # TEST CASE 5:
                if datas['payload']['testsilencer'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='exhaust', id=self.id, topHeading='Silencer ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/right.png')
                elif datas['payload']['testsilencer'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='exhaust', id=self.id, topHeading='Silencer ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550)
            # TEST CASE 6:
                if datas['payload']['testwiperblade'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='wiperblade', id=self.id, topHeading=' Wiper Blade', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/right.png')
                elif datas['payload']['testwiperblade'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='wiperblade', id=self.id, topHeading=' Wiper Blade', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620)
            # TEST CASE 7:
                if datas['payload']['testwipersystem'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='wipersystem', id=self.id, topHeading=' Wiper System', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/right.png')
                elif datas['payload']['testwipersystem'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='wipersystem', id=self.id, topHeading=' Wiper System', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680)
             # TEST CASE 8:
                if datas['payload']['testdashboard'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='dashboard', id=self.id, topHeading='Dashboard ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/right.png')
                elif datas['payload']['testdashboard'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='dashboard', id=self.id, topHeading='Dashboard ', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270)   
             # TEST CASE 9:
                if datas['payload']['testsafetyglass'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetyglasses', id=self.id, topHeading=' Safety Glass', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/right.png')
                elif datas['payload']['testsafetyglass'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetyglasses', id=self.id, topHeading=' Safety Glass', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340)
                
                # TEST CASE 10:
                if datas['payload']['teststoplight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='stoplight', id=self.id, topHeading='Stop Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/right.png')
                elif datas['payload']['teststoplight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='stoplight', id=self.id, topHeading='Stop Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410)
                
                # TEST CASE 11:
                if datas['payload']['testparkinglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkinglight', id=self.id, topHeading='Parking Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480, image_path_02='Images/right.png')
                elif datas['payload']['testparkinglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkingligth', id=self.id, topHeading='Parking Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480)
                
                # TEST CASE 12:
                if datas['payload']['testfoglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='foglight', id=self.id, topHeading='Fog Lamp', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550, image_path_02='Images/right.png')
                elif datas['payload']['testfoglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='foglight', id=self.id, topHeading='Fog Lamp', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550)
                
                
                # TEST CASE 13:
                if datas['payload']['testwarninglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='warninglight', id=self.id, topHeading='Warning Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620, image_path_02='Images/right.png')
                elif datas['payload']['testwarninglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='warninglight', id=self.id, topHeading='Warning Light', m_page=0))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620)
                
                
                  # Destroy the current frame
                # self.frame.destroy()
        # Create and display the SignInApp frame
                # start_testing(self.root)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    def start_thread(self):
        self.is_running = True  # Set the flag to start the thread
        self.thread = Thread(target=self.run_thread)
        self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Set the flag to stop the thread

    def run_thread(self):
        while self.is_running:
            print("Thread is running...")
            self.thread = Thread(target=self.automatic_fetching(id=self.id, center=self.center))
            time.sleep(2)
        
        print("Thread is stopped.")
    
    def Go_To_manual_testing_1(self, datas):
        self.frame.destroy()
        manual_testing_1(self.root, datas)



class manual_testing_1:
    def __init__(self, root, datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root, width=1300, height=750)
        self.frame.pack()
    # Load and display the background image
        Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0) 
        # EXTRACT DATA
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']

     # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_test_content(datas=datas)

        self.start_thread()

    def setup_test_content(self, datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/logocompleting.png', 540, 70, 40, 170)
        Image1.image_handler(self.frame, 'Images/whiteline.png', 20, 470, 650, 260)
        # Image1.image_handler(self.frame, 'Images/strttesting.png', 180, 80, 800, 600, command=lambda:self.stop_thread())
        
        
        labels=['Number Plate','Marker Lamp','Direction Indicator','Hazard Warning Signal','Rear View Mirror', 'Service Brakes','Parking Brakes']
         
        # Create labels dynamically
        label_y_position = 275
        for label_text in labels:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=120, y=label_y_position)
            label_y_position += 70 
       
        # Print 'wheel.png' images 10 times at different y positions
        for i in range(7):
            y_position = 270 + i * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30, 50, y_position)
        
        # Print 'DETAILS.png' button 10 times at different y positions
        # for i in range(5):
        #     y_position = 270 + i * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 500, y_position, command=lambda:self.on_detail_click(x=500, y=y_position, datas=datas))
    # SECOND PART
        for j in range(6):
            y_position = 270 + j * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30,700, y_position)
        # for j in range(4):
        #     y_position =270 + j * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 1130, y_position, command=lambda:self.on_detail_click(x=1130, y=y_position, datas=datas))
         # Create labels2 dynamically
        labels2=['Steering Gear','Joint Play', 'Speedometer','RUPD','LUPD','FASTag']
        label_y_position = 275
        for label_text in labels2:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=770, y=label_y_position)
            label_y_position += 70
        
        Image1.image_handler(self.root, 'Images/back.png', 180, 50, 1000, 700,command=lambda:(self.stop_thread(), self.Start_Testing(datas)))
        
        Image1.image_handler(self.root, 'Images/next.png', 180, 50, 1200, 700,command=lambda:(self.stop_thread(), self.Go_To_manual_testing_2(datas)))

    
    #  detail function
    def m_param_detail(self, datas, m_test_name, id, topHeading, m_page):
        topHeading = topHeading
        try:
            self.stop_thread()
            self.frame.destroy()
            Detail_page(self.root, datas=datas, topHeading=topHeading, m_test_name = m_test_name, id = id, m_page=m_page)
        except requests.RequestException as e:
            print(f'Error: {e}')
    

        
    

    def automatic_fetching(self, id, center):
        
        api_url = f'{m_base_url}/test/checkdata/{id}/{center}'  # Replace with your actual API endpoint
        # payload = {}
        # print('datas',datas)
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                #Manualy insert the data in response back datas
                datas['payload']['testcenter'] = center
                print(datas)
                print(datas['payload']['testheadlamp'])
               
            # TEST CASE 1:
                if datas['payload']['testnumberplatelight'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='numberplate', id=self.id, topHeading='Number Plate', m_page=1))
                elif datas['payload']['testnumberplatelight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='numberplate', id=self.id, topHeading='Number Plate', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270)
            # TEST CASE 2:
                if datas['payload']['testoutlinemarkerlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='markerlight', id=self.id, topHeading='Marker Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/right.png')
                elif datas['payload']['testoutlinemarkerlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='markerlight', id=self.id, topHeading='Marker Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340)
             # TEST CASE 3:
                if datas['payload']['testdirectionlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='directionlight', id=self.id, topHeading='Direction Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/right.png')
                elif datas['payload']['testdirectionlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='directionlight', id=self.id, topHeading='Direction Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410)
             # TEST CASE 4:
                if datas['payload']['testhazardlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='hazardlight', id=self.id, topHeading='Hazard Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/right.png')
                elif datas['payload']['testhazardlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='hazardlight', id=self.id, topHeading='Hazard Light', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480)
            # TEST CASE 5:
                if datas['payload']['testrearmirror'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='rearmirror', id=self.id, topHeading='Rear Mirror', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/right.png')
                elif datas['payload']['testrearmirror'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='rearmirror', id=self.id, topHeading='Rear Mirror', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550)
            # TEST CASE 6:
                if datas['payload']['testbrakingmanual'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='brakingmanual', id=self.id, topHeading='Braking Manual', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/right.png')
                elif datas['payload']['testbrakingmanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='brakingmanual', id=self.id, topHeading='Braking Manual', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620)
            # TEST CASE 7:
                if datas['payload']['testparkingbrakingmanual'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkingbrakingmanual', id=self.id, topHeading='Parking Brake', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/right.png')
                elif datas['payload']['testparkingbrakingmanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkingbrakingmanual', id=self.id, topHeading='Parking Brake', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680)
             # TEST CASE 8:
                if datas['payload']['teststeering'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='steering', id=self.id, topHeading='Steering', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/right.png')
                elif datas['payload']['teststeering'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='steering', id=self.id, topHeading='Steering', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270)   
             # TEST CASE 9:
                if datas['payload']['testjointplay'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='jointplay', id=self.id, topHeading='Joint Play', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/right.png')
                elif datas['payload']['testjointplay'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='jointplay', id=self.id, topHeading='Joint Play', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340)
                
                # TEST CASE 10:
                if datas['payload']['testspeedometermanual'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedometermanual', id=self.id, topHeading='Speedometer Manual', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/right.png')
                elif datas['payload']['testspeedometermanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedometermanual', id=self.id, topHeading='Speedometer Manual', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410)
                
                # TEST CASE 11:
                if datas['payload']['testrupd'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='rupd', id=self.id, topHeading='RUPD', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480, image_path_02='Images/right.png')
                elif datas['payload']['testrupd'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='rupd', id=self.id, topHeading='RUPD', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 480)
                
                # TEST CASE 12:
                if datas['payload']['testlupd'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='LUPD', id=self.id, topHeading='LUPD', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550, image_path_02='Images/right.png')
                elif datas['payload']['testlupd'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='LUPD', id=self.id, topHeading='LUPD', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 550)
                
                
                # TEST CASE 13:
                if datas['payload']['testfastag'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='fastag', id=self.id, topHeading='FATSag', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620, image_path_02='Images/right.png')
                elif datas['payload']['testfastag'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='fastag', id=self.id, topHeading='FATSag', m_page=1))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 620)
                
                  # Destroy the current frame
                # self.frame.destroy()
        # Create and display the SignInApp frame
                # start_testing(self.root)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    def start_thread(self):
        self.is_running = True  # Set the flag to start the thread
        self.thread = Thread(target=self.run_thread)
        self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Set the flag to stop the thread

    def run_thread(self):
        while self.is_running:
            print("Thread is running...")
            self.thread = Thread(target=self.automatic_fetching(id=self.id, center=self.center))
            time.sleep(2)
        
        print("Thread is stopped.")
    
    def Start_Testing(self, datas):
        self.frame.destroy()
        start_testing(self.root, datas)
    
    def Go_To_manual_testing_2(self, datas):
        self.frame.destroy()
        manual_testing_2(self.root, datas)





class manual_testing_2:
    def __init__(self, root, datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root, width=1300, height=750)
        self.frame.pack()
    # Load and display the background image
        Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0) 
        # EXTRACT DATA
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']

     # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_test_content(datas=datas)

        self.start_thread()

    def setup_test_content(self, datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)
        Image1.image_handler(self.frame, 'Images/logocompleting.png', 540, 70, 40, 170)
        Image1.image_handler(self.frame, 'Images/whiteline.png', 20, 470, 650, 260)
        # Image1.image_handler(self.frame, 'Images/strttesting.png', 180, 80, 800, 600, command=lambda:self.stop_thread())
        
        
        labels=['Others','Wheel Chair','VLT','HSRP','Battery', 'Seatbelt','Spead Governer']
        
        
         
        # Create labels dynamically
        label_y_position = 275
        for label_text in labels:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=120, y=label_y_position)
            label_y_position += 70 
       
         # Print 'wheel.png' images 10 times at different y positions
        for i in range(7):
            y_position = 270 + i * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30, 50, y_position)
        
        # Print 'DETAILS.png' button 10 times at different y positions
        # for i in range(5):
        #     y_position = 270 + i * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 500, y_position, command=lambda:self.on_detail_click(x=500, y=y_position, datas=datas))
    # SECOND PART
        for j in range(3):
            y_position = 270 + j * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 30, 30,700, y_position)
        # for j in range(4):
        #     y_position =270 + j * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 1130, y_position, command=lambda:self.on_detail_click(x=1130, y=y_position, datas=datas))
         # Create labels2 dynamically
        labels2=['Spray Suppression','Tyres', 'Reflective Tapes']

        
        label_y_position = 275
        for label_text in labels2:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=770, y=label_y_position)
            label_y_position += 70
        
        Image1.image_handler(self.root, 'Images/back.png', 180, 50, 1000, 700,command=lambda:(self.stop_thread(), self.Go_To_manual_testing_1(datas)))
        
        # Image1.image_handler(self.root, 'Images/next.png', 180, 50, 1200, 700,command=lambda:(self.stop_thread(), self.Go_To_Break_Test()))
    
    
    #  detail function
    def m_param_detail(self, datas, m_test_name, id, topHeading, m_page):
        topHeading = topHeading
        try:
            self.stop_thread()
            self.frame.destroy()
            Detail_page(self.root, datas=datas, topHeading=topHeading, m_test_name = m_test_name, id = id, m_page=m_page)
        except requests.RequestException as e:
            print(f'Error: {e}')
    

        
    

    def automatic_fetching(self, id, center):
        
        api_url = f'{m_base_url}/test/checkdata/{id}/{center}'  # Replace with your actual API endpoint
        # payload = {}
        # print('datas',datas)
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                #Manualy insert the data in response back datas
                datas['payload']['testcenter'] = center
                print(datas)
                print(datas['payload']['testheadlamp'])
               
            # TEST CASE 1:
                if datas['payload']['testothers'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='others', id=self.id, topHeading='Others', m_page=2))
                elif datas['payload']['testothers'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='others', id=self.id, topHeading='Others', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 270)
            # TEST CASE 2:
                if datas['payload']['testwheel'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='wheel', id=self.id, topHeading='Wheel', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/right.png')
                elif datas['payload']['testwheel'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='wheel', id=self.id, topHeading='Wheel', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 340)
             # TEST CASE 3:
                if datas['payload']['testvlt'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='vlt', id=self.id, topHeading='VLT', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/right.png')
                elif datas['payload']['testvlt'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='vlt', id=self.id, topHeading='VLT', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 410)
             # TEST CASE 4:
                if datas['payload']['testhsrp'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='hsrp', id=self.id, topHeading='HSRP', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/right.png')
                elif datas['payload']['testhsrp'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 480,command=lambda:self.m_param_detail(datas=datas, m_test_name='hsrp', id=self.id, topHeading='HSRP', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 480)
            # TEST CASE 5:
                if datas['payload']['testbattery'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='battery', id=self.id, topHeading='Battery', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/right.png')
                elif datas['payload']['testbattery'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 550,command=lambda:self.m_param_detail(datas=datas, m_test_name='battery', id=self.id, topHeading='Battery', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 550)
            # TEST CASE 6:
                if datas['payload']['testsafetybelt'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetybelt', id=self.id, topHeading='Safety Belt', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/right.png')
                elif datas['payload']['testsafetybelt'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 620,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetybelt', id=self.id, topHeading='Safety Belt', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 620)
            # TEST CASE 7:
                if datas['payload']['testspeedgoverner'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedgoverner', id=self.id, topHeading='Speed Governer', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/right.png')
                elif datas['payload']['testspeedgoverner'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 500, 680,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedgoverner', id=self.id, topHeading='Speed Governer', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 450, 680)
             # TEST CASE 8:
                if datas['payload']['testspray'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='spray', id=self.id, topHeading='Spray', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/right.png')
                elif datas['payload']['testspray'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 270,command=lambda:self.m_param_detail(datas=datas, m_test_name='spray', id=self.id, topHeading='Spray', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 270)   
             # TEST CASE 9:
                if datas['payload']['testtyres'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='tyres', id=self.id, topHeading='Tyres', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/right.png')
                elif datas['payload']['testtyres'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 340,command=lambda:self.m_param_detail(datas=datas, m_test_name='tyres', id=self.id, topHeading='Tyres', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 340)
                
                # TEST CASE 10:
                if datas['payload']['testretro'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='retro', id=self.id, topHeading='Retro', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/right.png')
                elif datas['payload']['testretro'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 130, 30, 1130, 410,command=lambda:self.m_param_detail(datas=datas, m_test_name='retro', id=self.id, topHeading='Retro', m_page=2))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 30, 30, 1080, 410)
                
                # How next button after completed manual test
                if datas['payload']['stage'] == 2:
                    # Image1.image_handler(self.frame, 'Images/strttesting.png', 180, 50, 1200, 700, command=lambda: [self.stop_thread(), self.Go_To_Break_Test()])
                    Image1.image_handler(self.root, 'Images/strttesting.png', 180, 50, 1200, 700,command=lambda:(self.stop_thread(), self.Go_To_Break_Test()))
                else:
                    # Manual Test Not completed label
                    m_test_not_completed = tk.Label(self.frame, text="Manual test is Ongoing", bg='#0E0E0E', fg='yellow', font=('', 18, 'bold'))
                    m_test_not_completed.place(x=1000, y=200)
                
                  # Destroy the current frame
                # self.frame.destroy()
        # Create and display the SignInApp frame
                # start_testing(self.root)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    def start_thread(self):
        self.is_running = True  # Set the flag to start the thread
        self.thread = Thread(target=self.run_thread)
        self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Set the flag to stop the thread

    def run_thread(self):
        while self.is_running:
            print("Thread is running...")
            self.thread = Thread(target=self.automatic_fetching(id=self.id, center=self.center))
            time.sleep(2)
        
        print("Thread is stopped.")
    
    def Go_To_manual_testing_1(self, datas):
        self.frame.destroy()
        manual_testing_1(self.root, datas)
    
    def Go_To_Break_Test(self):
        self.frame.destroy()
        Break_Test(self.root, self.id, self.center)








class Detail_page:
    def __init__(self, root, datas, topHeading, m_test_name, id, m_page):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
    # Create a frame
        self.frame = tk.Frame(root, width=1300, height=750)
        self.frame.pack()

        # print("Data is Here: ", hdlp_datas)

        # top Heading variable defined
        self.topHeading = topHeading

    # Load and display the background image        
        Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content(datas=datas, m_test_name = m_test_name, id = id, m_page=m_page)

    def setup_test_content(self, datas, m_test_name, id, m_page):
    #    # VFT heading for scanning page

        # Text Image for info
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 900, 50, 40, 40)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 500, 30, 10, 100)

        # Parameters image
        # self.show_image('Images/wheel.png', 40, 40, 50, 190)
        Image1.image_handler(self.frame, 'Images/wheel.png', 40, 40, 50, 190)
        
        Image1.image_handler(self.frame, 'Images/addtional.png', 300, 300, 650,210)
        # self.show_image('Images/back.png', 180, 42, 950,550, command=lambda:self.on_back_click(datas=datas))
        Image1.image_handler(self.frame, 'Images/back.png', 180, 42, 950,550, command=lambda:self.on_back_click(datas=datas, m_page=m_page))


        self.label1 = tk.Label(self.frame,text=self.topHeading,font=('Helvetica',16,'bold'),fg='#FFF846',bg='#0E0E0E')
        self.label1.place(x=100,y=195) 
        
        if m_page==0:
            if m_test_name == 'headlamp':
                # Dict for parameters details
                headings=[('1. Bulb should be working', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Head lamp operating switch working', ('Helvetica', 12, 'bold'), 'white'),
                ('3.No broken lens', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Lens of the lamp should not be painted with colour', ('Helvetica', 12, 'bold'), 'white'),
                ('5.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white')
                ]
            
            elif m_test_name == 'toplight':
                # Dict for parameters details
                headings=[('1. Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Rear: red, front: white for dual-lens lamps', ('Helvetica', 12, 'bold'), 'white'),
                ('5.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('6. Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'Supressor':
                # Dict for parameters details
                headings=[('1.Suppressor cap shall be in good condition', ('Helvetica', 12, 'bold'), 'white'),
                ('2.High Tension cable shall beproperly insulated', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Proper terminal connections shall be made on both sides of High-Tension cable', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'horn':
                # Dict for parameters details
                headings=[('1.Restrict harsh or alarming noise devices', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Horn shall be securely fitted', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Horn shall be functioning', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Is horn sound compliant with IS:15796', ('Helvetica', 12, 'bold'), 'white')
                ]
            
            elif m_test_name == 'exhaust':
                # Dict for parameters details
                headings=[('1.Ensure no leakage', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Secured fitment of silencer', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Is silencer rust-free and functionally sound', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Stationary noise test as per IS10399:1998', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'wiperblade':
                # Dict for parameters details
                headings=[('1.Ensure presence of wiper blades', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Wiper blade shall be in good condition', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'wipersystem':
                # Dict for parameters details
                headings=[('1.Do wipers cover the entire windshield', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Do each split windshield wipers operate securely', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'dashboard':
                # Dict for parameters details
                headings=[('1.Ensure secured mounting', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Wiring shall be insulated', ('Helvetica', 12, 'bold'), 'white'),
                ('3. Dashboard illumination shall be functioning', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Do warning lights turn off correctly', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'safetyglasses':
                # Dict for parameters details
                headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Does windscreen have required safety markings', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Is glass undamaged, free from films', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'stoplight':
                # Dict for parameters details
                headings=[('1.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working on actuation of the brake', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')]
            
            elif m_test_name == 'parkinglight':
                # Dict for parameters details
                headings=[('1.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ]
            
            elif m_test_name == 'foglight':
                # Dict for parameters details
                headings=[('1. Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ]
            
            elif m_test_name == 'numberplatelight':
                # Dict for parameters details
                headings=[('1.White light shall be used for illuminating number plate', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamps shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ]
            
            elif m_test_name == 'outlinemarkerlight':
                # Dict for parameters details
                headings=[('1.Ensure secured fitment of end-outline marker lamps', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Corrected Orientation:Red lens-rear,White-front', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'directionlight':
                # Dict for parameters details
                headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamps shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens ', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'warninglight':
                # Dict for parameters details
                headings=[('1.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ] 
            
            elif m_test_name == 'hazardlight':
                # Dict for parameters details
                headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Does switch ensure synchronize indicator operation ? ', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            elif m_test_name == 'rearmirror':
                # Dict for parameters details
                headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Does windscreen have required safety markings', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Is glass undamaged, free from films', ('Helvetica', 12, 'bold'), 'white'),
                ] 
            
            elif m_test_name == 'silencer':
                # Dict for parameters details
                headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Does windscreen have required safety markings', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Is glass undamaged, free from films', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            else:
                print("Error: m_test_name hasn't passed...")
            
            y_position = 265
            for text, font_params, fg_color in headings:
                label = tk.Label(self.frame, text=text, font=font_params, fg=fg_color, bg='#0E0E0E', wraplength=500)
                label.place(x=120, y=y_position)

                y_position += 70
            
            api_model.m_test_parameters_handler(frame = self.frame, m_test_name = m_test_name, id = id)
        
        elif m_page==1:
            if m_test_name == 'numberplate':
                # Dict for parameters details
                headings=[('1.White light shall be used for illuminating number plate', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamps shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ]
            elif m_test_name == 'markerlight':
                # Dict for parameters details
                headings=[('1.Ensure secured fitment of end-outline marker lamps', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Corrected Orientation:Red lens-rear,White-front', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'directionlight':
                # Dict for parameters details
                headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamps shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens ', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'warninglight':
                # Dict for parameters details
                headings=[('1.Coloured lens shall not be faded', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Lens should not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Lamp shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Secured fitment of the lamps', ('Helvetica', 12, 'bold'), 'white')
                ] 
        
            elif m_test_name == 'hazardlight':
                # Dict for parameters details
                headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Does switch ensure synchronize indicator operation ? ', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'rearmirror':
                # Dict for parameters details
                headings=[('1.Are mirrors fitted per AIS standards securely ', ('Helvetica', 12, 'bold'), 'white'),
                 ]
            elif m_test_name == 'brakingmanual':
                # Dict for parameters details
                headings=[('1.Fittings shall be secured', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Brake hoses shall not be damaged or cracked', ('Helvetica', 12, 'bold'), 'white'),
                ('3.No leakage of brake fluid', ('Helvetica', 12, 'bold'), 'white'),
                ] 
            elif m_test_name == 'parkingbrakingmanual':
                # Dict for parameters details
                headings=[('1.Fittings shall be secured', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Brake hoses shall not be damaged or cracked', ('Helvetica', 12, 'bold'), 'white'),
                ('3.No leakage of brake fluid', ('Helvetica', 12, 'bold'), 'white'),
                ] 
            elif m_test_name == 'steering':
                # Dict for parameters details
                headings=[('1.Is steering backlash limited to 30 degrees?', ('Helvetica', 12, 'bold'), 'white'),
                
                ]
            elif m_test_name == 'jointplay':
                # Dict for parameters details
                headings=[('1.Are springs and shocks securely attached?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Springs shall not be damaged or fractured', ('Helvetica', 12, 'bold'), 'white'),
                ('3.) Shock absorber dampers shall not have any oil leakage', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Is excessive wear prevented in swivel components?', ('Helvetica', 12, 'bold'), 'white'),
                ('5.In case of Air suspension,ensure no audible system leakage', ('Helvetica', 12, 'bold'), 'white')
                ]
            elif m_test_name == 'speedometermanual':
                # Dict for parameters details
                headings=[('1.Securely fitted', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Sufficiently illuminated', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Dial cover shall not be broken', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Indicator needle operational', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'rupd':
                # Dict for parameters details
                headings=[('1.Rear Underride Protection Device shall be fitted', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Is the rear underride protection undamaged?', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Are rear underride dimensions compliant with IS-14812-2005?', ('Helvetica', 12, 'bold'), 'white'),
                ] 
            elif m_test_name == 'lupd':
                # Dict for parameters details
                headings=[('1. Lateral under run protection device shall be fitted', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Is lateral underrun protection free from damage?', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Are lateral underrun dimensions compliant with IS-14682-2004?', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'fastag':
                # Dict for parameters details
                headings=[('1. To be affixed on the front windscreen', ('Helvetica', 12, 'bold'), 'white'),
                ('2.FASTag shall not be damaged.', ('Helvetica', 12, 'bold'), 'white'),
            ]
            
            else:
                print("Error: m_test_name hasn't passed...")
            
            y_position = 265
            for text, font_params, fg_color in headings:
                label = tk.Label(self.frame, text=text, font=font_params, fg=fg_color, bg='#0E0E0E', wraplength=500)
                label.place(x=120, y=y_position)

                y_position += 70
            
            api_model.m_test_parameters_handler(frame = self.frame, m_test_name = m_test_name, id = id)
        
        elif m_page==2:
            if m_test_name == 'others':
                # Dict for parameters details
                headings=[('1.Are priority seat pictograms visible as required?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.A pictogram shall be placed internally adjacent to the priority seat', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Do Type I buses meet disability seating requirements?', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Are priority seats behind the forward-facing driver?', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Are priority seats equipped for securing mobility aids?', ('Helvetica', 12, 'bold'), 'white'),
                ('6.Is there a handrail at Type I bus entrance?', ('Helvetica', 12, 'bold'), 'white'),
                ('7.Are Type I NDX buses equipped with stop-request controls?', ('Helvetica', 12, 'bold'), 'white'),
                #('8.Are communication devices near priority seats installed?', ('Helvetica', 12, 'bold'), 'white')
                ]
            elif m_test_name == 'wheel':
                # Dict for parameters details
                headings=[('1.Are there visible wheelchair pictograms on the bus?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Is there an internal pictogram indicating wheelchair orientation?', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Is there a wheelchair space with a capable restraint system?', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Is there enough space for a wheelchair user to maneuver independently?', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Does Type I vehicles have designated space for a wheelchair user?', ('Helvetica', 12, 'bold'), 'white'),
                ('6.Are communication devices located in the wheelchair area?', ('Helvetica', 12, 'bold'), 'white'),
            
                ]
            elif m_test_name == 'vlt':
                # Dict for parameters details
                headings=[('1.  Vehicle Location Tracking shall be installed', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Emergency alarm button shall be working', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'hsrp':
                # Dict for parameters details
                headings=[('1.Are high-security registration plates installed front and rear?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Securely fixed', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'battery':
                # Dict for parameters details
                headings=[('1.Secured mounting', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Ensure top is clean, dry, free of dirt and grime', ('Helvetica', 12, 'bold'), 'white'),
                ] 
            elif m_test_name == 'safetybelt':
                # Dict for parameters details
                headings=[('1.Are mandatory safety belts securely fitted and available?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Safety belts shall not be damaged', ('Helvetica', 12, 'bold'), 'white'),
                ('3. Safety belt anchorage shall not be loose', ('Helvetica', 12, 'bold'), 'white'),
                ('4. Is the seatbelt reminder system functioning properly?', ('Helvetica', 12, 'bold'), 'white'),
                ('5.G-lock of seatbelt should be functioning', ('Helvetica', 12, 'bold'), 'white')
                ] 
            elif m_test_name == 'speedgovernor':
                # Dict for parameters details
                headings=[('1.Securely fitted', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Speed governor shall be sealed', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Are speed governor electrical wirings not disconnected?', ('Helvetica', 12, 'bold'), 'white'),
                ]
            elif m_test_name == 'spray':
                # Dict for parameters details
                headings=[('1.Are spray suppression devices securely fitted?', ('Helvetica', 12, 'bold'), 'white'),
                    ]
            elif m_test_name == 'tyres':
                # Dict for parameters details
                headings=[('1.Are tires free from serious damage or unauthorized repairs?', ('Helvetica', 12, 'bold'), 'white'),
                ('2.Is the Non-Skid Depth (NSD) above the specified limit?', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Tyres shall be properly inflated', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Do the tires show any signs of incipient failure?', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Is the tyre casing fabric exposed due to wear or damage?', ('Helvetica', 12, 'bold'), 'white'),
                ('6.Is a temporary spare wheel or puncture repair kit available?', ('Helvetica', 12, 'bold'), 'white')
                ]
            elif m_test_name == 'retro':
                # Dict for parameters details
                headings=[('1.Ensure presence of clean reflective tapes', ('Helvetica', 12, 'bold'), 'white'),
                ('2. Securely pasted to vehicle body', ('Helvetica', 12, 'bold'), 'white'),
                ('3.Are reflective tapes compliant with rule 104 specifications?', ('Helvetica', 12, 'bold'), 'white'),
                ('4.Reflective tapes shall not be damaged', ('Helvetica', 12, 'bold'), 'white'),
                ('5.Are the marks clearly visible and indelible?', ('Helvetica', 12, 'bold'), 'white'),
                ]
            
            else:
                print("Error: m_test_name hasn't passed...")
            
            y_position = 265
            for text, font_params, fg_color in headings:
                label = tk.Label(self.frame, text=text, font=font_params, fg=fg_color, bg='#0E0E0E', wraplength=500)
                label.place(x=120, y=y_position)

                y_position += 70
            
            api_model.m_test_parameters_handler(frame = self.frame, m_test_name = m_test_name, id = id)
        
        

    
    # function to resize the image
    def detail_page_resize_image(self, image_path, width, height):
        try:
            img = Image.open(image_path)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)

            return img_tk
        except Exception as e:
            print(f"Error loading {image_path}: {e}") 
    
    
    def on_back_click(self, datas, m_page):
        self.frame.destroy()
        if m_page==0:
            start_testing(self.root, datas)
        elif m_page==1:
            manual_testing_1(self.root, datas)
        else:
            manual_testing_2(self.root, datas)
        print('BACK')

# Break Test and Axle weight test frame for page(GUI)
class Break_Test:
    def __init__(self, root, id, centre):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Create a frame
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill='both')

        # Load and display the background image        
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        
        # Variable defines for parameters
        self.id = id
        self.centre = centre
        
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content()
        self.start_thread1()
        self.start_thread2()
    
    
    def on_close(self):
        # Stop the thread
        self.stop_thread1()
        self.stop_thread2()
        # Destroy the Tkinter window
        self.root.destroy()
    
    # FUNCTION FOR BUTTONS
    def on_prev10_click(self):
        # self.buttonprev.config(bg='red', fg='white')
        self.buttonnext.config(bg='white', fg='red')
        

    def on_next10_click(self):
        # self.buttonprev.config(bg='white', fg='red')
        self.buttonnext.config(bg='red',  fg='white')
    
    
    def setup_test_content(self):
        # carwtbg
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        bg_img = Image.open('Images/blackbg.png')
        bg_img_tk = ImageTk.PhotoImage(bg_img)
        bg_img_label = tk.Label(self.frame, image=bg_img_tk)
        bg_img_label.image = bg_img_tk
        bg_img_label.pack(expand=True, fill='both')
        
        # Brake heading
        Image1.image_handler(self.frame, 'Images/brake.png', 600, 90, 10, 20)

        # Apply brake heading
        Image1.image_handler(self.frame, 'Images/applybreak.png', 500, 70, 80, 110)

        # SPEEDOMETER IMAGE 1
        MQTT = mqtt_handler.mqtt_object(frame=self.frame, id=self.id)
        
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 20, 468)
        
        # label 1 : left brake
        label1 = tk.Label(self.frame, text='Left Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label1.place(x=95 ,y=530)
        
        # entryfield left brake
        # leftbrake_entryField = tk.Label(self.frame, width=10,text='20', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # leftbrake_entryField.place(x=125, y=480)

        # SPEEDOMETER IMAGE 2
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 230, 50, 400, 380)

        # label 2: left brake
        label2 = tk.Label(self.frame, text='Weight',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label2.place(x=490 ,y=436)
        # entryfield WEIGHT
        # weight_entryfield = tk.Label(self.frame, width=8,text='30', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # weight_entryfield.place(x=480, y=387)
        
        # SPEEDOMETER IMAGE 3
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 690, 468)
        
        # label 3 : left brake
        label3 = tk.Label(self.frame, text='Right Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label3.place(x=770 ,y=530)
        # # entryfield 
        # rightbrake_entryfield = tk.Label(self.frame,text='400', width=10, font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # rightbrake_entryfield.place(x=795, y=480)
        
        # Break Efficiency and test result
        break_efficiency = tk.Label(self.frame, text='Break Efficiency', font=("Times", "20", "bold italic"), fg='white', bg='#0E0E0E')
        break_efficiency.place(x=80, y=600)
        
        break_efficiency = tk.Label(self.frame, text='Test Result', font=("Times", "20", "bold italic"), fg='white', bg='#0E0E0E')
        break_efficiency.place(x=500, y=600)


        # info
        Image1.image_handler(self.frame, 'Images/info.png', 20, 20, 40, 670)

        procedure_label = tk.Label(self.frame, text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure_label.place(x=80 ,y=670)

        procedure1_label = tk.Label(self.frame, text='1.Wait for car to establish connection with sensor',font=('Helvetica',10),bg="#0E0E0E",fg="white")
        procedure1_label.place(x=80 ,y=700)

        procedure2_label = tk.Label(self.frame, text='2.Ask Driver to press accelerato',font=('Helvetica',10),bg="#0E0E0E",fg="white")
        procedure2_label.place(x=80 ,y=720)
        

        # white bg of graph
        Image1.image_handler(self.frame, 'Images/graphbg.png', 500, 500, 1050, 140)
        
        #  BUTTON PREV AND NEXT
        # self.buttonprev = tk.Button(self.frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [self.on_prev10_click(), self.start_thread2()], activeforeground='white',)
        # self.buttonprev.place(x=1000,y=680)

        # self.buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [self.on_next10_click(), self.stop_thread2(), self.stop_thread1(), self.Go_To_Break_Test()],activeforeground='white')
        # self.buttonnext.place(x=1200,y=680)

        # status
        Image1.image_handler(self.frame, 'Images/status.png', 80, 20, 950, 70)

        # timer
        Image1.image_handler(self.frame, 'Images/timer.png', 40, 40, 950, 100)
        
        # timer1_label= tk.Label(self.frame,text='pass', bg="#0E0E0E",fg='yellow',font=(10))
        # timer1_label.place(x=1000, y=125)
        
        # Code to show variable data in graph
        style.use("ggplot")
        self.f = Figure(figsize=(5,5), dpi=77)
        self.a = self.f.add_subplot(111)

        # Adjust the appearance of axis labels
        self.a.tick_params(axis='x', labelsize=15)  # Set x-axis label size
        self.a.tick_params(axis='y', labelsize=15)  # Set y-axis label size

        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=1110, y=195)
    
    
    
    # Function to update graph
    def animate(self):
        file_path1 = resource_path('Graph_Text_Files\\sampleText.txt')
        file_path2 = resource_path('Graph_Text_Files\\sampleText2.txt')
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
        self.a.clear()
        self.a.plot(xList, yList, color='#CC0CA1')
        self.a.plot(xList2, yList2, color='#2BB3E1')
        self.a.tick_params(left = False)
        # Refresh the canvas to show the updated plot
        self.canvas.draw()
    
    # Show the next button after the completion on break force and axle weight test
    def NextButtonShow(self):
        
        api_url = f'{m_base_url}/test/checkdata/{self.id}/{self.centre}'  # Replace with your actual API endpoint
        # payload = {}
         
        
        try:
            response = requests.post(api_url) #,data=payload)
            # print(response.text,"api")
            if response.status_code == 200:
                # print('Searched successfully!') 
                datas = response.json()
                # print(datas)
                # print('############', datas['payload']['testbrake'])
                if datas['payload']['testbrake'] == 'fail' or datas['payload']['testbrake'] == 'pass':
                    try:
                        self.buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',activeforeground='white',command=lambda: [self.on_next10_click(), self.stop_thread2(), self.stop_thread1(), self.Go_To_Break_Test()])
                        self.buttonnext.place(x=1200,y=680)
                    except:
                        pass
                else:
                    pass
                 # Destroy the current frame
                # self.frame.destroy()

        # Create and display the SignInApp frame
                # start_testing(self.root, datas)
            else:
                print(f'Error: Not Found')
                # self.manual_label =tk.Label(self.frame,text="Manual Test is Running...",bg='#E5E5E5',fg='red',font=('Helvetica',14,'bold','italic'))
                # self.manual_label.place(x=300,y=275)
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))
                # self.frame.destroy()
                # start_testing(self.root, datas)

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    
    
    def start_thread1(self):
        self.is_running1 = True  # Set the flag to start the thread
        self.thread1 = Thread(target=self.run_thread1)
        self.thread1.start()

    def stop_thread1(self):
        self.is_running1 = False  # Set the flag to stop the thread

    def run_thread1(self):
        while self.is_running1:
            print("Thread1 is running...")
            self.thread1 = Thread(target=self.animate())
            time.sleep(2)
        
        print("Thread1 is stopped.")
    
    def start_thread2(self):
        self.is_running2 = True  # Set the flag to start the thread
        self.thread2 = Thread(target=self.run_thread2)
        self.thread2.start()

    def stop_thread2(self):
        self.is_running2 = False  # Set the flag to stop the thread

    def run_thread2(self):
        while self.is_running2:
            print("Thread2 is running...")
            self.thread2 = Thread(target=self.NextButtonShow())
            time.sleep(2)
        
        print("Thread2 is stopped.")
        
    
    def Go_To_Break_Test(self):
        self.frame.destroy()
        RPM_Test(self.root, self.id)



# Break Test and Axle weight test frame for page(GUI)
class RPM_Test:
    def __init__(self, root, id):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        # Create a frame
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill='both')
        
        self.id = id

        # Load and display the background image        
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content()
        # self.start_thread()
    
    
    # FUNCTION FOR BUTTONS
    def on_prev10_click(self):
        self.buttonprev.config(bg='red', fg='white')
        self.buttonnext.config(bg='white', fg='red')
        

    def on_next10_click(self):
        self.buttonprev.config(bg='white', fg='red')
        self.buttonnext.config(bg='red',  fg='white')
    
    
    def setup_test_content(self):
        # carwtbg
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        bg_img = Image.open('Images/blackbg.png')
        bg_img_tk = ImageTk.PhotoImage(bg_img)
        bg_img_label = tk.Label(self.frame, image=bg_img_tk)
        bg_img_label.image = bg_img_tk
        bg_img_label.pack(expand=True, fill='both')
        
        # Speed heading
        Image1.image_handler(self.frame, 'Images/speed.png', 900, 90, 10, 20)

        # Accelerate heading
        Image1.image_handler(self.frame, 'Images/accelerate.png', 600, 80, 60, 170)
        
        # Brake heading
        Image1.image_handler(self.frame, 'Images/brake.png', 600, 90, 10, 20)

        # Apply brake heading
        Image1.image_handler(self.frame, 'Images/applybreak.png', 500, 70, 80, 110)

        # SPEEDOMETER IMAGE 1
        MQTT = mqtt_handler.mqtt_RPM_object(frame=self.frame, id=self.id)

        # Status
        Image1.image_handler(self.frame, 'Images/status.png', 100, 20, 160, 280)
        
        # Timer
        Image1.image_handler(self.frame, 'Images/timer.png', 40, 40, 160, 320)
        status_input = tk.Label(self.frame, width=8,text='pass', font=(12), fg='yellow',bg="#0E0E0E",borderwidth=0,relief='flat')
        status_input.place(x=200, y=330)

        # Info
        Image1.image_handler(self.frame, 'Images/info.png', 25, 25, 40, 470)

        procedure_label = tk.Label(self.frame, text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure_label.place(x=80 ,y=473)

        procedure1_label = tk.Label(self.frame, text='1.Wait for car to establish connection with sensor',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure1_label.place(x=80 ,y=500)

        procedure2_label = tk.Label(self.frame, text='2.Ask Driver to press accelerato',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure2_label.place(x=80 ,y=530)

        procedure3_label = tk.Label(self.frame, text='3. .....(your own instructions)',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure3_label.place(x=80 ,y=560)
        
        # Speedometer Image
        # Image1.image_handler(self.frame, 'Images/speedometer.png', 500, 450, 650, 100)

        # ENTRY FIELD IN SPEEDOMETER
        # speedentryField = tk.Label(self.frame, width=20,text='80kmph', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # speedentryField.place(x=810, y=460)
        
        # BUTTON PREV AND NEXT
        buttonprev = tk.Button(self.frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=self.on_prev10_click, activeforeground='white',)
        buttonprev.place(x=850,y=580)

        buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=self.on_next10_click,activeforeground='white')
        buttonnext.place(x=1050,y=580)

# Usage
root = tk.Tk()
app = VFTApp(root)
root.mainloop()
