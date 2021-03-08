window.onload = function () {
  pref = document.getElementById("pref");
  region = document.getElementById("region");
  region.onchange = changeregion;
};

function changeregion() {
  pref.textContent = null;
  var changedRegion = region.value;
  if (changedRegion == "北海道") {
    pref_list = [
      { cd: "011000", label: "稚内" },
      { cd: "012010", label: "旭川" },
      { cd: "012020", label: "留萌" },
      { cd: "013010", label: "網走" },
      { cd: "013020", label: "北見" },
      { cd: "013030", label: "紋別" },
      { cd: "014010", label: "根室" },
      { cd: "014020", label: "釧路" },
      { cd: "014030", label: "帯広" },
      { cd: "015010", label: "室蘭" },
      { cd: "015020", label: "浦河" },
      { cd: "016010", label: "札幌" },
      { cd: "016020", label: "岩見沢" },
      { cd: "016030", label: "倶知安" },
      { cd: "017010", label: "函館" },
      { cd: "017020", label: "江差" },
    ];
  } else if (changedRegion == "東北") {
    pref_list = [
      { cd: "020010", label: "青森" },
      { cd: "020020", label: "むつ" },
      { cd: "020030", label: "八戸" },
      { cd: "030010", label: "盛岡" },
      { cd: "030020", label: "宮古" },
      { cd: "030030", label: "大船渡" },
      { cd: "040010", label: "仙台" },
      { cd: "040020", label: "白石" },
      { cd: "050010", label: "秋田" },
      { cd: "050020", label: "横手" },
      { cd: "060010", label: "山形" },
      { cd: "060020", label: "米沢" },
      { cd: "060030", label: "酒田" },
      { cd: "060040", label: "新庄" },
      { cd: "070010", label: "福島" },
      { cd: "070020", label: "小名浜" },
      { cd: "070030", label: "若松" },
    ];
  } else if (changedRegion == "関東") {
    pref_list = [
      { cd: "080010", label: "水戸" },
      { cd: "080020", label: "土浦" },
      { cd: "090010", label: "宇都宮" },
      { cd: "090020", label: "大田原" },
      { cd: "100010", label: "前橋" },
      { cd: "100020", label: "みなかみ" },
      { cd: "110010", label: "さいたま" },
      { cd: "110020", label: "熊谷" },
      { cd: "110030", label: "秩父" },
      { cd: "120010", label: "千葉" },
      { cd: "120020", label: "銚子" },
      { cd: "120030", label: "館山" },
      { cd: "130010", label: "東京" },
      { cd: "130020", label: "大島" },
      { cd: "130030", label: "八丈島" },
      { cd: "130040", label: "父島" },
      { cd: "140010", label: "横浜" },
      { cd: "140020", label: "小田原" },
    ];
  } else if (changedRegion == "中部") {
    pref_list = [
      { cd: "150010", label: "新潟" },
      { cd: "150020", label: "長岡" },
      { cd: "150030", label: "高田" },
      { cd: "150040", label: "相川" },
      { cd: "160010", label: "富山" },
      { cd: "160020", label: "伏木" },
      { cd: "170010", label: "金沢" },
      { cd: "170020", label: "輪島" },
      { cd: "180010", label: "福井" },
      { cd: "180020", label: "敦賀" },
      { cd: "190010", label: "甲府" },
      { cd: "190020", label: "河口湖" },
      { cd: "200010", label: "長野" },
      { cd: "200020", label: "松本" },
      { cd: "200030", label: "飯田" },
      { cd: "210010", label: "岐阜" },
      { cd: "210020", label: "高山" },
      { cd: "220010", label: "静岡" },
      { cd: "220020", label: "網代" },
      { cd: "220030", label: "三島" },
      { cd: "220040", label: "浜松" },
      { cd: "230010", label: "名古屋" },
      { cd: "230020", label: "豊橋" },
      { cd: "240010", label: "津" },
      { cd: "240020", label: "尾鷲" },
    ];
  } else if (changedRegion == "近畿") {
    pref_list = [
      { cd: "250010", label: "大津" },
      { cd: "250020", label: "彦根" },
      { cd: "260010", label: "京都" },
      { cd: "260020", label: "舞鶴" },
      { cd: "270000", label: "大阪" },
      { cd: "280010", label: "神戸" },
      { cd: "280020", label: "豊岡" },
      { cd: "290010", label: "奈良" },
      { cd: "290020", label: "風屋" },
      { cd: "300010", label: "和歌山" },
      { cd: "300020", label: "潮岬" },
    ];
  } else if (changedRegion == "中国") {
    pref_list = [
      { cd: "310010", label: "鳥取" },
      { cd: "310020", label: "米子" },
      { cd: "320010", label: "松江" },
      { cd: "320020", label: "浜田" },
      { cd: "320030", label: "西郷" },
      { cd: "330010", label: "岡山" },
      { cd: "330020", label: "津山" },
      { cd: "340010", label: "広島" },
      { cd: "340020", label: "庄原" },
      { cd: "350010", label: "下関" },
      { cd: "350020", label: "山口" },
      { cd: "350030", label: "柳井" },
      { cd: "350040", label: "萩" },
    ];
  } else if (changedRegion == "四国") {
    pref_list = [
      { cd: "360010", label: "徳島" },
      { cd: "360020", label: "日和佐" },
      { cd: "370000", label: "高松" },
      { cd: "380010", label: "松山" },
      { cd: "380020", label: "新居浜" },
      { cd: "380030", label: "宇和島" },
      { cd: "390010", label: "高知" },
      { cd: "390020", label: "室戸岬" },
      { cd: "390030", label: "清水" },
    ];
  } else if (changedRegion == "九州") {
    pref_list = [
      { cd: "400010", label: "福岡" },
      { cd: "400020", label: "八幡" },
      { cd: "400030", label: "飯塚" },
      { cd: "400040", label: "久留米" },
      { cd: "410010", label: "佐賀" },
      { cd: "410020", label: "伊万里" },
      { cd: "420010", label: "長崎" },
      { cd: "420020", label: "佐世保" },
      { cd: "420030", label: "厳原" },
      { cd: "420040", label: "福江" },
      { cd: "430010", label: "熊本" },
      { cd: "430020", label: "阿蘇乙姫" },
      { cd: "430030", label: "牛深" },
      { cd: "430040", label: "人吉" },
      { cd: "440010", label: "大分" },
      { cd: "440020", label: "中津" },
      { cd: "440030", label: "日田" },
      { cd: "440040", label: "佐伯" },
      { cd: "450010", label: "宮崎" },
      { cd: "450020", label: "延岡" },
      { cd: "450030", label: "都城" },
      { cd: "450040", label: "高千穂" },
      { cd: "460010", label: "鹿児島" },
      { cd: "460020", label: "鹿屋" },
      { cd: "460030", label: "種子島" },
      { cd: "460040", label: "名瀬" },
    ];
  } else if (changedRegion == "沖縄") {
    pref_list = [
      { cd: "471010", label: "那覇" },
      { cd: "471020", label: "名護" },
      { cd: "471030", label: "久米島" },
      { cd: "472000", label: "南大東" },
      { cd: "473000", label: "宮古島" },
      { cd: "474010", label: "石垣島" },
      { cd: "474020", label: "与那国島" },
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

  region_list = [
    { label: changedRegion }
  ];
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