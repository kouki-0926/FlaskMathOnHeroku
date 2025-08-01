from .station_list import *

tokaido = [
    # ================= 乗車券 =================
    ["令和元年9月17日-令和元年9月20日", "総武本線・東海道本線経由乗車券 東千葉->神戸市内(往復(ゆき))"],
    ["令和元年9月21日", "東海道本線・東海道新幹線・総武本線経由乗車券 神戸市内->東千葉(往復(かえり))"],
    ["令和元年9月17日", "鎌倉・江ノ島パス"],
    ["令和元年9月18日", "名古屋市交通局地下鉄全線24時間券"],
    ["令和元年9月19日", "歩くまち・京都レールきっぷ1日版A券"],
    ["令和元年9月19日", "歩くまち・京都レールきっぷ1日版B券"],
    ["令和元年9月20日", "大阪地下鉄・大阪シティバス1日乗車券"],
    ["令和元年9月20日", "神戸ベイエリア回遊1dayパス"],
    # ================= 特急券 =================
    # ================= 入場券 =================
    # ================= 食事 =================
    ["令和元年9月17日", "小田原駅 しらす弁当"],
    ["令和元年9月18日", "豊橋駅 壺屋 稲荷寿司"],
    ["令和元年9月18日", "名古屋駅 松浦のみそカツ 1/2"],
    ["令和元年9月18日", "名古屋駅 松浦のみそカツ 2/2"],
    ["令和元年9月20日", "大阪駅 道頓堀 たこ焼き"]
]

tokaido_images = [
    "令和元年9月17日~令和元年9月21日 東海道本線",
    [
        # =================================================
        ["../trainCar/NoImage.jpg", "開発中"],
    ]
]

tokaido_stations = [
    # ============================ R1/09/17 ============================
    [Chiba, Tokyo, Ofuna, Enoshima, Hase, Kamakura, Ofuna, Odawara, Nebukawa, Atami, Mishima, Numazu, Shimizu],
    # ============================ R1/09/18 ============================
    [Shimizu, Shizuoka, Bentenjima, Toyohashi, Nagoya, Fushimi, Sakae, Nagoya_Castle, Sakae, Kamimaezu, Atsuta_Jingu_Nishi, Kamimaezu, Osu_Kannon, Fushimi, Nagoya],
    # ============================ R1/09/19 ============================
    [Nagoya, Ogaki, Maibara, Hikone, Kyoto, Inari, Fushimi_Inari, Shimizu_Gojyo, Higashiyama, Nijyo_Castle, Tenjingawa, Katabiranotsuji, Arashiyama, Katabiranotsuji, Kitano_Hakubaicho, Katabiranotsuji, Tenjingawa, Shijo_Omiya, Karasuma, Kyoto],
    # ============================ R1/09/20 ============================
    [Kyoto, Shin_Osaka, Osaka, Umeda, Shinsaibashi, Namba, Dobutsuen_Mae, Tennoji, Tanimachi_4_Chome, Temmabashi, Higashi_Umeda, Osaka, Sannomiya, Kobe, Sannomiya, Kyukyoryuchi_Daimarumae, Minato_Motomachi, Harborland, Kobe],
    # ============================ R1/09/21 ============================
    [Kobe, Sannomiya, Osaka, Shin_Osaka, Tokyo, Chiba]
]
