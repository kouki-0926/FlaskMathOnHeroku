import requests
from flask import flash


def get_data(x, y):
    url = "http://express.heartrails.com/api/json?method=getStations&x="+str(x)+"&y="+str(y)
    data = requests.get(url).json()
    data = data["response"]["station"]

    Data = []
    for i in range(len(data)):
        tmp_data = []
        tmp_data.append(data[i]["name"])
        tmp_data.append(data[i]["prefecture"])
        tmp_data.append(data[i]["line"])
        tmp_data.append(data[i]["x"])
        tmp_data.append(data[i]["y"])
        tmp_data.append(data[i]["postal"])
        tmp_data.append(data[i]["distance"])
        tmp_data.append(data[i]["prev"])
        tmp_data.append(data[i]["next"])
        Data.append(tmp_data)
    return Data


if __name__ == "__main__":
    Data = get_data("139.7527", "35.704")
    print(Data)
    # for i in range(len(Data)):
    #     print(Data[i])
