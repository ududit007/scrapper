$(document).ready(function(){
        $('#search').on('submit', function(e){
        // alert("fdfd")
        e.preventDefault();
        $.ajax({
            type: 'GET',
            url: '/scrapy/scrap/',
            data: {
                search:$('#search').val(),
                // email:$('#email').val(),
                // password:$('#password').val(),
                // csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(result){
              alert("search successful");
            },
            error: function () {
                alert("error in searching!!")
            }
        });
    });




//     $('#user_login').on('submit', function(e){
//           // alert("fdfd")
//         e.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: '/scrapy/login_user/',
//             data: {
//                 // name:$('#name').val(),
//                 email: $('#email').val(),
//                 password: $('#password').val(),
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             success:function(result) {
//                 location.href="/scrapy/loggedIn/"
//                 alert("Login successfully");
//             }
//         });
//         return false;
//     });
//
// });