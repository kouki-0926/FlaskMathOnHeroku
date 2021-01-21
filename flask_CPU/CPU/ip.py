import requests
from flask import flash


def get_location(ip_address):
    try:
        Data = {}
        url = "https://ipapi.co/"+str(ip_address)+"/json/"
        data = requests.get(url).json()
        # 0
        Data["ip"] = "{}".format(data["ip"])
        # 1-5
        Data["version"] = "{}".format(data["version"])
        Data["city"] = "{}".format(data["city"])
        Data["region"] = "{}".format(data["region"])
        Data["region_code"] = "{}".format(data["region_code"])
        Data["country"] = "{}".format(data["country"])
        # 6-10
        Data["country_name"] = "{}".format(data["country_name"])
        Data["country_code"] = "{}".format(data["country_code"])
        Data["country_code_iso3"] = "{}".format(data["country_code_iso3"])
        Data["country_capital"] = "{}".format(data["country_capital"])
        Data["country_tld"] = "{}".format(data["country_code"])
        # 11-15
        Data["continent_code"] = "{}".format(data["continent_code"])
        Data["in_EU"] = "{}".format(data["in_eu"])

        latitude = data["latitude"]
        Data["latitude"] = "{}".format(data["latitude"])
        if(latitude == "Sign up to access"):
            Data["latitude_2"] = "{}".format(data["latitude"])
        elif(float(latitude) >= 0):
            Data["latitude_2"] = "北緯{}".format(abs(float(latitude)))
        elif(float(latitude) < 0):
            Data["latitude_2"] = "南緯{}".format(abs(float(latitude)))

        longitude = data["longitude"]
        Data["longitude"] = "{}".format(data["longitude"])
        if(longitude == "Sign up to access"):
            Data["longitude_2"] = "{}".format(data["longitude"])
        elif(float(longitude) >= 0):
            Data["longitude_2"] = "東経{}".format(abs(float(longitude)))
        elif(float(longitude) < 0):
            Data["longitude_2"] = "西経{}".format(abs(float(longitude)))

        Data["timezone"] = "{}".format(data["timezone"])
        # 16~20
        Data["utc_offset"] = "{}".format(data["utc_offset"])
        Data["country_calling_code"] = "{}".format(data["country_calling_code"])
        Data["currency_name"] = "{}".format(data["currency_name"])
        Data["languages"] = "{}".format(data["languages"])
        Data["country_population"] = "{}".format(data["country_population"])
        # 21~22
        Data["asn"] = "{}".format(data["asn"])
        Data["org"] = "{}".format(data["org"])

    except:
        Data = []
        Data.append("ERROR")
        flash("IPアドレスの情報取得失敗")
        # Data.append("error: {}".format(data["error"]))
        Data.append("reason: {}".format(data["reason"]))
        Data.append("{}".format(data["message"]))
    return Data


if __name__ == "__main__":
    Data = get_location("8.8.8.8")
    for data in Data.values():
        print(data)
