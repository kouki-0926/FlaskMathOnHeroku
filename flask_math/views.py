from flask import request,redirect,url_for,render_template,flash,Blueprint,make_response
from flask_math.calculation import *

Math=Blueprint("Math",__name__,template_folder='templates',static_folder="static")

@Math.route("/index")
def index_view():
    return render_template("index.html")


@Math.route("/index_2")
def index_2_view():
    return render_template("index_2.html")


@Math.route("/instructions")
def instructions_view():
    return render_template("instructions.html")


@Math.route("/Apart",methods=["GET","POST"])
def Apart_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Apart.Apart(formula)
        return render_template("Apart.html",formula=formula,anser=anser,init_flag=0)
    else:
        return render_template("Apart.html",init_flag=1)


@Math.route("/base_conversion",methods=["GET","POST"])
def base_conversion_view():
    if request.method=="POST":
        try:
            if request.form.get("bin")!="":
                base="binary"
                before_conversion=request.form.get("bin")
            elif request.form.get("oct")!="":
                base="octal"
                before_conversion=request.form.get("oct")
            elif request.form.get("dec")!="":
                base="decimal"
                before_conversion=request.form.get("dec")
            elif request.form.get("hex")!="":
                base="hexadecimal"
                before_conversion=request.form.get("hex")
            anser=base_conversion.base_conversion(base,before_conversion)
        except:
            anser=["Error","Error","Error","Error"]
            flash("エラー：もう一度入力してください")
        return render_template("base_conversion.html",bin=anser[0],oct=anser[1],dec=anser[2],hex=anser[3])
    else:
        return render_template("base_conversion.html")


@Math.route("/BMI",methods=["GET","POST"])
def BMI_view():
    if request.method=="POST":
        height=request.form.get("height")
        weight=request.form.get("weight")
        anser=BMI.BMI(height,weight)
        return render_template("BMI.html",height=height,weight=weight,anser_0=anser[0],anser_1=anser[1])
    else:
        return render_template("BMI.html")


@Math.route("/derivative",methods=["GET","POST"])
def derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        type=request.form.get("type")
        Anser=derivative.derivative(formula,type)
        return render_template("derivative.html",formula=formula,type=type,Anser=Anser,init_flag=0)
    else:
        return render_template("derivative.html",type="x",init_flag=1)


@Math.route("/diff_equation",methods=["GET","POST"])
def diff_equation_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=diff_equation.diff_equation(formula)
        return render_template("diff_equation.html",formula=formula,Anser=Anser)
    else:
        return render_template("diff_equation.html")


@Math.route("/equation",methods=["GET","POST"])
def equation_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=equation.equation(formula)
        return render_template("equation.html",formula=formula,Anser=Anser)
    else:
        return render_template("equation.html")


@Math.route("/equations",methods=["GET","POST"])
def equations_view():
    try:
        if request.method=="POST":
            number=int(request.form.get("number"))
            if number==1:
                formula_1=request.form.get("formula_1")
                Formula=[formula_1]
                Anser=equations.equations(Formula,number)
                return render_template("equations.html",formula_1=formula_1,Anser=Anser,number=number)
            elif number==2:
                formula_1=request.form.get("formula_1")
                formula_2=request.form.get("formula_2")
                Formula=[formula_1,formula_2]
                Anser=equations.equations(Formula,number)
                return render_template("equations.html",formula_1=formula_1,formula_2=formula_2,Anser=Anser,number=number)
            elif number==3:
                formula_1=request.form.get("formula_1")
                formula_2=request.form.get("formula_2")
                formula_3=request.form.get("formula_3")
                Formula=[formula_1,formula_2,formula_3]
                Anser=equations.equations(Formula,number)
                return render_template("equations.html",formula_1=formula_1,formula_2=formula_2,formula_3=formula_3,Anser=Anser,number=number)
            else:
                return render_template("equations.html",number=1)
        else:
            number=int(request.args.get("number"))
            if number>=1 and number<=3:
                return render_template("equations.html",number=number)
            else:
                return redirect(url_for("Math.equations_view",number=1))
    except:
        flash("エラー：もう一度入力してください")
        return render_template("equations.html",number=1)


@Math.route("/Euclidean_Algorithm",methods=["GET","POST"])
def Euclidean_Algorithm_view():
    if request.method=="POST":
        number_x=request.form.get("number_x")
        number_y=request.form.get("number_y")
        anser=Euclidean_Algorithm.Euclidean_Algorithm(number_x,number_y)
        return render_template("Euclidean_Algorithm.html",number_x=number_x,number_y=number_y,anser=anser)
    else:
        return render_template("Euclidean_Algorithm.html")


@Math.route("/Expand",methods=["GET","POST"])
def Expand_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Expand.Expand(formula)
        return render_template("Expand.html",formula=formula,anser=anser,init_flag=0)
    else:
        return render_template("Expand.html",init_flag=1)


@Math.route("/Factorial",methods=["GET","POST"])
def Factorial_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Factorial.Factorial(formula)
        return render_template("Factorial.html",formula=formula,anser=anser)
    else:
        return render_template("Factorial.html")


@Math.route("/factorization",methods=["GET","POST"])
def factorization_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=factorization.factorization(formula)
        return render_template("factorization.html",formula=formula,anser=anser)
    else:
        return render_template("factorization.html")


@Math.route("/graph",methods=["GET","POST"])
def graph_view():
    if request.method=="POST":
        formula_1=request.form.get("formula_1")
        lower_end_x=request.form.get("lower_end_x")
        upper_end_x=request.form.get("upper_end_x")
        return render_template("graph.html",formula_1=formula_1,lower_end_x=lower_end_x,upper_end_x=upper_end_x)
    else:
        return render_template("graph.html",lower_end_x=-10,upper_end_x=10)


@Math.route('/graph.png')
def graph_png():
    formula_1=request.args.get("formula_1")
    lower_end_x=request.args.get("lower_end_x")
    upper_end_x=request.args.get("upper_end_x")
    response=graph.graph(formula_1,lower_end_x,upper_end_x)
    return response


@Math.route("/integral",methods=["GET","POST"])
def integral_view():
    if(request.method=="POST"):
        formula=request.form.get("formula")
        upper_end_x=request.form.get("upper_end_x")
        lower_end_x=request.form.get("lower_end_x")
        Upper_end=[upper_end_x]
        Lower_end=[lower_end_x]
        dimension=request.form.get("dimension")
        type=request.form.get("type")

        if(dimension=="2D"):
            anser=integral.integral(formula,Upper_end,Lower_end,type)
            return render_template("integral.html",formula=formula,upper_end_x=upper_end_x,lower_end_x=lower_end_x,
            dimension=dimension,type=type,anser=anser,init_flag=0)
        else:
            upper_end_y=request.form.get("upper_end_y")
            lower_end_y=request.form.get("lower_end_y")
            Upper_end.append(upper_end_y)
            Lower_end.append(lower_end_y)
            anser=integral.integral(formula,Upper_end,Lower_end,type)
            return render_template("integral.html",formula=formula,upper_end_x=upper_end_x,lower_end_x=lower_end_x,
            upper_end_y=upper_end_y,lower_end_y=lower_end_y,dimension=dimension,type=type,anser=anser,init_flag=0)

    elif(request.method=="GET"):
        dimension=request.args.get("dimension")
        if(dimension=="2D"):
            return render_template("integral.html",dimension=dimension,type="indefinite_integral",init_flag=1)
        elif(dimension=="3D"):
            return render_template("integral.html",dimension=dimension,type="multiple_integral_1",init_flag=1)
        else:
            flash("エラー:dimension")
            return redirect(url_for("Math.integral_view",dimension="2D"))


@Math.route("/latex",methods=["GET","POST"])
def latex_view():
    if(request.method=="POST"):
        input_type=request.form.get("input_type")
        if(input_type=="python"):
            formula_python=request.form.get("formula_python")        
            anser=latex.latex(formula_python)
            return render_template("latex.html",formula_python=formula_python,anser=anser,input_type=input_type,init_flag=0)
        elif(input_type=="latex"):
            formula_latex=request.form.get("formula_latex")
            return render_template("latex.html",formula_latex=formula_latex,anser=formula_latex,input_type=input_type,init_flag=0)
        else:
            return redirect(url_for("Math.latex_view",input_type="python"))
    else:
        input_type=request.args.get("input_type")
        return render_template("latex.html",input_type=input_type,init_flag=1)


@Math.route("/lim",methods=["GET","POST"])
def lim_view():
    if(request.method=="POST"):
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=lim.lim(formula,a)
        return render_template("lim.html",formula=formula,a=a,anser=anser,init_flag=0)
    else:
        return render_template("lim.html",a=0,init_flag=1)


@Math.route("/matrix",methods=["GET","POST"])
def matrix_view():
    if request.method=="POST":
        matrixA=request.form.get("matrix")
        Ar=request.form.get("Ar")
        Ac=request.form.get("Ac")
        type=request.form.get("type")

        Anser=matrix.calculation(matrixA,Ar,Ac,type)

        if Anser[4]=="MATRIX":
            anser=[]
            for i in range(Anser[1]):
                A=str(Anser[0].row(i))
                A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
                anser.append(A)
        elif Anser[4]=="NUMBER":
            anser=Anser[0]
        return render_template("matrix.html",matrix=matrixA,Ar=Ar,Ac=Ac,type=type,anser_0=anser,anser_3=Anser[3])
    else:
        return render_template("matrix.html",Ar=2,Ac=2,type="A")


@Math.route("/matrix_2",methods=["GET","POST"])
def  matrix_2_view():
    if request.method=="POST":
        matrixA=request.form.get("matrixA")
        matrixB=request.form.get("matrixB")
        Ar=request.form.get("Ar")
        Ac=request.form.get("Ac")
        Br=request.form.get("Br")
        Bc=request.form.get("Bc")
        type=request.form.get("type")
        k=request.form.get("k")
        l=request.form.get("l")

        Anser=matrix_2.calculation(matrixA,matrixB,Ar,Ac,Br,Bc,type,k,l)

        anser=[]
        if Anser[4]=="NUMBER":
            anser=[Anser[0]]
        elif Anser[4]=="MATRIX":
            for i in range(Anser[2]):
                A=str(Anser[0].row(i))
                A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
                anser.append(A)
        return render_template("matrix_2.html",matrixA=matrixA,matrixB=matrixB,Ar=Ar,Ac=Ac,Br=Br,Bc=Bc,type=type,k=k,l=l,
        anser_0=anser,anser_1=Anser[1])
    else:
        return render_template("matrix_2.html",Ar=2,Ac=2,Br=2,Bc=2,type="A",k=2,l=2)


@Math.route("/max_min",methods=["GET","POST"])
def max_min_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=max_min.max_min(formula)
        return render_template("max_min.html",formula=formula,Anser=Anser)
    else:
        return render_template("max_min.html")


@Math.route("/newton_method",methods=["GET","POST"])
def  newton_method_view():
    if request.method=="POST":
        number=request.form.get("number")
        Anser=newton_method.newton_method(number)
        return render_template("newton_method.html",number=number,anser_0=Anser[0],anser_1=Anser[1])
    else:
        return render_template("newton_method.html",anser_0="initial")


@Math.route("/prime_factorization",methods=["GET","POST"])
def prime_factorization_view():
    if request.method=="POST":
        number=request.form.get("number")
        anser=prime_factorization.prime_factorization(number)
        return render_template("prime_factorization.html",number=number,anser=anser,init_flag=0)
    else:
        return render_template("prime_factorization.html",init_flag=1)


@Math.route("/Sieve_of_Eratosthenes",methods=["GET","POST"])
def  Sieve_of_Eratosthenes_view():
    if request.method=="POST":
        number=request.form.get("number")
        Anser=Sieve_of_Eratosthenes.Sieve_of_Eratosthenes(number)
        return render_template("Sieve_of_Eratosthenes.html",number=number,Anser=Anser)
    else:
        return render_template("Sieve_of_Eratosthenes.html")


@Math.route("/taylor",methods=["GET","POST"])
def  taylor_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        dimension=request.form.get("dimension")
        center=request.form.get("center")
        Anser=taylor.taylor(formula,dimension,center)
        return render_template("taylor.html",formula=formula,dimension=dimension,center=center,Anser=Anser,init_flag=0)
    else:
        return render_template("taylor.html",dimension=10,center=0,init_flag=1)
