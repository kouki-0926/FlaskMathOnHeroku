import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, svm, metrics
from PIL import Image
import io


# 学習データの準備
digits = datasets.load_digits()
data_train = digits.data
target_train = digits.target

# SVM分類器の作成
clf = svm.SVC(C=1.0, kernel="linear", decision_function_shape="ovr")
clf.fit(data_train, target_train)


def recog_num(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("L").resize((8, 8), Image.LANCZOS)

    image_array = np.array(image, dtype=float)
    image_array = 16 - (image_array / 255.0) * 16
    image_array = image_array.astype(int).reshape((1, -1))

    predict = clf.predict(image_array)
    print("解析結果（識別した数字）:", predict[0])
    return predict[0]
