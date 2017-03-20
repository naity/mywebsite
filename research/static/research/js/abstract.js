$(document).ready(function() {
    // show more or less of the abstract
    var show_more = "...Show more >>";
    var show_less = "...Show less <<";
    var less_css = {"line-height": "1.4em", "height": "4.2em", "overflow": "hidden"};
    var more_css = {"line-height": "1.4em", "height": "auto"};

    $(".show-more-or-less").click(function(){
        if($(this).hasClass("current-less")) {
            $(this).siblings(".abstract").css(more_css);
            $(this).removeClass("current-less");
            $(this).html(show_less);
        } else {
            $(this).siblings(".abstract").css(less_css);
            $(this).addClass("current-less");
            $(this).html(show_more);
        }
    });

});