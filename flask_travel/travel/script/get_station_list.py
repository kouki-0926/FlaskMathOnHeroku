import requests
from pykakasi import kakasi


response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
image_info = response.json()


def get_station_list(image_info, key: str):
    station_list = []
    for marker in image_info[key]["markers"]:
        if "駅名標_" in marker["title"]:
            station_list.append([marker["title"].split("駅名標_")[1], marker["coords"]])
        if "駅舎_" in marker["title"]:
            station_list.append([marker["title"].split("駅舎_")[1], marker["coords"]])
    station_list = sorted(station_list, key=lambda x: x[0])

    formatted = []
    for station in station_list:
        original = station[0].split("_")[0]                       # _新幹線などを除去
        romaji = kanji_to_romaji(original)[:-3].replace("'", "")  # --駅の駅を除去
        formatted.append((original, romaji, station[1]))

    # 同じ駅名を除去
    seen = set()
    unique_formatted = []
    for item in formatted:
        if item[0] not in seen:
            unique_formatted.append(item)
            seen.add(item[0])
    return unique_formatted


_kks = kakasi()
_kks.setMode("H", "a")
_kks.setMode("K", "a")
_kks.setMode("J", "a")
_kks.setMode("r", "Hepburn")
_conv = _kks.getConverter()


def kanji_to_romaji(name: str) -> str:
    r = _conv.do(name)
    r = " ".join(r.split())
    return r.title().replace(" ", "")


fileName = "./flask_ticket/ticket/station_list.py"
with open(fileName, "w", encoding="utf-8") as f:
    f.write("")

for key in image_info.keys():
    station_list = get_station_list(image_info, key)
    max_width = max(len(kanji_to_romaji(station[0])[:-3]) for station in station_list)

    with open(fileName, "a", encoding="utf-8") as f:
        f.write(f"# {key}\n")

        for orig, romaji, coords in station_list:
            lat, lng = coords
            line = "{rom:<{w}} = [{lat:.6f}, {lng:.6f}, \"{ori}\"]".format(rom=romaji, w=max_width, lat=lat, lng=lng, ori=orig)
            f.write(line + "\n")
        f.write("\n")
