import requests


def STR(a):
    a = a.replace("\u3000", "").replace("\n", "")
    a = a.translate(str.maketrans(
        {chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    return a


def get_weather(pref_num):
    url = "https://weather.tsukumijima.net/api/forecast"
    payload = {"city": pref_num}
    data = requests.get(url, params=payload).json()

    data["description"]["headlineText"] = STR(data["description"]["headlineText"])
    data["description"]["bodyText"] = STR(data["description"]["bodyText"])

    forecasts = data["forecasts"]

    for i in range(3):
        forecasts[i]["detail"]["wind"] = STR(forecasts[i]["detail"]["wind"])
        forecasts[i]["detail"]["wave"] = STR(forecasts[i]["detail"]["wave"])

    return [data, forecasts]


if(__name__ == "__main__"):
    data = get_weather("130010")
    print(data[1][0]["detail"]["wave"])
