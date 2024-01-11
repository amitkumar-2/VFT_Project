import requests
import sys
# sys.path.append("C:/Users/cti-2/OneDrive/Documents/Vehicle-Fitness-Test/bhavna_vft")
from config import settings


#Defined function to return the response data in json format
def return_api_response(api):
    # Request the URL and return the response data
    try:
        response = requests.get(api)
        if response.status_code == 200:
            # print('Searched successfully!') 
            response_datas = response.json()
            # print(response_datas)
            return response_datas
        else:
            print(f'Error: Request is not successfully completed...')
            response_datas = response.json()
            print(response_datas)
            # return response_datas
    except requests.RequestException as e:
        # print(f'Error: {e}')
        except_error = (f'Error: {e}')
        return except_error

def call_api(**kwargs):
    
    #Login statement
    if 'username' in kwargs and 'password'in kwargs and 'centre' in kwargs:
        url = f'{settings.sign_in_url}{kwargs["username"]}/{kwargs["password"]}/{kwargs["centre"]}'
        # print(url)
        
        # Call the function to get response data in json formate
        response_datas = return_api_response(url)
        # print(response_datas)
        return response_datas
        
    
    #Search vehicle appointment
    elif 'vehiclenumber' in kwargs:
        url = f'{settings.check_vehicle_appointment}{kwargs["vehiclenumber"]}'
        # print(url)
        
        # Call the function to get response data in json formate
        response_datas = return_api_response(url)
        # print(response_datas)
        return response_datas
    
    # Fetch data of vehicle details
    elif 'id' in kwargs and 'centre' in kwargs:
        url = f'{settings.fetch_vehicle_details}{kwargs["id"]}/{kwargs["centre"]}'
        # print(url)
        
        # Call the function to get response data in json formate
        response_datas = return_api_response(url)
        # print(response_datas)
        return response_datas
    
    # All manual tests status Overview
    elif 'id' in kwargs and 'centre' in kwargs:
        url = f'{settings.manual_tests_status}{kwargs["id"]}/{kwargs["centre"]}'
        # print(url)
        
        # Call the function to get response data in json formate
        response_datas = return_api_response(url)
        # print(response_datas)
        return response_datas
    
    # Manual test's parameters datas and descriptions
    elif 'testname' in kwargs and 'id' in kwargs:
        url = f'{settings.parameters_data_of_manual_tests}{kwargs["testname"]}/{kwargs["id"]}'
        print("##################", url)
        
        # Call the function to get response data in json formate
        response_datas = return_api_response(url)
        return response_datas

# call_api(username='amzad', password = 'abc123', centre = 'CTI1')
# call_api(vehiclenumber = 'HR NC 12 2918')
# call_api(testname = 'headlamp', id = 'A3')