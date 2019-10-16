$(function () {
    $('header').load('header.html');
})

$('.bots-nav-item').click(function (e) {
    $('.bots-nav-item').removeClass('selected');
    $(this).addClass('selected');
})

$(function () {
    if ($('.bots').children.length) {
        $('.bots').append("<p>нет ботов в данной категории</p>")
    }
})

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
})

// Переделать чекинг
$('#messenger-selector input[type=checkbox]').change(function() {
    $('.go-to-create-btn').removeClass('disabled');
})

$('.btn').click(function (e) {
    if ($(this).hasClass('disabled'))
        e.preventDefault();
})

