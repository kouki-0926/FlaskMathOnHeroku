# -*- coding: utf-8 -*-
import numpy as np
from sklearn.neural_network import MLPClassifier
from flask import flash

# ====1.分類器に入力するデータの準備=============================
# じゃんけんの手のベクトル形式を格納した配列。入力データとして用いる
# グー [1, 0, 0], チョキ [0, 1, 0], パー [0, 0, 1]
janken_array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


# じゃんけんの過去の手の初期化
# 過去何回分の手を覚えるか
n = 3
# 過去の人間の手とコンピュータの手をそれぞれn回分用意
ch_prev = np.zeros(3*n*2)
# 過去の手(ベクトル形式)をランダムに初期化
for i in range(2*n):
    ch_prev[3*i:3*i+3] = janken_array[np.random.randint(0, 3)]
# 過去の手(入力データ)をscikit_learn用の配列に変換
ch_prev_set = np.array([ch_prev])


# 今回の手(0～2の整数)をランダムに初期化
j = np.random.randint(0, 3)
# 今回の手(ターゲット)をscikit_learn用の配列に変換
h_now_set = np.array([j])


# ====2.機械学習の実行=============================
# 三層ニューラルネットワークを定義
clf = MLPClassifier(hidden_layer_sizes=(200,), random_state=None)

# ランダムな入力でオンライン学習を1回行う。
# 初回の学習では、あり得るターゲット(0, 1, 2)を分類器に知らせる必要がある
clf.partial_fit(ch_prev_set, h_now_set, classes=[0, 1, 2])


# ====3.機械学習の結果の表示と評価=============================
# 対戦結果の初期化
result = [0, 0, 0]


def janken_ml(h_choice):
    global ch_prev, ch_prev_set
    h_choice -= 1
    if(h_choice < 0 or h_choice > 2):
        flash("0,1,2を入力してください")

    # コンピュータが、過去の手から人間の今回の手を予測
    h_predict = clf.predict(ch_prev_set)

    # 予測を元にコンピュータが決める
    # 予測がグーならパー、予測がチョキならグー、予測がパーならチョキ
    c_choice = (h_predict[0] + 2) % 3

    # グー, チョキ, パーの名称を格納した配列
    janken_class = ["グー", "チョキ", "パー"]
    # 人間の手とコンピュータの手を画面に表示
    Anser = ["あなた:"+janken_class[h_choice]+", コンピュータ:"+janken_class[c_choice]]

    # 勝敗結果を更新
    if(h_choice == c_choice):
        result[2] += 1
    elif(h_choice == (c_choice+1) % 3):
        result[1] += 1
    else:
        result[0] += 1
    # 勝敗結果を表示
    Anser.append("あなたの勝ち: {}, 負け: {}, あいこ: {}".format(result[0], result[1], result[2]))

    # 過去の手の末尾に今回のコンピュータの手を追加
    ch_prev = np.append(ch_prev[3:], janken_array[c_choice])
    # 過去の手の末尾に今回の人間の手を追加
    ch_prev = np.append(ch_prev[3:], janken_array[h_choice])

    # 過去のじゃんけんの手(ベクトル形式)をscikit_learn形式に
    ch_prev_set = np.array([ch_prev])
    # 今回のじゃんけんの手(0～2の整数)をscikit_learn形式に
    h_now_set = np.array([h_choice])

    # 過去の手(入力データ)と今回の手(ターゲット)とでオンライン学習
    clf.partial_fit(ch_prev_set, h_now_set)

    return Anser
