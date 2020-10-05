
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

 $('.js--wp-1').waypoint(function(direction){
   $('.js--wp-1').addClass('animate__animated animate__bounceInUp');
 }, {
   offset: '50%'
 });
