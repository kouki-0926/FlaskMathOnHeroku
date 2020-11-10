import requests
from flask import flash

def get_data(x,y):
    Data = []
    url = "http://map.simpleapi.net/stationapi?x="+str(x)+"&y="+str(y)+"&output=json"
    data = requests.get(url).json()

    for i in range(len(data)):
        tmp_data=[]
        tmp_data.append(data[i]["name"])
        tmp_data.append(data[i]["line"])
        tmp_data.append(data[i]["distanceM"])
        tmp_data.append(data[i]["traveltime"])
        Data.append(tmp_data)
    return Data


if __name__ == "__main__":
    Data = get_data("139.7527","35.704")
    for i in range(len(Data)):
        print(Data[i])
