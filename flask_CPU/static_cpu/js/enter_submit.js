// Enterキー押下時, 送信処理を実行する
window.document.onkeydown = function (event) {
  if (event.key === "Enter") {
    document.form_text.submit();
  }
};
