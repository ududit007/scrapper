$(document).ready(function() {
    $('#new_user_form').on('submit', function (e) {
        e.preventDefault();
//        $('#loading-image').show();
        $.ajax({
            type: 'POST',
            url: '/scrapy/signup/',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            data: JSON.stringify({
                name: $('#name').val(),
                email: $('#email').val(),
                password: $('#password').val()
            }),
            success: function (result) {
                window.location.replace('/scrapy/login/');
            },

//            complete: function(){
//                 $('#loading-image').hide();
//               }
            error: function (xhr) {
                alert("error in searching!!");
            }
        });
        return false;
    });
});
