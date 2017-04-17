$(document).ready(function() {
    $('.like-photo').click(function(){
        var button = $(this);
        var photoid = button.attr("data-photoid");
        var icon = button.children("span").eq(0);
        var likes = button.children("span").eq(1);

        $.get('/photography/like_photo/', {photo_id: photoid}, function(data) {
            // update button color
            button.attr("disabled", "disabled");

            // update the heart icon 
            icon.attr("class", "glyphicon glyphicon-heart");

            // update number of likes
            likes.html(data);
        });
    });
});