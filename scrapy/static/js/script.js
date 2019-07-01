$(document).ready(function() {
    $('#example').on('submit', function (e) {

        e.preventDefault();
        $.ajax({
            type: 'GET',
            url: '/scrapy/scrap/',
            data: {
                search: $('#search').val()
            },
            success: function (result) {
                var json_data = $.parseJSON(result)
                flipkart_data = json_data.flipkart;
                amazon_data = json_data.amazon;
                var flipkartHtml = "";
                var amazonHtml = "";
                for (i in flipkart_data){
                    flipkartHtml += "<div class=\"border-bottom\">"
                        + "<h3 id=\"flipkart_name\">" + flipkart_data[i].name + "</h3>"
                        + "<p id=\"flipkart_actual_price\">" + flipkart_data[i].actual_price + "</p>"
                        + "<p id=\"flipkart_selling_price\">" + flipkart_data[i].selling_price + "</p>"
                        + "<p id=\"flipkart_rating\">" + flipkart_data[i].rating + "</p>"
                        + "<p id=\"flipkart_image\">" + flipkart_data[i].image + "</p>"
                        + "</div> ";
                }
                for (i in amazon_data){
                    amazonHtml += "<div class=\"border-bottom\">"
                        + "<h3 id=\"amazon_name\">" + amazon_data[i].name + "</h3>"
                        + "<p id=\"amazon_actual_price\">" + amazon_data[i].actual_price + "</p>"
                        + "<p id=\"amazon_selling_price\">" + amazon_data[i].selling_price + "</p>"
                        + "<p id=\"amazon_rating\">" + amazon_data[i].rating + "</p>"
                        + "<p id=\"amazon_image\">" + amazon_data[i].image + "</p>"
                        + "</div> ";
                }


                $("#flipkartDiv").html(flipkartHtml);
                $("#amazonDiv").html( amazonHtml);
            },
            error: function (xhr) {
                alert("error in searching!!");
            }
        });
        return false;
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