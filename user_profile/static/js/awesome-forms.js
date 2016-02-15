$(function(){

  $('.awesome-form .label-group input').focusout(function(){
    var text_value = $(this).val();

    if(text_value === ""){
      $(this).removeClass('has-value');
    }else{
      $(this).addClass('has-value');
    }

  });

});
