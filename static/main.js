// const buttonOpen = document.getElementById('modalOpen');
// const modal = document.getElementById('easyModal');
// const buttonClose = document.getElementsByClassName('modalClose')[0];

// ボタンがクリックされた時
// buttonOpen.addEventListener('click', modalOpen);
// function modalOpen() {
//   modal.style.display = 'block';
// }

// バツ印がクリックされた時
// buttonClose.addEventListener('click', modalClose);
// function modalClose() {
//   modal.style.display = 'none';
// }

// モーダルコンテンツ以外がクリックされた時
// addEventListener('click', outsideClose);
// function outsideClose(e) {
//   if (e.target == modal) {
//     modal.style.display = 'none';
//   }
// }

// --------------------------
const buttonOpen2 = document.getElementById('loginBtn');
const modal2 = document.getElementById('easyModal');
const buttonClose2 = document.getElementsByClassName('modalClose')[0];

// ボタンがクリックされた時
buttonOpen2.addEventListener('click', modalOpen);
function modalOpen() {
  modal2.style.display = 'block';
}

// バツ印がクリックされた時
buttonClose2.addEventListener('click', modalClose);
function modalClose() {
  modal2.style.display = 'none';
}

// モーダルコンテンツ以外がクリックされた時
addEventListener('click', outsideClose);
function outsideClose(e) {
  if (e.target == modal2) {
    modal2.style.display = 'none';
  }
}