$(document).ready(function () {

  function setFieldHeight() {
    var height = $('.bingo-field').width();
    $('.bingo-field').height(height);
  };    
  
  function checkField( field ) {
    var value = $(field).find('.field-is-checked').text();
    
    if (value == 'True') {
      $(field).addClass('bingo-field-done');
    } else {
      $(field).removeClass('bingo-field-done');
    }
  };
  
  var array = ['#field1', '#field2', '#field3', '#field4', '#field5', '#field6', '#field7',
               '#field8', '#field9', '#field10', '#field11', '#field12', '#field13', '#fiel14',
               '#field15', '#field16', '#field17', '#field18', '#field19', '#field20', '#field21',
               '#field22', '#field23', '#field24', '#field25'];
  
  $.each(array, function (index, value) {
    checkField(value);
  });
  
  $('.field-is-checked').hide();
  
  $(window).resize(function () {
    setFieldHeight();
  });
  
  setFieldHeight();
  
});
