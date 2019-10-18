let authBtn = document.querySelector(".auth-btn");
let popupAuth = document.querySelector(".auth-block");
let popupReg = document.querySelector(".reg-block");
let regBtn = document.querySelector(".reg-btn");


$('.bots-nav-item').click(function (e) {
    $('.bots-nav-item').removeClass('selected');
    $(this).addClass('selected');
});

$(function () {
    if ($('.bots').children.length) {
        $('.bots').append("<p>нет ботов в данной категории</p>")
    }
});

$('#messenger-selector').click(function (e) {
    if ($(e.target).hasClass('hideable'))
        $(e.target).addClass('hidden');

});

function addPair() {
    var template =  $('.pair.template').clone();
    $(template).removeClass('template');
    $('.commands').prepend(template);
}

$('.create-new-btn').click(function (e) {
    e.preventDefault();
    $('#messenger-selector').removeClass('hidden');
    $('#telegram-check').prop('checked', false);
    $('.go-to-create-btn').prop('disabled', 'disabled');
});

// Переделать чекинг
$('#messenger-selector input[type=checkbox]').change(function() {
    $('.go-to-create-btn').removeClass('disabled');
});

$('.btn').click(function (e) {
    if ($(this).hasClass('disabled'))
        e.preventDefault();
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

$(function () {
    if ($('.bots').children.length) {
        $('.bots').append("<p>нет ботов в данной категории</p>")
    }
});

// $(function(){
//             $('numeral').each(function (i) {
//                 $(this).html(i+1);
//             });
//         });
