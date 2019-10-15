let authBtn = document.querySelector(".auth-btn");
let popupAuth = document.querySelector(".auth-block");
let popupReg = document.querySelector(".reg-block");
let regBtn = document.querySelector(".reg-btn");


console.log("Ок");

$('.bots-nav-item').click(function (e) {
    $('.bots-nav-item').removeClass('selected');
    $(this).addClass('selected');
});

$(function () {
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
