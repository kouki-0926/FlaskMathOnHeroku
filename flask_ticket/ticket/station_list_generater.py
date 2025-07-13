import csv
import pykakasi


def kanji_to_romaji(station_name: str) -> str:
    kakasi = pykakasi.kakasi()
    result = kakasi.convert(station_name)

    return result[0]["passport"].capitalize()


def get_station_coordinates(station_name: str):
    with open("station.csv", "r", encoding="utf-8") as iuput_file:
        reader = csv.reader(iuput_file)
        l = [row for row in reader]

    for row in l:
        if station_name in row[2]:
            print(f'{kanji_to_romaji(station_name)} = [{row[10]}, {row[9]}, "{station_name}駅"]\n')
            return
    print(f"Station {station_name} not found in CSV data.")


if __name__ == "__main__":
    get_station_coordinates("東京")
