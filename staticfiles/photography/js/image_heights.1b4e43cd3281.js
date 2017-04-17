// use $(window).on("load", function(){} to make sure all images are loaded first
$(window).on("load", function(){
	var heights = $(".dynamic-heights").map(function() {
        return $(this).height();
    }).get();

    minHeight = Math.min.apply(100, heights);

    $(".dynamic-heights").height(minHeight);
});