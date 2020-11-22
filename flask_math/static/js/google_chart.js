function addValue() {
    var s = document.getElementById("InputFormulaLatex").value;
    document.getElementById('wrapper').src = "https://chart.apis.google.com/chart?chs=60&cht=tx&chl=" + s;
}