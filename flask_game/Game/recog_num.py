import numpy as np
from sklearn import datasets, svm
from sklearn.neural_network import MLPClassifier
from PIL import Image, ImageEnhance
import io


# 学習データの準備
digits = datasets.load_digits()
data_train = digits.data
target_train = digits.target

# NN分類器の作成
clf_nn = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=1000, tol=0.0001, random_state=None)
clf_nn.fit(data_train, target_train)

# SVM分類器の作成
clf_svm = svm.SVC(C=1.0, kernel="linear", decision_function_shape="ovr")
clf_svm.fit(data_train, target_train)


def pre_process_image(image_data):
    # 画像読み込み
    image = Image.open(io.BytesIO(image_data)).convert("L")
    image_width, image_height = image.size

    # 数字が存在する部分を切り抜く
    inverted_image = Image.eval(image, lambda x: 255 - x)
    cropped_image = image.crop(inverted_image.getbbox())
    cropped_width, cropped_height = cropped_image.size

    # 数字を90%に縮小
    scale = 0.9 * np.min([image_width / cropped_width, image_height / cropped_height])
    new_cropped_width  = int(np.round(cropped_width  * scale))
    new_cropped_height = int(np.round(cropped_height * scale))
    cropped_image = cropped_image.resize((new_cropped_width, new_cropped_height), Image.Resampling.LANCZOS)

    # 数字を中央に配置
    center_image = Image.new("L", image.size, 255)
    center_image.paste(cropped_image, ((image_width - new_cropped_width) // 2, (image_height - new_cropped_height) // 2))

    # コントラストを強調
    resized_image = center_image.resize((8, 8), Image.Resampling.LANCZOS)
    resized_image = ImageEnhance.Contrast(resized_image).enhance(2.5)

    # 入力データを分類器に合わせて整形
    image_array = np.asarray(resized_image, dtype=np.float64)
    image_array = 16 - (image_array / 255.0) * 16
    image_array = image_array.reshape((1, -1))

    return resized_image, image_array


def recog_num(image_array):
    predict_nn  =  clf_nn.predict(image_array)
    predict_svm = clf_svm.predict(image_array)
    return [predict_nn[0], predict_svm[0]]
