window.addEventListener("load", () => {
  var mydata;
  if (!localStorage.getItem("mydata")) {
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      mydata = "dark";
    } else {
      mydata = "light";
    }
    localStorage.setItem("mydata", mydata);
  } else {
    mydata = localStorage.getItem("mydata");
  }
  classToggle(mydata);
});

function dataToggle() {
  pre_mydata = localStorage.getItem("mydata");
  if (pre_mydata == "dark") {
    mydata = "light";
  } else {
    mydata = "dark";
  }
  localStorage.setItem("mydata", mydata);
  classToggle(mydata);
}

function classToggle(mydata) {
  target = document.getElementById("target");
  checkbox = document.getElementById("checkbox");
  if (mydata == "dark") {
    target.classList.add("bootstrap-dark");
    target.classList.remove("bootstrap");
    target.classList.add("radioAreaDark");
    target.classList.remove("radioArea");
    checkbox.checked = false;
  } else {
    target.classList.add("bootstrap");
    target.classList.remove("bootstrap-dark");
    target.classList.add("radioArea");
    target.classList.remove("radioAreaDark");
    checkbox.checked = true;
  }

  const result = document.getElementsByClassName("heading");
  if (mydata == "dark") {
    for (let i = 0; i < result.length; i++) {
      result[i].classList.add("heading_dark");
    }
  } else {
    for (let i = 0; i < result.length; i++) {
      result[i].classList.remove("heading_dark");
    }
  }
}
