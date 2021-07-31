function clickBtn1(dimension) {
  const t1 = document.getElementById("BeforeConversion").value;
  document.getElementById("BeforeConversion").value =
    t1 + dimension.target.eventParam;
}

function clickdel1(idx) {
  const t1 = document.getElementById("BeforeConversion").value;
  if (idx.target.eventParam == 4) {
    document.getElementById("BeforeConversion").value = t1.slice(0, -1);
  } else if (idx.target.eventParam == 5) {
    document.getElementById("BeforeConversion").value = t1.slice(0, 0);
  }
}

window.onload = function () {
  var parent = document.getElementById("parent");

  var child = document.createElement("div");
  child.style.border = "2px solid #6091d3";
  // child.style.borderRadius = "10px";
  child.classList.add("center");

  var child1InnerText = ["a", "b", "c", "d"];
  var child1 = document.createElement("div");
  for (var i = 0; i < 14; i++) {
    var element = document.createElement("button");
    if (i < 10) {
      element.innerText = i;
    } else {
      element.innerText = child1InnerText[i - 10];
    }
    element.addEventListener("click", clickBtn1, false);
    element.eventParam = String(i);
    element.classList.add("btn", "btn-outline-info");
    element.style.marginTop = "2px";
    element.style.marginBottom = "2px";
    element.style.marginRight = "1px";
    element.style.padding = "1.5vh 7.3vw 1.5vh 7.3vw";
    child1.appendChild(element);
  }
  child.appendChild(child1);

  var child4InnerText = ["0b", "0o", "0d", "0x", "消去", "全消去"];
  var child4 = document.createElement("div");
  for (var i = 0; i < 6; i++) {
    var element = document.createElement("button");
    element.innerText = child4InnerText[i];
    if (i < 4) {
      element.addEventListener("click", clickBtn1, false);
      element.eventParam = child4InnerText[i];
      element.classList.add("btn", "btn-outline-info");
    } else {
      element.addEventListener("click", clickdel1, false);
      element.eventParam = i;
      element.classList.add("btn", "btn-outline-danger");
    }
    element.style.marginBottom = "2px";
    element.style.marginRight = "1px";
    element.style.padding = "1.5vh 3.65vw 1.5vh 3.65vw";
    child4.appendChild(element);
  }
  child.appendChild(child4);

  parent.appendChild(child);
};
