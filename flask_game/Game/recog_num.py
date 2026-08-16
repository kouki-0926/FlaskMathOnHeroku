import numpy as np
from sklearn import datasets, svm, metrics
from PIL import Image
import io


# 学習データの準備
digits = datasets.load_digits()
data_train = digits.images.reshape((digits.images.shape[0], -1))
label_train = digits.target

# トレーニングデータで機械学習SVM
clf = svm.SVC(gamma=0.001, C=10.0)
clf.fit(data_train, label_train)


def recog_num(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("L").resize((8, 8), Image.LANCZOS)

    image_array = np.array(image, dtype=float)
    image_array = 16 - np.floor(17 * image_array / 256)
    image_array = image_array.reshape((1, -1))

    predict = clf.predict(image_array)
    print("解析結果（識別した数字）:", predict[0])
