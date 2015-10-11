$(document).ready(function () {

  function setFieldHeight() {
    var height = $('.bingo-field').width();
    $('.bingo-field').height(height);
  };    
    
  $(window).resize(function () {
    setFieldHeight();
  });
  
  setFieldHeight();
  
});
