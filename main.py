
import requests
from twilio.rest import Client

own="https://api.openweathermap.org/data/2.5/onecall"
api_key="d2f064f9c90d6dc94badc629662cc85c"
account_sid="ACf75a20f8834d0e00d3abc2d0a6d429f6"
auth_token="12d2b5a08865196286176af5e91640e1"


weather={
    "lat":14.058324,
    "lon":108.277199,
    "appid":api_key,
    "exclude":"current,minutely,daily",
}
response=requests.get(own,params=weather)
response.raise_for_status()
weather_day=response.json()
weather_slice=weather_day["hourly"][:12]

will_rain=False
for hour_da in weather_slice:
    condition_code=(hour_da["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
            from_="+19895753266",
            to="+84947419402",
            body="It's going to rain today. Remeber to bring an umbrella.",
        )
    print(message.status)
else:
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
            from_="+19895753266",
            to="+84947419402",
            body="It's going to cloud today. Good happiness with everyone.",
        )
    print(message.status)
