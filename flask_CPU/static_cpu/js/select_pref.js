window.onload = function () {
  pref = document.getElementById("pref");
  region = document.getElementById("region");
  region.onchange = changeregion;
}

function changeregion() {
  pref.textContent = null;
  var changedRegion = region.value;
  if (changedRegion == "北海道") {
    pref_list = [
      { cd: "012010", label: "道北・旭川" },
      { cd: "014020", label: "道東・釧路" },
      { cd: "016010", label: "道央・札幌" },
      { cd: "017010", label: "道南・函館" }
    ];
  } else if (changedRegion == "東北") {
    pref_list = [
      { cd: "020010", label: "青森県・青森" },
      { cd: "030010", label: "岩手県・盛岡" },
      { cd: "040010", label: "宮城県・仙台" },
      { cd: "050010", label: "秋田県・秋田" },
      { cd: "060010", label: "山形県・山形" },
      { cd: "070010", label: "福島県・福島" }
    ];
  } else if (changedRegion == "関東") {
    pref_list = [
      { cd: "080010", label: "茨城県・水戸" },
      { cd: "090010", label: "栃木県・宇都宮" },
      { cd: "100010", label: "群馬県・前橋" },
      { cd: "110010", label: "埼玉県・さいたま" },
      { cd: "120010", label: "千葉県・千葉" },
      { cd: "130010", label: "東京都・東京" },
      { cd: "140010", label: "神奈川県・横浜" }
    ];
  } else if (changedRegion == "中部") {
    pref_list = [
      { cd: "150010", label: "新潟県・新潟" },
      { cd: "160010", label: "富山県・富山" },
      { cd: "170010", label: "石川県・金沢" },
      { cd: "180010", label: "福井県・福井" },
      { cd: "190010", label: "山梨県・甲府" },
      { cd: "200010", label: "長野県・長野" },
      { cd: "210010", label: "岐阜県・岐阜" },
      { cd: "220010", label: "静岡県・静岡" },
      { cd: "230010", label: "愛知県・名古屋" },
      { cd: "240010", label: "三重県・津" }
    ];
  } else if (changedRegion == "近畿") {
    pref_list = [
      { cd: "250010", label: "滋賀県・大津" },
      { cd: "260010", label: "京都府・京都" },
      { cd: "270000", label: "大阪府・大阪" },
      { cd: "280010", label: "兵庫県・神戸" },
      { cd: "290010", label: "奈良県・奈良" },
      { cd: "300010", label: "和歌山県・和歌山" }
    ];
  } else if (changedRegion == "中国") {
    pref_list = [
      { cd: "310010", label: "鳥取県・鳥取" },
      { cd: "320010", label: "島根県・松江" },
      { cd: "330010", label: "岡山県・岡山" },
      { cd: "340010", label: "広島県・広島" },
      { cd: "350020", label: "山口県・山口" }
    ];
  } else if (changedRegion == "四国") {
    pref_list = [
      { cd: "360010", label: "徳島県・徳島" },
      { cd: "370000", label: "香川県・高松" },
      { cd: "380010", label: "愛媛県・松山" },
      { cd: "390010", label: "高知県・高知" }
    ];
  } else if (changedRegion == "九州・沖縄") {
    pref_list = [
      { cd: "400010", label: "福岡県・福岡" },
      { cd: "410010", label: "佐賀県・佐賀" },
      { cd: "420010", label: "長崎県・長崎" },
      { cd: "430010", label: "熊本県・熊本" },
      { cd: "440010", label: "大分県・大分" },
      { cd: "450010", label: "宮崎県・宮崎" },
      { cd: "460010", label: "鹿児島県・鹿児島" },
      { cd: "471010", label: "沖縄県・那覇" }
    ];
  }
  region_list_2 = [
    { cd: "", label: "地点を選択して下さい" }
  ];
  region_list_2.forEach(function (value) {
    var op_2 = document.createElement("option");
    op_2.value = value.cd;
    op_2.text = value.label;
    pref.appendChild(op_2);
  });

  region_list=[{label:changedRegion}];
  region_list.forEach(function (value) {
    var opt = document.createElement("optgroup");
    opt.label = value.label;
    pref.appendChild(opt);
  });

  pref_list.forEach(function (value) {
    var op = document.createElement("option");
    op.value = value.cd;
    op.text = value.label;
    pref.appendChild(op);
  });
}