from PIL import Image


def eraser_exif(file):
    with Image.open(file) as src:
        data = src.getdata()
        mode = src.mode
        size = src.size

        with Image.new(mode, size) as dst:
            dst.putdata(data)
            dst.save(file)


if __name__ == "__main__":
    for i in range(8):
        try:
            eraser_exif("flask_ticket\static_ticket\images\img"+str(i)+".jpg")
        except:
            print("削除失敗")
