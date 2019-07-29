$(document).ready(function() {
    $('#user_login').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/scrapy/login_user/',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            data: JSON.stringify({
                email: $('#email').val(),
                password: $('#password').val()
            }),
            success: function (result) {
               window.location.replace(result.url);
            },

            error: function (xhr) {
                alert("error in searching!!");
            }
        });
        return false;
    });
});