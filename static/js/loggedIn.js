$(document).ready(function() {
    $('#search_form').on('submit', function (e) {
    alert("dd")
        e.preventDefault();
        if($('#search').val()) {
            $.ajax({
                type: 'GET',
                url: '/scrapy/scrap/',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                },
                data: {
                    search: $('#search').val(),
                 },
                success: function (result) {
                    if(result.data_list_flipkart.length === 0 && result.data_list_amazon.length === 0)
                    {
                        alert("no result found")
                    }
                    else{
                            var flipkart_data = result.data_list_flipkart;
                            var amazon_data = result.data_list_amazon;
                            var flipkartHtml = "";
                            var amazonHtml = "";
                           for (i in flipkart_data){
                    flipkartHtml += "<div class=\"border-bottom p-3\">"
                        + "<a  href='https://www.flipkart.com"+ flipkart_data[i].link_product +"' id=\"flipkart_link\">"
                        + "<h3 id=\"flipkart_name\">Name: " + flipkart_data[i].name + "</h3>"
                        + "<div class='row'><div class='col-sm-6'>"
                        + "<p id=\"flipkart_actual_price\">Actual price: " + flipkart_data[i].actual_price + "</p>"
                        + "<p id=\"flipkart_selling_price\">Selling price: " + flipkart_data[i].selling_price + "</p>"
                        + "<p id=\"flipkart_rating\">Rating: " + flipkart_data[i].rating + "</p>"
                        + "</div> "
                        + "<div class='col-sm-6'>"
                        + "<img width='100%' id=\"flipkart_image\" src='/static/images/flipkart.png'>"
                        + "</div></div>"
                        + "</div> ";
                }
                for (i in amazon_data){
                    amazonHtml += "<div class=\"border-bottom p-3\">"
                        + "<a  href='https://www.amazon.in"+ amazon_data[i].link_product +"' id=\"amazon_link\">"
                        + "<h3 id=\"amazon_name\">Name: " + amazon_data[i].name + "</h3>"
                        + "<div class='row'><div class='col-sm-6'>"
                        + "<p id=\"amazon_actual_price\">Actual Price: " + amazon_data[i].actual_price + "</p>"
                        + "<p id=\"amazon_selling_price\">Selling price: " + amazon_data[i].selling_price + "</p>"
                        + "<p id=\"amazon_rating\">Rating: " + amazon_data[i].rating + "</p>"
                        + "<p id=\"amazon_rating\">Link: " + amazon_data[i].link_product + "</p>"
                        + "</div> "
                        + "<div class='col-sm-6'>"
                        + "<img width='100%' src='" + amazon_data[i].image + "' id=\"amazon_image\"/>"
                        + "</div></div>"
                        + "</div>";


                }
                 $("#flipkartDiv").html(flipkartHtml);
                 $("#amazonDiv").html( amazonHtml);
            }
                    },
                    error: function (xhr) {
                        alert("error in searching!!");
                    }
                });

        } else {
            alert("Give proper keyword to search")
        }
        return false;
    });
});