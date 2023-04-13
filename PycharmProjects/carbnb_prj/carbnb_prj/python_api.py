import requests
import base64

BASE_URL = "http://127.0.0.1:8000/API/"


def signup(username, password):
    res = requests.post (BASE_URL + "signup", json ={"username": username, "password": password})
    # print (res.text)
    return res




def private(username, password):
    encoded_data = base64.b64decode (bytes(f"{username}:{password}", 'ISO-8859-1')).decode("ascii")
    # encoded_data = base64.b64decode (bytes (f"{username}:{password}", 'ISO-8859-1')).decode ("utf-8")
    url = BASE_URL + "private"
    res = requests.get(url, headers = {'Authorization': f'Basic {encoded_data}'})
    print(res.text)
#
# this function gives me the following error:
# UnicodeDecodeError: 'ascii' codec can't decode byte 0x9a in position 0: ordinal not in range(128)

def get_car(car_id: int):
    response = requests.get (f"http://127.0.0.1:8000/API/car?car_id={car_id}")
    return response.json ()


def create_car():
    plate_number = input ("enter plate number")
    type = input ("Enter car type:")
    cost = int (input ("Enter car cost:"))
    year = int (input ("Enter car year:"))

    data = { "plate_number":8888,
            "type": "mitzhubishi",
            "cost": {cost},
            "year": {year},
            }

    response = requests.post (f"http://127.0.0.1:8000/API/car", json = data)
    return response.json ()


#
# def update_car(car_id: int):
#     response = requests.put (f"http://127.0.0.1:8000/API/car?car_id={car_id}")
#     return response.json ()


def get_person(person_id: int):
    response = requests.get (f"http://127.0.0.1:8000/API/person?person_id={person_id}")
    return response.json ()


def get_rent(rent_id: int):
    response = requests.get (f"http://127.0.0.1:8000/API/car?rent_id={rent_id}")
    return response.json ()


x = signup ('bat',1234)
print (x)
