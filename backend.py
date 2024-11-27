import requests

API_KEY = "f830b94708f367552dcfb1529b39fcf6"

def get_data(place, forcast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))