import requests
from flask import flash


def get_location(ip_address):
    try:
        url = "https://ipapi.co/"+str(ip_address)+"/json/"
        Data = requests.get(url).json()

        latitude = Data["latitude"]
        try:
            if(float(latitude) >= 0):
                Data["latitude_2"] = "北緯{}".format(abs(float(latitude)))
            elif(float(latitude) < 0):
                Data["latitude_2"] = "南緯{}".format(abs(float(latitude)))
        except:
            Data["latitude_2"] = Data["latitude"]

        longitude = Data["longitude"]
        try:
            if(float(longitude) >= 0):
                Data["longitude_2"] = "東経{}".format(abs(float(longitude)))
            elif(float(longitude) < 0):
                Data["longitude_2"] = "西経{}".format(abs(float(longitude)))
        except:
            Data["longitude_2"] = Data["longitude"]
    except:
        flash("IPアドレスの情報取得失敗")
        Data["message"] = "https://ipapi.co/ratelimited/"
    return Data


if __name__ == "__main__":
    Data = get_location("8.8.8.8")
    print(Data)
    for data in Data.values():
        print(data)
