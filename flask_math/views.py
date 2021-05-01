from flask import request, redirect, url_for, render_template, flash, Blueprint, make_response
from flask_math.calculation import *

Math = Blueprint("Math", __name__, template_folder="templates_math", static_folder="static_math")


@Math.route("/test")
def test_view():
    return render_template("test.html")


@Math.route("/index")
def index_view():
    return render_template("index.html")


@Math.route("/index_2")
def index_2_view():
    return render_template("index_2.html")


@Math.route("/index_3")
def index_3_view():
    return render_template("index_3.html")


@Math.route("/instructions")
def instructions_view():
    return render_template("instructions.html")


@Math.route("/Apart", methods=["GET", "POST"])
def Apart_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        anser = Apart.Apart(formula)
        return render_template("Apart.html", formula=formula, anser=anser, init_flag=0)
    else:
        return render_template("Apart.html", init_flag=1)


@Math.route("/base_conversion", methods=["GET", "POST"])
def base_conversion_view():
    if request.method == "POST":
        try:
            if request.form.get("bin") != "":
                base = "binary"
                before_conversion = request.form.get("bin")
            elif request.form.get("oct") != "":
                base = "octal"
                before_conversion = request.form.get("oct")
            elif request.form.get("dec") != "":
                base = "decimal"
                before_conversion = request.form.get("dec")
            elif request.form.get("hex") != "":
                base = "hexadecimal"
                before_conversion = request.form.get("hex")
            anser = base_conversion.base_conversion(base, before_conversion)
        except:
            anser = ["Error", "Error", "Error", "Error"]
            flash("エラー：もう一度入力してください")
        return render_template("base_conversion.html", bin=anser[0], oct=anser[1], dec=anser[2], hex=anser[3])
    else:
        return render_template("base_conversion.html")


@Math.route("/BMI", methods=["GET", "POST"])
def BMI_view():
    if request.method == "POST":
        height = request.form.get("height")
        weight = request.form.get("weight")
        Anser = BMI.BMI(height, weight)
        return render_template("BMI.html", height=height, weight=weight, Anser=Anser, init_flag=0)
    else:
        return render_template("BMI.html", init_flag=1)


@Math.route("/bode", methods=["GET", "POST"])
def bode_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        try:
            lower_end = int(request.form.get("lower_end"))
            upper_end = int(request.form.get("upper_end"))
            if(lower_end >= upper_end):
                tmp = upper_end
                upper_end = lower_end
                lower_end = tmp
        except:
            lower_end = -3
            upper_end = 3
        return render_template("bode.html", formula=formula, lower_end=lower_end, upper_end=upper_end, init_flag=0)
    else:
        return render_template("bode.html", lower_end=-3, upper_end=3, init_flag=1)


@Math.route('/bode.png')
def bode_png():
    formula = request.args.get("formula")
    try:
        lower_end = int(request.args.get("lower_end"))
        upper_end = int(request.args.get("upper_end"))
    except:
        lower_end = -3
        upper_end = 3
    response = bode.bode(formula, lower_end, upper_end)
    return response


@Math.route("/derivative", methods=["GET", "POST"])
def derivative_view():
    if (request.method == "POST"):
        formula = request.form.get("formula")
        type = request.form.get("type")
        Anser = derivative.derivative(formula, type)
        return render_template("derivative.html", formula=formula, type=type, Anser=Anser, init_flag=0)
    else:
        return render_template("derivative.html", type="x", init_flag=1)


@Math.route("/diff_equation", methods=["GET", "POST"])
def diff_equation_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        Anser = diff_equation.diff_equation(formula)
        return render_template("diff_equation.html", formula=formula, Anser=Anser, init_flag=0)
    else:
        return render_template("diff_equation.html", init_flag=1)


@Math.route("/equation", methods=["GET", "POST"])
def equation_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        type = request.form.get("type")
        Anser = equation.equation(formula, type)
        return render_template("equation.html", formula=formula, Anser=Anser, type=type, init_flag=0)
    else:
        type = request.args.get("type")
        if(type is None):
            return redirect(url_for("Math.equation_view", type="analytical"))
        return render_template("equation.html", type=type, init_flag=1)


@Math.route("/equations", methods=["GET", "POST"])
def equations_view():
    try:
        if request.method == "POST":
            number = int(request.form.get("number"))
            if number == 1:
                formula_1 = request.form.get("formula_1")
                Formula = [formula_1]
                Anser = equations.equations(Formula, number)
                return render_template("equations.html", formula_1=formula_1, Anser=Anser, number=number, init_flag=0)
            elif number == 2:
                formula_1 = request.form.get("formula_1")
                formula_2 = request.form.get("formula_2")
                Formula = [formula_1, formula_2]
                Anser = equations.equations(Formula, number)
                return render_template("equations.html", formula_1=formula_1, formula_2=formula_2, Anser=Anser, number=number, init_flag=0)
            elif number == 3:
                formula_1 = request.form.get("formula_1")
                formula_2 = request.form.get("formula_2")
                formula_3 = request.form.get("formula_3")
                Formula = [formula_1, formula_2, formula_3]
                Anser = equations.equations(Formula, number)
                return render_template("equations.html", formula_1=formula_1, formula_2=formula_2, formula_3=formula_3, Anser=Anser, number=number, init_flag=0)
            else:
                return render_template("equations.html", number=1, init_flag=1)
        else:
            number = int(request.args.get("number"))
            if number >= 1 and number <= 3:
                return render_template("equations.html", number=number, init_flag=1)
            else:
                return redirect(url_for("Math.equations_view", number=1), init_flag=1)
    except:
        flash("エラー：もう一度入力してください")
        return render_template("equations.html", number=1, init_flag=1)


@Math.route("/Euclidean_Algorithm", methods=["GET", "POST"])
def Euclidean_Algorithm_view():
    if request.method == "POST":
        number_x = request.form.get("number_x")
        number_y = request.form.get("number_y")
        anser = Euclidean_Algorithm.Euclidean_Algorithm(number_x, number_y)
        return render_template("Euclidean_Algorithm.html", number_x=number_x, number_y=number_y, anser=anser, init_flag=0)
    else:
        return render_template("Euclidean_Algorithm.html", init_flag=1)


@Math.route("/Expand", methods=["GET", "POST"])
def Expand_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        anser = Expand.Expand(formula)
        return render_template("Expand.html", formula=formula, anser=anser, init_flag=0)
    else:
        return render_template("Expand.html", init_flag=1)


@Math.route("/Factorial", methods=["GET", "POST"])
def Factorial_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        anser = Factorial.Factorial(formula)
        return render_template("Factorial.html", formula=formula, anser=anser, init_flag=0)
    else:
        return render_template("Factorial.html", init_flag=1)


@Math.route("/factorization", methods=["GET", "POST"])
def factorization_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        anser = factorization.factorization(formula)
        return render_template("factorization.html", formula=formula, anser=anser, init_flag=0)
    else:
        return render_template("factorization.html", init_flag=1)


@Math.route("/graph", methods=["GET", "POST"])
def graph_view():
    if request.method == "POST":
        formula_1 = request.form.get("formula_1")
        try:
            lower_end_x = float(request.form.get("lower_end_x"))
            upper_end_x = float(request.form.get("upper_end_x"))
            if(lower_end_x >= upper_end_x):
                tmp = upper_end_x
                upper_end_x = lower_end_x
                lower_end_x = tmp
        except:
            lower_end_x = -10
            upper_end_x = 10
        return render_template("graph.html", formula_1=formula_1, lower_end_x=lower_end_x, upper_end_x=upper_end_x, init_flag=0)
    else:
        return render_template("graph.html", lower_end_x=-10, upper_end_x=10, init_flag=1)


@Math.route('/graph.png')
def graph_png():
    formula_1 = request.args.get("formula_1")
    lower_end_x = request.args.get("lower_end_x")
    upper_end_x = request.args.get("upper_end_x")
    response = graph.graph(formula_1, lower_end_x, upper_end_x)
    return response


@Math.route("/integral", methods=["GET", "POST"])
def integral_view():
    dimension = request.args.get("dimension")
    if(request.method == "POST"):
        formula = request.form.get("formula")
        Upper_end = [request.form.get("upper_end_x")]
        Lower_end = [request.form.get("lower_end_x")]
        type = request.form.get("type")
        if(dimension == "2D"):
            anser = integral.integral(formula, Upper_end, Lower_end, type)
            return render_template("integral.html", formula=formula, upper_end_x=Upper_end[0], lower_end_x=Lower_end[0], dimension=dimension, type=type, anser=anser, init_flag=0)
        elif(dimension == "3D"):
            Upper_end.append(request.form.get("upper_end_y"))
            Lower_end.append(request.form.get("lower_end_y"))
            anser = integral.integral(formula, Upper_end, Lower_end, type)
            return render_template("integral.html", formula=formula, upper_end_x=Upper_end[0], lower_end_x=Lower_end[0], upper_end_y=Upper_end[1], lower_end_y=Lower_end[1], dimension=dimension, type=type, anser=anser, init_flag=0)
        else:
            flash("エラー:dimension")
            return redirect(url_for("Math.integral_view", dimension="2D"))
    elif(request.method == "GET"):
        if(dimension == "2D"):
            return render_template("integral.html", dimension=dimension, type="indefinite_integral", init_flag=1)
        elif(dimension == "3D"):
            return render_template("integral.html", dimension=dimension, type="multiple_integral_1", init_flag=1)
        else:
            flash("エラー:dimension")
            return redirect(url_for("Math.integral_view", dimension="2D"))


@Math.route("/laplace", methods=["GET", "POST"])
def laplace_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        type = request.args.get("type")
        anser = laplace.laplace(formula, type=type)
        return render_template("laplace.html", formula=formula, type=type, anser=anser, init_flag=0)
    else:
        type = request.args.get("type")
        if(type == "lap" or type == "inv"):
            return render_template("laplace.html", type=type, init_flag=1)
        else:
            return redirect(url_for('Math.laplace_view', type='lap'))


@Math.route("/latex", methods=["GET", "POST"])
def latex_view():
    if(request.method == "POST"):
        input_type = request.form.get("input_type")
        if(input_type == "python"):
            formula_python = request.form.get("formula_python")
            anser = latex.latex(formula_python)
            return render_template("latex.html", formula_python=formula_python, anser=anser, input_type=input_type, init_flag=0)
        elif(input_type == "latex"):
            formula_latex = request.form.get("formula_latex")
            return render_template("latex.html", formula_latex=formula_latex, anser=formula_latex, input_type=input_type, init_flag=0)
        else:
            return redirect(url_for("Math.latex_view", input_type="python"))
    else:
        input_type = request.args.get("input_type")
        return render_template("latex.html", input_type=input_type, init_flag=1)


@Math.route("/lim", methods=["GET", "POST"])
def lim_view():
    if(request.method == "POST"):
        formula = request.form.get("formula")
        a = request.form.get("a")
        anser = lim.lim(formula, a)
        return render_template("lim.html", formula=formula, a=a, anser=anser, init_flag=0)
    else:
        return render_template("lim.html", a=0, init_flag=1)


@Math.route("/matrix", methods=["GET", "POST"])
def matrix_view():
    if request.method == "POST":
        matrixA = request.form.get("matrix")
        Ar = request.form.get("Ar")
        Ac = request.form.get("Ac")
        type = request.form.get("type")
        anser = matrix.calculation(matrixA, Ar, Ac, type)
        return render_template("matrix.html", matrix=matrixA, Ar=Ar, Ac=Ac, type=type, anser=anser, init_flag=0)
    else:
        return render_template("matrix.html", Ar=2, Ac=2, type="A", init_flag=1)


@Math.route("/matrix_2", methods=["GET", "POST"])
def matrix_2_view():
    if request.method == "POST":
        matrixA = request.form.get("matrixA")
        matrixB = request.form.get("matrixB")
        Ar = request.form.get("Ar")
        Ac = request.form.get("Ac")
        Br = request.form.get("Br")
        Bc = request.form.get("Bc")
        type = request.form.get("type")
        k = request.form.get("k")
        l = request.form.get("l")

        anser = matrix_2.calculation(
            matrixA, matrixB, Ar, Ac, Br, Bc, type, k, l)
        return render_template("matrix_2.html", matrixA=matrixA, matrixB=matrixB, Ar=Ar, Ac=Ac, Br=Br, Bc=Bc, type=type, k=k, l=l, anser=anser, init_flag=0)
    else:
        return render_template("matrix_2.html", Ar=2, Ac=2, Br=2, Bc=2, type="A", k=2, l=2, init_flag=1)


@Math.route("/max_min", methods=["GET", "POST"])
def max_min_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        Anser = max_min.max_min(formula)
        return render_template("max_min.html", formula=formula, Anser=Anser, init_flag=0)
    else:
        return render_template("max_min.html", init_flag=1)


@Math.route("/newton_method", methods=["GET", "POST"])
def newton_method_view():
    if request.method == "POST":
        number = request.form.get("number")
        anser = newton_method.newton_method(number)
        return render_template("newton_method.html", number=number, anser=anser, init_flag=0)
    else:
        return render_template("newton_method.html", init_flag=1)


@Math.route("/nyquist", methods=["GET", "POST"])
def nyquist_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        return render_template("nyquist.html", formula=formula, init_flag=0)
    else:
        return render_template("nyquist.html", init_flag=1)


@Math.route('/nyquist.png')
def nyquist_png():
    formula = request.args.get("formula")
    response = nyquist.nyquist(formula)
    return response


@Math.route("/prime_factorization", methods=["GET", "POST"])
def prime_factorization_view():
    if request.method == "POST":
        number = request.form.get("number")
        anser = prime_factorization.prime_factorization(number)
        return render_template("prime_factorization.html", number=number, anser=anser, init_flag=0)
    else:
        return render_template("prime_factorization.html", init_flag=1)


@Math.route("/Sieve_of_Eratosthenes", methods=["GET", "POST"])
def Sieve_of_Eratosthenes_view():
    if request.method == "POST":
        number = request.form.get("number")
        Anser = Sieve_of_Eratosthenes.Sieve_of_Eratosthenes(number)
        return render_template("Sieve_of_Eratosthenes.html", number=number, Anser=Anser, init_flag=0)
    else:
        return render_template("Sieve_of_Eratosthenes.html", init_flag=1)


@Math.route("/sysio", methods=["GET", "POST"])
def sysio_view():
    if request.method == "POST":
        formula = request.form.get("formula")
        formula_2 = request.form.get("formula_2")
        lower_end = request.form.get("lower_end")
        upper_end = request.form.get("upper_end")
        type = request.args.get("type")
        return render_template("sysio.html", formula=formula, formula_2=formula_2, lower_end=lower_end, upper_end=upper_end, type=type, init_flag=0)
    else:
        type = request.args.get("type")
        if(type == "s" or type == "t"):
            return render_template("sysio.html", lower_end=-2, upper_end=5, type=type, init_flag=1)
        else:
            return redirect(url_for('Math.sysio_view', type='s'))


@Math.route("/sysio_graph", methods=["GET", "POST"])
def sysio_graph_png():
    formula = request.args.get("formula")
    formula_2 = request.args.get("formula_2")
    lower_end = request.args.get("lower_end")
    upper_end = request.args.get("upper_end")
    type = request.args.get("type")
    try:
        response = sysio.sysio(
            formula, formula_2, lower_end, upper_end, type=type)
        return response
    except:
        flash("Error")
        return "Error"


@Math.route("/taylor", methods=["GET", "POST"])
def taylor_view():
    if(request.method == "POST"):
        formula = request.form.get("formula")
        dimension = request.form.get("dimension")
        center = request.form.get("center")
        Anser = taylor.taylor(formula, dimension, center)
        return render_template("taylor.html", formula=formula, dimension=dimension, center=center, Anser=Anser, init_flag=0)
    else:
        return render_template("taylor.html", dimension=10, center=0, init_flag=1)
