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
                var flipkartHtml = '<div class=\"row\">';
                var amazonHtml = '<div class=\"row\">';


                flipkartHtml1 = flipkart(flipkart_data, flipkartHtml);
                amazonHtml1 = amazon(amazon_data, amazonHtml);
                flipkartHtml = "<h1 class='text-center'> Flipkart </h1>";
                amazonHtml = "<h1 class='text-center'> Amazon </h1>";
                flipkartHtml += flipkartHtml1;
                amazonHtml += amazonHtml1;
                $("#flipkartDiv").html(flipkartHtml);
                $("#amazonDiv").html( amazonHtml);
                $('#body_div').DataTable();
            },

            error: function (xhr) {
                alert("error in searching!!");
            }
        });
        return false;
    });
});



