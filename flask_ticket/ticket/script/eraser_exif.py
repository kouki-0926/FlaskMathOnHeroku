import os
from PIL import Image


def remove_exif_folder(folder_path):
    # フォルダ内のすべてのファイルを取得
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # ファイルの拡張子をチェックして画像ファイルか確認
        _, file_ext = os.path.splitext(file_name)
        if file_ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            # 画像ファイルのパスを作成
            image_path = os.path.join(folder_path, file_name)

            # Exifメタデータを削除
            image = Image.open(image_path)
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(list(image.getdata()))

            # 元のファイルを上書き保存
            image_without_exif.save(image_path)


remove_exif_folder("flask_ticket/static_ticket/images/bousou")
remove_exif_folder("flask_ticket/static_ticket/images/hokaido")
remove_exif_folder("flask_ticket/static_ticket/images/hokuriku")
remove_exif_folder("flask_ticket/static_ticket/images/ise")
remove_exif_folder("flask_ticket/static_ticket/images/kagoshima")
remove_exif_folder("flask_ticket/static_ticket/images/kobe")
remove_exif_folder("flask_ticket/static_ticket/images/nagano")
remove_exif_folder("flask_ticket/static_ticket/images/tohoku")
remove_exif_folder("flask_ticket/static_ticket/images/tokyo")
