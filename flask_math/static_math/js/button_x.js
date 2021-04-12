function clickBtn1(dimension) {
  const t1 = document.getElementById("InputFormula").value;
  document.getElementById("InputFormula").value =
    t1 + dimension.target.eventParam;
}

function clickdel(idx) {
  const t1 = document.getElementById("InputFormula").value;
  if (idx.target.eventParam == 0) {
    document.getElementById("InputFormula").value = t1.slice(0, -1);
  }else if (idx.target.eventParam == 1) {
    document.getElementById("InputFormula").value = t1.slice(0, 0);
  }
}

window.onload = function () {
  var parent = document.getElementById("parent");

  var child1 = document.createElement("div");
  for (var i = 0; i <= 9; i++) {
    var element = document.createElement("button");
    element.innerText = i;
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = String(i);
    element.classList.add("btn", "btn-outline-info");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "8px 8px 8px 8px";
    child1.appendChild(element);
  }
  parent.appendChild(child1);

  var child2 = document.createElement("div");
  for (var i = 1; i < 6; i++) {
    var element = document.createElement("button");
    element.innerText = "*x**" + i + "+";
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = "*x**" + String(i) + "+";
    element.classList.add("btn", "btn-outline-info");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "5px 5px 5px 5px";
    child2.appendChild(element);
  }
  parent.appendChild(child2);

  var innerText = ["末尾の1文字消去", "全消去"];
  var child3 = document.createElement("div");
  for (var i = 0; i <= 1; i++) {
    var element = document.createElement("button");
    element.innerText = innerText[i];
    element.addEventListener("click", clickdel, false);
    element.eventParam = i;
    element.classList.add("btn", "btn-outline-danger");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "5px 5px 5px 5px";
    child3.appendChild(element);
  }
  parent.appendChild(child3);

  parent.appendChild(document.createElement("br"));
  parent.appendChild(document.createElement("br"));
};
