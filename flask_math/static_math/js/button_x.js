function clickBtn1(dimension) {
  const t1 = document.getElementById("InputFormula").value;
  document.getElementById("InputFormula").value = t1 + dimension.target.eventParam;
}

function clickdel(idx) {
  const t1 = document.getElementById("InputFormula").value;
  if (idx.target.eventParam == 0) {
    document.getElementById("InputFormula").value = t1.replace(/x/g, "s");
  } else if (idx.target.eventParam == 1) {
    document.getElementById("InputFormula").value = t1.replace(/s/g, "x");
  } else if (idx.target.eventParam == 2) {
    document.getElementById("InputFormula").value = t1.slice(0, -1);
  } else if (idx.target.eventParam == 3) {
    document.getElementById("InputFormula").value = t1.slice(0, 0);
  }
}

window.onload = function () {
  var parent = document.getElementById("parent");

  var child = document.createElement("div");
  child.style.border = "2px solid #6091d3";
  child.style.borderRadius = "10px";
  child.classList.add("center", "SPOnly");

  var child1 = document.createElement("div");
  for (var i = 0; i < 10; i++) {
    var element = document.createElement("button");
    element.innerText = i;
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = String(i);
    element.classList.add("btn", "btn-outline-info");
    element.style.marginTop = "5px";
    element.style.marginBottom = "5px";
    element.style.marginRight = "5px";
    element.style.padding = "5px 8px 5px 8px";
    child1.appendChild(element);
  }
  child.appendChild(child1);

  var child2 = document.createElement("div");
  for (var i = 1; i < 6; i++) {
    var element = document.createElement("button");
    element.innerText = "*x**" + i;
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = "*x**" + String(i);
    element.classList.add("btn", "btn-outline-info");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "5px 10px 5px 10px";
    child2.appendChild(element);
  }
  child.appendChild(child2);

  var child3InnerText = ["+", "-", "/", "(", ")"];
  var child3 = document.createElement("div");
  for (var i = 0; i < 5; i++) {
    var element = document.createElement("button");
    element.innerText = child3InnerText[i];
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = child3InnerText[i];
    element.classList.add("btn", "btn-outline-info");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "5px 25px 5px 25px";
    child3.appendChild(element);
  }
  child.appendChild(child3);

  var child4InnerText = ["x=>s", "s=>x", "末尾の1文字消去", "全消去"];
  var child4 = document.createElement("div");
  for (var i = 0; i < 4; i++) {
    var element = document.createElement("button");
    element.innerText = child4InnerText[i];
    element.addEventListener("click", clickdel, false);
    element.eventParam = i;
    element.classList.add("btn", "btn-outline-danger");
    element.style.marginRight = "5px";
    element.style.marginBottom = "5px";
    element.style.padding = "5px 7px 5px 7px";
    child4.appendChild(element);
  }
  child.appendChild(child4);

  parent.appendChild(child);
  parent.appendChild(document.createElement("br"));
  parent.appendChild(document.createElement("br"));
};
