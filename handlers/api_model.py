import sys
# sys.path.append("C:/Users/cti-2/OneDrive/Documents/Vehicle-Fitness-Test/bhavna_vft/handlers")
# from Find_Directory_Path import resource_path

import os
# current_dir = os.path.dirname(os.path.realpath(__file__))
# print(current_dir)


import requests
from io import BytesIO
from tkinter import Label
from PIL import Image
from handlers.Image1 import image_handler
from handlers.API_Handler import call_api

# result = call_api(vehiclenumber = 'HR NC 12 2918')
# print(result)

def get_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def m_test_parameters_handler(**kwargs):
    if 'm_test_name' in kwargs:
        response_datas = call_api(testname = kwargs['m_test_name'], id = kwargs['id'])
        
        #Image code for perticular manual test
        try:
            if response_datas['payload']['img'] != 'none':
                img_url = response_datas['payload']['img']
                img = get_image_from_url(img_url)
                image_handler(kwargs['frame'],'Images/blnkbox.png', 300, 300, 980, 210,direct_img=img)
            else:
                label_m_test_Img = Label(kwargs['frame'], text='Image not provided', fg='red', bg='#0E0E0E', font=('',18))
                label_m_test_Img.place(x=980, y=210)
        except:
            label_m_test_Img = Label(kwargs['frame'], text='Image not provided', fg='red', bg='#0E0E0E', font=('',18))
            label_m_test_Img.place(x=980, y=210)
        
        #createing Label to show additional details for manual tests
        try:
            if response_datas['payload']['remark'] != None:
                label_additional_details = Label(kwargs['frame'],text=f"{response_datas['payload']['remark']}", wraplength=280, font=('',14))
                label_additional_details.place(x=660, y=260)
            else:
                label_additional_details = Label(kwargs['frame'],text="You haven't mention the remarks")
                label_additional_details.place(x=660, y=260)
        except:
            label_additional_details = Label(kwargs['frame'],text="You haven't mention the remarks")
            label_additional_details.place(x=660, y=260)
        
        # For Parameter 1
        try:
            if response_datas['payload']['p1'] == '1':
                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 260, image_path_02='Images/right.png')
            elif response_datas['payload']['p1'] == '2':
                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 260, image_path_02='Images/cross.png')
            else:
                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 260)
                na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=266)
        except:
            image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 260)
            na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=266)
        
        # For Parameter 2
        if kwargs['m_test_name'] != 'rearmirror' and kwargs['m_test_name'] != 'spray' and kwargs['m_test_name'] != 'steering':
            print('############', kwargs['m_test_name'] != 'rearmirror')
            try:
                if response_datas['payload']['p2'] == '1':
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 330, image_path_02='Images/right.png')
                elif response_datas['payload']['p2'] == '2':
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 330, image_path_02='Images/cross.png')
                else:
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 330)
                    na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=336)
            except:
                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 330)
                na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=336)
        
        try:
            if kwargs['m_test_name'] == 'headlamp' or kwargs['m_test_name'] == 'exhaust' or kwargs['m_test_name'] == 'dashboard' or kwargs['m_test_name'] == 'horn' or kwargs['m_test_name'] == 'safetyglasses' or kwargs['m_test_name'] == 'Supressor' or kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'stoplight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'warninglight' or kwargs['m_test_name'] == 'numberplate'or kwargs['m_test_name'] == 'markerlight'or kwargs['m_test_name'] == 'directionlight'or kwargs['m_test_name'] == 'warninglight'or kwargs['m_test_name'] == 'numberplate'or  kwargs['m_test_name'] == 'brakingmanual'or kwargs['m_test_name'] == 'parkingbrakingmanual'or kwargs['m_test_name'] == 'rupd'or kwargs['m_test_name'] == 'lupd'or kwargs['m_test_name'] == 'speedgoverner'or kwargs['m_test_name'] == 'jointplay'or kwargs['m_test_name'] == 'speedometermanual'or kwargs['m_test_name'] == 'safetybelt'or kwargs['m_test_name'] == 'retro' or kwargs['m_test_name'] == 'tyres' or kwargs['m_test_name'] == 'wheel' or kwargs['m_test_name'] == 'others':
                # For Parameter 3
                try:
                    if response_datas['payload']['p3'] == '1':
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 400, image_path_02='Images/right.png')
                    elif response_datas['payload']['p3'] == '2':
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 400, image_path_02='Images/cross.png')
                    else:
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 400)
                        na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=406)
                except:
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 400)
                    na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=406)
                
                try:
                    if kwargs['m_test_name'] == 'headlamp'or kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'dashboard' or kwargs['m_test_name'] == 'exhaust' or kwargs['m_test_name'] == 'horn' or kwargs['m_test_name'] == 'stoplight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'warninglight'or kwargs['m_test_name'] == 'numberplate'or kwargs['m_test_name'] == 'markerlight'or kwargs['m_test_name'] == 'directionlight'or kwargs['m_test_name'] == 'warninglight'or kwargs['m_test_name'] == 'numberplate'or kwargs['m_test_name'] == 'jointplay'or kwargs['m_test_name'] == 'speedometermanual'or kwargs['m_test_name'] == 'safetybelt'or kwargs['m_test_name'] == 'retro' or kwargs['m_test_name'] == 'tyres' or kwargs['m_test_name'] == 'wheel' or kwargs['m_test_name'] == 'others':
                        #For Parameter 4
                        try:
                            if response_datas['payload']['p4'] == '1':
                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 470, image_path_02='Images/right.png')
                            elif response_datas['payload']['p4'] == '2':
                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 470, image_path_02='Images/cross.png')
                            else:
                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 470)
                                na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=476)
                        except:
                            image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 470)
                            na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=476)
                        
                        try:
                            if kwargs['m_test_name'] == 'headlamp' or kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'stoplight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'warninglight'or kwargs['m_test_name'] == 'numberplate'or kwargs['m_test_name'] == 'markerlight'or kwargs['m_test_name'] == 'directionlight'or kwargs['m_test_name'] == 'warninglight'or kwargs['m_test_name'] == 'numberplate'or kwargs['m_test_name'] == 'jointplay'or kwargs['m_test_name'] == 'safetybelt'or kwargs['m_test_name'] == 'retro' or kwargs['m_test_name'] == 'tyres' or kwargs['m_test_name'] == 'wheel' or kwargs['m_test_name'] == 'others':
                                #For Parameter 5
                                try:
                                    if response_datas['payload']['p5'] == '1':
                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 540, image_path_02='Images/right.png')
                                    elif response_datas['payload']['p5'] == '2':
                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 540, image_path_02='Images/cross.png')
                                    else:
                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 540)
                                        na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=546)
                                except:
                                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 540)
                                    na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=546)
                                
                                try:
                                    if kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'tyres' or kwargs['m_test_name'] == 'wheel' or kwargs['m_test_name'] == 'others':
                                        #For Parameter 6
                                        try:
                                            if response_datas['payload']['p6'] == '1':
                                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 610, image_path_02='Images/right.png')
                                            elif response_datas['payload']['p6'] == '2':
                                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 610, image_path_02='Images/cross.png')
                                            else:
                                                image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 610)
                                                na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=616)
                                        except:
                                            image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 610)
                                            na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=616)
                                        try:
                                            if kwargs['m_test_name'] == 'others':
                                                #For Parameter 7
                                                try:
                                                    if response_datas['payload']['p7'] == '1':
                                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 680, image_path_02='Images/right.png')
                                                    elif response_datas['payload']['p7'] == '2':
                                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 680, image_path_02='Images/cross.png')
                                                    else:
                                                        image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 680)
                                                        na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=686)
                                                except:
                                                    image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 680)
                                                    na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=686)
                                                
                                                # try:
                                                #     if kwargs['m_test_name'] == 'others':
                                                #         #For Parameter 8
                                                #         try:
                                                #             if response_datas['payload']['p8'] == '1':
                                                #                 image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 700, image_path_02='Images/right.png')
                                                #             elif response_datas['payload']['p8'] == '2':
                                                #                 image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 700, image_path_02='Images/cross.png')
                                                #             else:
                                                #                 image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 700)
                                                #                 na_label = Label(kwargs['frame'], text='NA', font=('', 11, 'bold'), fg='black').place(x=64, y=756)
                                                #         except:
                                                #             image_handler(kwargs['frame'],'Images/blnkbox.png', 30, 30, 60, 700)
                                                #             na_label = Label(kwargs['frame'], text='', font=('', 11, 'bold'), fg='black').place(x=64, y=756)
                                                # except:
                                                #     pass
                                        except:
                                            pass
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass

# m_test_parameters_handler(m_test_name = 'headlamp', id = 'A3')