import requests
import os

# parameters = {
#     "lat": 1.436050,
#     "lon": 103.786057,
#     "appid": "cfde991a55b51555eaea8ad03144e917",
#     "exclude": "minutely,daily"
# }
# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# data = response.json()
# loc_weather = data["current"]["weather"]
# print(loc_weather)
# cfde991a55b51555eaea8ad03144e917
# check if it will rain in next 12 hours
auth_token = os.environ.get("AUTH_TOKEN")
rain_parameters = {
    "lat": 1.436050,
    "lon": 103.786057,
    "appid": auth_token,
    "exclude": "current,minutely,daily"
}
rain_response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=rain_parameters)
rain_response.raise_for_status()
rain_data = rain_response.json()
hourly_data = rain_data["hourly"]

for i in range(12):
    if hourly_data[i]["weather"][0]["id"]:
        rain = True
        break

if rain:
    print("bring umbrella")
else:
    print("its gonna be hot")
