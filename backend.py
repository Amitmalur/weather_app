import requests

API_KEY = "a7bb55e7e708ca77f896245e7582ca7e"


def get_data(place, forecast_days=3, kind="Sky"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_days
    filtered_data = filtered_data[:nr_value]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))