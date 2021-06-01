function OnWindowEvent() {
    let width = $(window).width() - $('.logo').width() - 4 * $('.first').width()
    $('.ln').each(function () {
        $(this).width(width / 4.5)
    })
    $('.arrow').offset({left: $('.selected').offset().left + $('.selected').width() / 2.5})
}

$(document).ready(function () {
    OnWindowEvent()
    $('.header').css('margin-top', 0)
})

$(window).resize(OnWindowEvent)

$('.nav-elem').click(function () {
    $('.selected').toggleClass('selected')
    $(this).toggleClass('selected')
    $('.arrow').offset({left: $(this).offset().left + $(this).width() / 2.5})
})
