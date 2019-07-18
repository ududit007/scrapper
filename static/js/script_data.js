function flipkart(flipkart_data, flipkartHtml) {
    for (i in flipkart_data){
        flipkartHtml += "<div class=\"col-sm-6 border-bottom p-1 card bg-transparent\"><div class='flipkartDivOutput p-2'>"
            + "<a  href='https://www.flipkart.com"+ flipkart_data[i].link_product +"' id=\"flipkart_link\" target=\"_blank\">"
            + "<h6 id=\"flipkart_name\">" + flipkart_data[i].name + "</h6>"
            + "<div class='row'><div class='col-sm-6'>"
            + "<p id=\"flipkart_actual_price\">Actual price: ₹" + flipkart_data[i].actual_price + "</p>"
            + "<p id=\"flipkart_selling_price\">Selling price: ₹" + flipkart_data[i].selling_price + "</p>"
            + "<p id=\"flipkart_rating\">Rating: " + flipkart_data[i].rating + "</p>"
            + "</div> "
            + "<div class='col-sm-6'>"
            + "<img width='100%' class='img-fluid' id=\"flipkart_image\" src='/static/images/flipkart.png'>"
            + "</div></div></div>"
            + "</div> ";
        }
        flipkartHtml += "</div>";
    return flipkartHtml;
}
function amazon(amazon_data, amazonHtml){
    for (i in amazon_data){
                    amazonHtml += "<div class=\"col-sm-6 border-bottom p-1 card bg-transparent\"><div class='amazonDivOutput p-2'>"
                        + "<a  href='https://www.amazon.in"+ amazon_data.link_product +"' id=\"amazon_link\" target=\"_blank\">"
                        + "<h6 id=\"amazon_name\">" + amazon_data[i].name + "</h6>"
                        + "<div class='row'><div class='col-sm-6'>"
                        // + "<p id=\"amazon_actual_price\">Actual Price: ₹" + amazon_data[i].actual_price + "</p>"
                        + "<p id=\"amazon_selling_price\">Selling price: ₹" + amazon_data[i].selling_price + "</p>"
                        + "<p id=\"amazon_rating\">Rating: " + amazon_data[i].rating + "</p>"
                        + "</div> "
                        + "<div class='col-sm-6'>"
                        + "<img width='100%' class='img-fluid' height='auto' src='" + amazon_data[i].image + "' id=\"amazon_image\"/>"
                        + "</div></div></div>"
                        + "</div>";
                }
                amazonHtml += "</div>";
                return amazonHtml;
}