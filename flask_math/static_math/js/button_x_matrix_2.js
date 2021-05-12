function clickBtn1(dimension) {
  const t1 = document.getElementById("InputMatrix").value;
  document.getElementById("InputMatrix").value = t1 + dimension.target.eventParam;
}
function clickBtn2(dimension) {
  const t2 = document.getElementById("InputMatrix_2").value;
  document.getElementById("InputMatrix_2").value = t2 + dimension.target.eventParam;
}

function clickdel1(idx) {
  const t1 = document.getElementById("InputMatrix").value;
  if (idx.target.eventParam == 0) {
    document.getElementById("InputMatrix").value = t1 + "  ";
  } else if (idx.target.eventParam == 1) {
    document.getElementById("InputMatrix").value = t1 + "\n";
  } else if (idx.target.eventParam == 2) {
    t1_2 = t1.replace(/exp/g, "EP");
    t1_3 = t1_2.replace(/x/g, "s");
    t1_4 = t1_3.replace(/EP/g, "exp");
    document.getElementById("InputMatrix").value = t1_4;
  } else if (idx.target.eventParam == 3) {
    document.getElementById("InputMatrix").value = t1.replace(/s/g, "x");
  } else if (idx.target.eventParam == 4) {
    document.getElementById("InputMatrix").value = t1.slice(0, -1);
  } else if (idx.target.eventParam == 5) {
    document.getElementById("InputMatrix").value = t1.slice(0, 0);
  }
}
function clickdel2(idx) {
  const t2 = document.getElementById("InputMatrix_2").value;
  if (idx.target.eventParam == 0) {
    document.getElementById("InputMatrix_2").value = t2 + "  ";
  } else if (idx.target.eventParam == 1) {
    document.getElementById("InputMatrix_2").value = t2 + "\n";
  } else if (idx.target.eventParam == 2) {
    t2_2 = t2.replace(/exp/g, "EP");
    t2_3 = t2_2.replace(/x/g, "s");
    t2_4 = t2_3.replace(/EP/g, "exp");
    document.getElementById("InputMatrix_2").value = t2_4;
  } else if (idx.target.eventParam == 3) {
    document.getElementById("InputMatrix_2").value = t2.replace(/s/g, "x");
  } else if (idx.target.eventParam == 4) {
    document.getElementById("InputMatrix_2").value = t2.slice(0, -1);
  } else if (idx.target.eventParam == 5) {
    document.getElementById("InputMatrix_2").value = t2.slice(0, 0);
  }
}

window.onload = function () {
  for (var j = 1; j <= 2; j++) {
    if (j == 1) {
      var parent = document.getElementById("parent");
    } else {
      var parent = document.getElementById("parent_2");
    }

    var child = document.createElement("div");
    child.style.border = "2px solid #6091d3";
    // child.style.borderRadius = "10px";
    child.classList.add("center");

    var child1 = document.createElement("div");
    for (var i = 0; i < 10; i++) {
      var element = document.createElement("button");
      element.innerText = i;
      if (j == 1) {
        element.addEventListener("click", clickBtn1, false);
      } else {
        element.addEventListener("click", clickBtn2, false);
      }
      element.eventParam = String(i);
      element.classList.add("btn", "btn-outline-info");
      element.style.marginTop = "2px";
      element.style.marginBottom = "2px";
      element.style.marginRight = "1px";
      element.style.padding = "6px 10.7px 6px 10.7px";
      child1.appendChild(element);
    }
    child.appendChild(child1);

    var child2InnerText = ["x", "y", "z", "s", "t", "+", "-", "/", "(", ")"];
    var child2 = document.createElement("div");
    for (var i = 0; i < 10; i++) {
      var element = document.createElement("button");
      element.innerText = child2InnerText[i];
      if (j == 1) {
        element.addEventListener("click", clickBtn1, false);
      } else {
        element.addEventListener("click", clickBtn2, false);
      }
      element.eventParam = child2InnerText[i];
      element.classList.add("btn", "btn-outline-info");
      element.style.marginBottom = "2px";
      element.style.marginRight = "1px";
      element.style.padding = "6px 11.9px 6px 11.9px";
      child2.appendChild(element);
    }
    child.appendChild(child2);

    var child3InnerText = ["*", "**", "exp(", "sin(", "cos(", "Us(", "δ("];
    var child3Parameter = ["*", "**", "exp(", "sin(", "cos(", "Heaviside(", "DiracDelta("];
    var child3 = document.createElement("div");
    for (var i = 0; i < 7; i++) {
      var element = document.createElement("button");
      element.innerText = child3InnerText[i];
      if (j == 1) {
        element.addEventListener("click", clickBtn1, false);
      } else {
        element.addEventListener("click", clickBtn2, false);
      }
      element.eventParam = child3Parameter[i];
      element.classList.add("btn", "btn-outline-info");
      element.style.marginBottom = "2px";
      element.style.marginRight = "1px";
      element.style.padding = "6px 11.7px 6px 11.8px";
      child3.appendChild(element);
    }
    child.appendChild(child3);

    var child4InnerText = ["空白", "改行", "x→s", "s→x", "消去", "全消去"];
    var child4 = document.createElement("div");
    for (var i = 0; i < 6; i++) {
      var element = document.createElement("button");
      element.innerText = child4InnerText[i];
      if (j == 1) {
        element.addEventListener("click", clickdel1, false);
      } else {
        element.addEventListener("click", clickdel2, false);
      }
      element.eventParam = i;
      element.classList.add("btn", "btn-outline-danger");
      element.style.marginBottom = "2px";
      element.style.marginRight = "1px";
      element.style.padding = "6px 9.4px 6px 9.3px";
      child4.appendChild(element);
    }
    child.appendChild(child4);

    parent.appendChild(child);
  }
};
