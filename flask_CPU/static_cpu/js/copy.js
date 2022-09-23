function copy() {
    const element = document.querySelector('#en_text');
    const selection = window.getSelection();
    const range = document.createRange();

    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
    const succeeded = document.execCommand('copy');

    if (succeeded) {
        alert('コピーが成功しました！');
    } else {
        alert('コピーが失敗しました!');
    }
    selection.removeAllRanges();
}