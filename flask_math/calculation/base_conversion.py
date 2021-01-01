from flask import flash


def base_conversion(base, before_conversion):
    try:
        if (base == "binary"):
            bin = before_conversion
            oct = format(int(bin, 2), "o")
            dec = int(bin, 2)
            hex = format(int(bin, 2), "x")
        elif (base == "octal"):
            oct = before_conversion
            bin = format(int(oct, 8), "b")
            dec = int(oct, 8)
            hex = format(int(oct, 8), "x")
        elif (base == "decimal"):
            dec = int(before_conversion)
            bin = format(dec, 'b')
            oct = format(dec, 'o')
            hex = format(dec, 'x')
        elif (base == "hexadecimal"):
            hex = before_conversion
            bin = format(int(hex, 16), "b")
            oct = format(int(hex, 16), "o")
            dec = int(hex, 16)
        anser = [bin, oct, dec, hex]
    except:
        anser = ["Error", "Error", "Error", "Error"]
        flash("エラー：もう一度入力してください")
    return anser
