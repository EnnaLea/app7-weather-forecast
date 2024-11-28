import requests

API_KEY = "f830b94708f367552dcfb1529b39fcf6"

def get_data(place, forcast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    # filtered the data by forcast_days
    nr_values = 8*forcast_days
    filtered_data = filtered_data[:nr_values]

    # filter data by kind
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]

    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3, kind="Temperature"))