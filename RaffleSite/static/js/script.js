$('.nav-elem').click(function () {
    $('.selected').toggleClass('selected')
    $(this).toggleClass('selected')
})

var wax = new waxjs.WaxJS('https://wax.greymass.com', null, null, false)

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    var host = document.location.host;
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    return (url === origin || url.slice(0, origin.length + 1) === origin + '/') ||
        (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') ||
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (csrftoken && !csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken.value);
        }
    }
});

autoLogin()

$('.login-btn').click(function () {
    login()
})

async function autoLogin() {
    var isAutoLoginAvailable = await wax.isAutoLoginAvailable()
    if (isAutoLoginAvailable) {
        login()
    }
}

async function login() {
    try {
        const userAccount = await wax.login()
        $.post('/api/login/', {username: userAccount}, function () {
            location.reload()
        })
    } catch (e) {
        console.log(e.message)
    }
}


$('.logout-btn').click(function () {
    wax = new waxjs.WaxJS('https://wax.greymass.com', null, null, false)
    $.get('/api/logout/', function () {
        location.reload()
    })
})

$('.user-info').hover(function () {
    $('.username').toggleClass('menu-active')
    $('.menu').toggleClass('menu-active')
    $('.user-info').toggleClass('menu-active')
    $('.menu').offset({left: $(this).offset().left})
    $('.menu').width($(this).outerWidth())
})

$(window).resize(function () {
    $('.head-bg').height($('.header').height())
    $('.foot-bg').height($('footer').height())
    $('.menu').offset({left: $('.user-info').offset().left})
    $('footer').offset({top: Math.max($(window).height() - $('footer').outerHeight() - 2, $('.wrapper').offset().top + $('.wrapper').outerHeight())})
    $('.foot-bg').offset({top: $('footer').offset().top})
})

function onLoad() {
    $('.head-bg').height($('.header').height())
    $('.foot-bg').height($('footer').height())
    $('footer').offset({top: Math.max($(window).height() - $('footer').outerHeight() - 2, $('.wrapper').offset().top + $('.wrapper').outerHeight())})
    $('.foot-bg').offset({top: $('footer').offset().top})
}

$(onLoad)

$('.logo').click(function () {
    location.assign('/')
})

$(document).ready(function () {
    setInterval(function () {

    }, 1000)
})