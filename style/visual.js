$('.bots-nav-item').click(function (e) {
    $('.bots-nav-item').removeClass('selected');
    $(this).addClass('selected');
})

$(function () {
    $('header').load('header.html');

    if ($('.bots').children.length) {
        $('.bots').append("<p>нет ботов в данной категории</p>")
    }
})
