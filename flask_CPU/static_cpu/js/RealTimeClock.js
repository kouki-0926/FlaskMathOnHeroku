function setfig(num) {
    var ret;
    if (num < 10) {
        ret = "0" + num;
    } else {
        ret = num;
    }
    return ret;
}

function showClock() {
    var nowTime = new Date();
    var nowHour = setfig(nowTime.getHours());
    var nowMin = setfig(nowTime.getMinutes());
    var nowSec = setfig(nowTime.getSeconds());
    var msg = "現在時刻:" + nowHour + ":" + nowMin + ":" + nowSec;
    document.getElementById("RealtimeClock").innerHTML = msg;
}
setInterval('showClock()', 1000);
