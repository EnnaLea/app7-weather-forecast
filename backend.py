import requests

API_KEY = "f830b94708f367552dcfb1529b39fcf6"

def get_data(place=None, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    # filtered the data by forcast_days
    nr_values = 8*forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data()