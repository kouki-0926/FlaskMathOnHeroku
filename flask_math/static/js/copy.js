function copy() {
    var text = document.getElementById("optional").innerText;
    var area = document.createElement("input");
    area.textContent = text;
    area.type = 'hidden';
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    document.body.removeChild(area);
    alert("コピーしました");
}
