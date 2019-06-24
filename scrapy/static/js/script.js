$(document).ready(function(){
        // console.log("hello");
    $('#new_user_form').on('submit', function(e){
          // alert("fdfd")
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/scrapy/signup/',
            data: {
                name:$('#name').val(),
                email:$('#email').val(),
                password:$('#password').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result){
              // alert("Created new user");
            }
        });
    });

    $('#user_login').on('submit', function(e){
          // alert("fdfd")
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/scrapy/login_user/',
            data: {
                // name:$('#name').val(),
                email: $('#email').val(),
                password: $('#password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(result) {
                location.href="/scrapy"
               // alert("Login successfully");
            }
        });
        return false;
        // QJHnBSdaoRu5eSjN50NTidBY1g4H08PlXZAeoohAFpM2jrj523CNCSOBO85poAR1
        // Bt9wOXD6rjO97A76BMDN4RlG78JQiyVKIJ2nBtHwIR66c97oyPsHowyjU0KyG0Xq
    });

});