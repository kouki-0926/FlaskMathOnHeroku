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
    var weeks = new Array('日', '月', '火', '水', '木', '金', '土')

    var nowTime = new Date();
    var nowYear = setfig(nowTime.getFullYear() - 2018);
    var nowMonth = setfig(nowTime.getMonth() + 1);
    var nowDay = setfig(nowTime.getDate());
    var nowWeek = weeks[nowTime.getDay()];
    var nowHour = setfig(nowTime.getHours());
    var nowMin = setfig(nowTime.getMinutes());
    var nowSec = setfig(nowTime.getSeconds());
    var msg = "令和" + nowYear + "/" + nowMonth + "/" + nowDay + "(" + nowWeek + ") " + nowHour + ":" + nowMin + ":" + nowSec;
    document.getElementById("RealtimeClock").innerHTML = msg;
}
setInterval('showClock()', 1000);
