let authBtn = document.querySelector(".auth-btn");
let popupAuth = document.querySelector(".auth-block");
let popupReg = document.querySelector(".reg-block");
let popupDialog = document.querySelector(".dialog-block");
let regBtn = document.querySelector(".reg-btn");
let authCloseBtn = document.querySelector(".auth-close-btn");
let regCloseBtn = document.querySelector(".reg-close-btn");
let addKeysBtn = document.querySelector(".add-keys-to-bot");
console.log("Ок");

addKeysBtn.addEventListener("click", function (evt) {
    console.log("Ок");

    // if(popupDialog.classList.contains("modal-show")){
    //     popupDialog.classList.remove("modal-show");
    // }
    // evt.preventDefault();
    popupDialog.classList.toggle("modal-show");
});


$('.bots-nav-item').click(function (e) {
    $('.bots-nav-item').removeClass('selected');
    $(this).addClass('selected');
});

$(function () {
    $('header').load('header.html');
    if ($('.bots').children.length) {
        $('.bots').append("<p>нет ботов в данной категории</p>")
    }
});
authBtn.addEventListener("click", function (evt) {
    evt.preventDefault();
    if(popupReg.classList.contains("modal-show")){
    	popupReg.classList.remove("modal-show");
    }
    popupAuth.classList.add("modal-show");
});

regBtn.addEventListener("click", function (evt) {
	if(popupAuth.classList.contains("modal-show")){
    	popupAuth.classList.remove("modal-show");
    }
    evt.preventDefault();
    popupReg.classList.add("modal-show");
});


authCloseBtn.addEventListener("click", function (evt) {
	evt.preventDefault();
  	popupAuth.classList.remove("modal-show");

    
});

regCloseBtn.addEventListener("click", function (evt) {
	evt.preventDefault();
  	popupReg.classList.toggle("modal-show");

});


