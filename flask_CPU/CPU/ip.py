import requests

def get_location():
    try:
        Data = []
        url = "https://ipapi.co/json/"
        data = requests.get(url).json()

        #0
        Data.append("{}".format(data["ip"]))
        #1~5
        Data.append("{}".format(data["version"]))
        Data.append("{}".format(data["city"]))
        Data.append("{}".format(data["region"]))
        Data.append("region_code: {}".format(data["region_code"]))
        Data.append("{}".format(data["country"]))
        #6~10
        Data.append("country_name: {}".format(data["country_name"]))
        Data.append("country_code: {}".format(data["country_code"]))
        Data.append("country_code_iso3: {}".format(data["country_code_iso3"]))
        Data.append("country_capital: {}".format(data["country_capital"]))
        Data.append("country_tld: {}".format(data["country_code"]))
        #11~15
        Data.append("continent_code: {}".format(data["continent_code"]))
        Data.append("in_EU: {}".format(data["in_eu"]))
        Data.append("{}".format(data["latitude"]))
        Data.append("{}".format(data["longitude"]))
        Data.append("timezone: {}".format(data["timezone"]))
        #16~20
        Data.append("utc_offset: {}".format(data["utc_offset"]))
        Data.append("country_calling_code: {}".format(data["country_calling_code"]))
        Data.append("currency_name: {}".format(data["currency_name"]))
        Data.append("languages: {}".format(data["languages"]))
        Data.append("country_population: {}".format(data["country_population"]))
        #21~22
        Data.append("asn: {}".format(data["asn"]))
        Data.append("org: {}".format(data["org"]))
    except:
        Data = []
        Data.append("error: {}".format(data["error"]))
        Data.append("reason: {}".format(data["reason"]))
        Data.append("{}".format(data["message"]))
    return Data


if __name__ == "__main__":
    Data = get_location()
    for i in range(len(Data)):
        print(Data[i])
