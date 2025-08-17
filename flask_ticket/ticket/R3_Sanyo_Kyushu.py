from .station_list import *

sanyo_kyushu = [
    # ================= 乗車券 =================
    ["令和3年9月11日-令和3年9月15日", "総武本線・東海道山陽新幹線・山陽本線・鹿児島本線経由乗車券 東千葉->八代"],
    ["令和3年9月14日", "鹿児島本線経由乗車券 門司->門司港(往復(ゆき))"],
    ["令和3年9月14日", "鹿児島本線経由乗車券 門司港->門司(往復(かえり))"],
    ["令和3年9月15日", "肥薩おれんじ鉄道 期間限定!1dayのれる切符 八代->川内"],
    ["令和3年9月16日", "鹿児島本線経由乗車券 川内->鹿児島"],
    # ================= 特急券 =================
    ["令和3年9月11日", "東海道山陽新幹線のぞみ13号自由席特急券 東京->新神戸"],
    ["令和3年9月14日", "特急ソニック22号自由席特急券 小倉->博多"],
    ["令和3年9月15日", "特急かもめ101号自由席特急券 博多->鳥栖"],
    # ================= 入場券 =================
    ["令和3年9月13日", "広島電鉄 1日乗車乗船券"],
    ["令和3年9月14日", "福岡市地下鉄 1日乗車券"],
    ["令和3年9月14日", "西鉄 大宰府散策きっぷ"],
    ["令和3年9月15日", "熊本市電1日乗車券"],
    ["令和3年9月16日", "鹿児島市営バス電車フェリー1日共通利用券"],
    # ================= 食事 =================
    ["令和3年9月11日", "岡山駅 桃太郎の祭ずし 1/2"],
    ["令和3年9月11日", "岡山駅 桃太郎の祭ずし 2/2"],
    ["令和3年9月12日", "広島駅 瀬戸のかきめし 1/2"],
    ["令和3年9月12日", "広島駅 瀬戸のかきめし 2/2"],
    ["令和3年9月13日", "宮島口駅 もみじまんじゅう"],
    ["令和3年9月14日", "博多駅 かしわうどん"],
    ["令和3年9月14日", "博多駅 かしわめし 1/2"],
    ["令和3年9月14日", "博多駅 かしわめし 2/2"],
    ["令和3年9月14日", "太宰府駅 梅ヶ枝餅 1/2"],
    ["令和3年9月14日", "太宰府駅 梅ヶ枝餅 2/2"],
    ["令和3年9月15日", "熊本駅 火の国うどん"],
    ["令和3年9月16日", "鹿児島空港 鶏飯"]
]

sanyo_kyushu_images = [
    "令和3年9月11日~令和3年9月16日 山陽九州旅行",
    [
        # =================================================
        ["../trainCar/NoImage.jpg", "開発中"],
    ]
]

sanyo_kyushu_stations = [
    # ============================ R3/09/11 ============================
    [Chiba, Tokyo, Shin_Kobe, Sannomiya, Kobe, Maiko, Akashi, Himeji, Okayama],
    # ============================ R3/09/12 ============================
    [Okayama, Kurashiki, Fukuyama, Onomichi, Itozaki, Hiroshima],
    # ============================ R3/09/13 ============================
    [Hiroshima, Miyajima_Guchi, Iwakuni, Shin_Yamaguchi],
    # ============================ R3/09/14 ============================
    [Shin_Yamaguchi, Shimonoseki, Moji, Mojikou, Moji, Kokura, Hakata, Nakasu_Kawabata, Tenjin, Ohori_Koen, Tenjin, Nishitetsu_Fukuoka, Tofuro_Mae, Nishitetsu_Futsukaichi, Dazaifu, Nishitetsu_Futsukaichi, Tofuro_Mae, Nishitetsu_Fukuoka, Tenjin, Nakasu_Kawabata, Hakata],
    # ============================ R3/09/15 ============================
    [Hakata, Tosu, Kurume, Ginsui, Kumamoto, Kumamoto_Castle, Kumamoto, Yatsushiro, Satsuma_Taki, Satsuma_Sendai],
    # ============================ R3/09/16 ============================
    [Satsuma_Sendai, Kagoshima_Chuo, Kagoshima, Kagoshima_Port, Sakurajima_Port, Kagoshima_Port, Kagoshima_Chuo, Kagoshima_Airport, Haneda_Airport, Shinagawa, Tokyo, Chiba]
]
