var a = $("#nav").offset().top;

$(document).scroll(function(){
    if($(this).scrollTop() > a)
    {
       $("#nav").css({"background":"white"});
    } else {
       $("#nav").css({"background":"black"});
    }
});
//masonry 
$('.grid').masonry({
  itemSelector: '.grid-item', // use a separate class for itemSelector, other than .col-
  columnWidth: '.grid-sizer',
  percentPosition: true
});
$('.grid').masonry('reloadItems')
