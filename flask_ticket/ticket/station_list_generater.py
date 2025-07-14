import csv
import sys
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
            print(f'{kanji_to_romaji(row[2])} = [{row[10]}, {row[9]}, "{row[2]}駅"] {row[8]}')


if __name__ == "__main__":
    get_station_coordinates(sys.argv[1])
