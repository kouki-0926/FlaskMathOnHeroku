from googletrans import Translator


def translate(en_text):
    translator = Translator()
    return translator.translate(text=en_text, src="en", dest="ja").text


if __name__ == "__main__":
    print(translate("Hello"))
