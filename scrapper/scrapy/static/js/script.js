$(document).ready(function(){
        // console.log("hello");
        $('#new_user_form').on('submit', function(e){
          // alert("fdfd")
          e.preventDefault();
          $.ajax({
            type:'POST',
            url:'/scrapy/signup/',
            data:{
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

      });