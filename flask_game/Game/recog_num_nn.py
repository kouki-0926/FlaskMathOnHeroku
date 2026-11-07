import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from PIL import Image
import io


# 学習データの準備
digits = datasets.load_digits()
data_train = digits.data
target_train = digits.target

# NN分類器の作成
clf = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=1000, tol=0.0001, random_state=None)
clf.fit(data_train, target_train)


def recog_num(image_data):
    # 画像読み込み
    image = Image.open(io.BytesIO(image_data)).convert("L")

    # 数字が存在する部分を切り抜く
    inverted_image = Image.eval(image, lambda x: 255 - x)
    croped_image = image.crop(inverted_image.getbbox())

    # 数字を中央に配置
    width, height = croped_image.size
    size = max(width, height)

    square_image = Image.new("L", (size, size), 255)
    square_image.paste(croped_image, ((size - width) // 2, (size - height) // 2))
    resized_image = square_image.resize((8, 8), Image.LANCZOS)

    # 入力データを分類器に合わせて整形
    image_array = np.array(resized_image, dtype=float)
    image_array = 16 - (image_array / 255.0) * 16
    image_array = image_array.astype(int).reshape((1, -1))

    # 予測
    predict = clf.predict(image_array)
    return predict[0]
