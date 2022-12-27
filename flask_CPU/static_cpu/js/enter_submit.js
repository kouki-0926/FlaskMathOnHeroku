// Enterキー押下時、送信処理が実行する
window.document.onkeydown = function (event) {
  if (event.key === "Enter") {
    document.form_text.submit();
  }
};
