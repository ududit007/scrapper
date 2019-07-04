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
                    flipkartHtml += "<div class=\"border-bottom p-3\" id='flipkartDivOutput'>"
                        + "<a  href='https://www.flipkart.com"+ flipkart_data[i].link_product +"' id=\"flipkart_link\" target=\"_blank\">"
                        + "<h6 id=\"flipkart_name\">" + flipkart_data[i].name + "</h6>"
                        + "<div class='row'><div class='col-sm-3'>"
                        + "<p id=\"flipkart_actual_price\">Actual price: ₹" + flipkart_data[i].actual_price + "</p>"
                        + "<p id=\"flipkart_selling_price\">Selling price: ₹" + flipkart_data[i].selling_price + "</p>"
                        + "<p id=\"flipkart_rating\">Rating: " + flipkart_data[i].rating + "</p>"
                        + "</div> "
                        + "<div class='col-sm-3'>"
                        + "<img width='100%' id=\"flipkart_image\" src='/static/images/flipkart.png'>"
                        + "</div></div>"
                        + "</div> ";
                }
                for (i in amazon_data){
                    amazonHtml += "<div class=\"border-bottom p-3\" id='amazonDivOutput'>"
                        + "<a  href='https://www.amazon.in"+ amazon_data[i].link_product +"' id=\"amazon_link\" target=\"_blank\">"
                        + "<h6 id=\"amazon_name\">" + amazon_data[i].name + "</h6>"
                        + "<div class='row'><div class='col-sm-3'>"
                        + "<p id=\"amazon_actual_price\">Actual Price: ₹" + amazon_data[i].actual_price + "</p>"
                        + "<p id=\"amazon_selling_price\">Selling price: ₹" + amazon_data[i].selling_price + "</p>"
                        + "<p id=\"amazon_rating\">Rating: " + amazon_data[i].rating + "</p>"
                        + "</div> "
                        + "<div class='col-sm-3'>"
                        + "<img width='100%' height='auto' src='" + amazon_data[i].image + "' id=\"amazon_image\"/>"
                        + "</div></div>"
                        + "</div>";


                }


                $("#flipkartDiv1").html(flipkartHtml);
                 $("#flipkartDiv2").html(flipkartHtml);
                $("#amazonDiv1").html( amazonHtml);
                $("#amazonDiv2").html( amazonHtml);
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