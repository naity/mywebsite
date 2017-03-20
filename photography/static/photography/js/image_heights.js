$( document ).ready(function() {
    var heights = $(".dynamic-heights").map(function() {
        return $(this).height();
    }).get(),

    minHeight = Math.min.apply(null, heights);

    $(".dynamic-heights").height(minHeight);
});