from googletrans import Translator


def translate(ja_text):
    translator = Translator()
    return translator.translate(text=ja_text, src="en", dest="ja").text


if __name__ == "__main__":
    print(translate("Hello"))
