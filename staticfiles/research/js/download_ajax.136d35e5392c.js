$(document).ready(function() {
    $('.downloads').click(function(){
        var pubid = $(this).attr("data-pubid");
        $.get('/research/count_downloads/', {publication_id: pubid}, function(data) {
        });
    });
});