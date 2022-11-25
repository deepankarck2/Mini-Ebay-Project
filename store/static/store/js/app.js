$(document).ready(function(){

  $('.increaseValue').click(function(e){
    e.preventDefault();
    var val_str = $(this).closest('.product_data').find('.quan_input').val();
    var value = parseInt(val_str, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    $(this).closest('.product_data').find('.quan_input').val(value);
  })

  $('.decreaseValue').click(function(e){
    e.preventDefault();
    var val_str = $(this).closest('.product_data').find('.quan_input').val();
    var value = parseInt(val_str, 10);
    value = isNaN(value) ? 0 : value;
    if(value >= 1){
    value--;
    $(this).closest('.product_data').find('.quan_input').val(value);
    }
  })

  $('#addToCartBtn').click( e => {
    console.log(e);
      e.preventDefault();
      var prod_id = $(e.currentTarget).closest('.product_data').find('.id_prod').val();
      var prod_quantity =  $(e.currentTarget).closest('.product_data').find('.quan_input').val();
      console.log(prod_quantity);

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
  
  $('.changeQuantity').click( e => {
    console.log(e);
      e.preventDefault();
      var prod_id = $(e.currentTarget).closest('.product_data').find('.id_prod').val();
      var prod_quantity =  $(e.currentTarget).closest('.product_data').find('.quan_input').val();
     
      var token = $('input[name=csrfmiddlewaretoken]').val();
      
      $.ajax({
        method : "POST",
        url: "/update-cart",
        data: {
          'product_id' : prod_id,
          'prod_quantity' : prod_quantity,
           csrfmiddlewaretoken : token
        },
        success: (response) =>{
          res = response
            console.log(res);
        }
      })
  })
  $('.delete-cart-item').click(function(e){
    e.preventDefault();
        var prod_id = $(e.currentTarget).closest('.product_data').find('.id_prod').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
          method : "POST",
          url: "/delete-cart-item",
          data: {
            'product_id' : prod_id,
            csrfmiddlewaretoken : token
          },
          success: (response) =>{
            res = response
            console.log(res);
            $('.cartdata').load(location.href + " .cartdata")
          }
    })

  })
});

