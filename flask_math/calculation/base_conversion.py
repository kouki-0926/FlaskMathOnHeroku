from flask import flash
from sympy.logic.boolalg import simplify_logic


def base_conversion(before_conversion):
    try:
        base = str(before_conversion)[0:2]
        before_conversion = str(before_conversion)[2:]

        if (base == "0b"):
            bin = before_conversion
            oct = format(int(bin, 2), "o")
            dec = int(bin, 2)
            hex = format(int(bin, 2), "x")
        elif (base == "0o"):
            oct = before_conversion
            bin = format(int(oct, 8), "b")
            dec = int(oct, 8)
            hex = format(int(oct, 8), "x")
        elif (base == "0d"):
            dec = int(before_conversion)
            bin = format(dec, 'b')
            oct = format(dec, 'o')
            hex = format(dec, 'x')
        elif (base == "0x"):
            hex = before_conversion
            bin = format(int(hex, 16), "b")
            oct = format(int(hex, 16), "o")
            dec = int(hex, 16)
        anser = ["2進法:"+str(bin), "8進法:"+str(oct),
                 "10進法:"+str(dec), "16進法:"+str(hex)]
    except:
        anser = ["Error", "Error", "Error", "Error"]
        flash("エラー：もう一度入力してください")
    return anser
