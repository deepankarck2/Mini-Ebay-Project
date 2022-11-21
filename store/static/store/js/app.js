$(document).ready(function(){
  $('#addToCartBtn').click( e => {
      e.preventDefault();
      document.getElementsByClassName('quan_input')[0].value = 0; 
      var prod_id = $(e.currentTarget).closest('.product_data').find('.id_prod').val();
      var prod_quantity =  $(e.currentTarget).closest('.product_data').find('.quan_input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();
      
      $.ajax({
        method : "POST",
        url: "/add-to-cart",
        data: {
          'product_id' : prod_id,
          'prod_quantity' : prod_quantity,
           csrfmiddlewaretoken : token
        },
        success: (response) =>{
          res = response
            console.log(res);
            alertify.success(res.status);
        }
      })
  })
});

function increaseValue() {
    var value = parseInt(document.getElementsByClassName('quan_input')[0].value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementsByClassName('quan_input')[0].value = value;
}
  
function decreaseValue() {
    var value = parseInt(document.getElementsByClassName('quan_input')[0].value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    value--;
    document.getElementsByClassName('quan_input')[0].value = value;
}
