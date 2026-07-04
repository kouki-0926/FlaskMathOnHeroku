import requests


def STR(a):
    try:
        b = a.replace("\u3000", "").replace("\n", "")
        b = b.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        return b
    except:
        return a


def get_weather(pref_num):
    url = "https://weather.tsukumijima.net/api/forecast"
    payload = {"city": pref_num}
    data = requests.get(url, params=payload).json()

    data["description"]["headlineText"] = STR(data["description"]["headlineText"])
    data["description"]["bodyText"] = STR(data["description"]["bodyText"])

    for i in range(3):
        data["forecasts"][i]["detail"]["wind"] = STR(data["forecasts"][i]["detail"]["wind"])
        data["forecasts"][i]["detail"]["wave"] = STR(data["forecasts"][i]["detail"]["wave"])
    return data


if(__name__ == "__main__"):
    data = get_weather("130010")
    print(data)
