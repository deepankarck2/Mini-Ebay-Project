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

    $('#bidbtn').click( function(e){    
      e.preventDefault();
      var prod_id = $(e.currentTarget).closest('.product_data').find('.id_prod').val();
      var prod_quantity =  $(e.currentTarget).closest('.product_data').find('.quan_input').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();
      var user_bid_amount = $('#user_bid_amount').val();

      $.ajax({
        method : "POST",
        url: "/place-bid",
        data: {
          'product_id' : prod_id,
          'prod_quantity' : prod_quantity,
          'user_bid_amount' : user_bid_amount,
           csrfmiddlewaretoken : token
        },
        success: (response) =>{
            res = response
            console.log(res);
            alertify.success(res.status);
            if(res.reload){
              $(".bid_section").load(location.href + " .bid_section");
            }
        }
      })
    })

  $('#addToCartBtn').click( e => {
      e.preventDefault();
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
  
  $('.changeQuantity').click( e => {
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
            setInterval(()=>{
              location.reload(true);
            }, 200);
          }

    })
    
  })

  //Search
  // $('.ck-box').on('click', function(e){
  //   var selected = [];
  //   let filterobj = {}; 
  //   $('#checkboxes input[type=checkbox]').each(function() {
  //      if ($(this).is(":checked")) {
  //       let add = (obj, key, val) => {
  //         if (key in obj) obj[key] = [].concat(obj[key], val);
  //         else obj[key] = val;
  //       }
  //       console.log(filterobj);
  //       add(filterobj, $(this).attr('name'), $(this).val())        
  //      }
  //   });

  //   $.ajax({
  //     url:'/search1',
  //     data: filterobj,
  //     success: function(res){
  //       //console.log(res.status);
  //     }
  //   })
  // });

  $('#search-submit').click( e => {
    e.preventDefault();
    
    const token = $('input[name=csrfmiddlewaretoken]').val();
    const title = $('#search-title').val().split(",");
    const keyword = $('#search-keyword').val().split(",");
    const min_price = $('#search-min').val();
    const max_price = $('#search-max').val();
    const rating = $('#search-slider').val();

    //console.log(title);
    console.log(keyword);

    $.ajax({
      url: "/search",
      data: {
        'title' : title,
        'keyword' : keyword,
        'min_price' : min_price,
        'max_price' : max_price,
        'rating' : rating,
      },
      success: (response) =>{
        console.log(response.data);
         $("#filteredProducts").html(response.data);
          
      }
    })

})


  $('.buyer_account_options li').click(function() {
    $('.buyer_account_options li.profile_active').removeClass('profile_active');
    $(this).addClass('profile_active');
  });
  
  $('.bid_confirm_btn').click(e =>{
    e.preventDefault()
    var bid_id = $(e.currentTarget).closest('.bid_prod_info').find('.bid_id_num').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
      method : "POST",
      url: "/confirm-bid-sell-prod",
      data: {
        'bid_id' : bid_id,
         csrfmiddlewaretoken : token
      },
      success: (response) =>{
        alertify.success(response.status);
      }
    })
  })

  $('#depBtnSub').click(e => {
    e.preventDefault();
    const deposit_amount = $("#deposit_amount").val()
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
      method : "POST",
      url: "/confirm-deposit-money",
      data: {
        'deposit_amount' : deposit_amount,
         csrfmiddlewaretoken : token
      },
      success: (response) =>{
        alertify.success(response.status);
        setInterval(()=>{
          location.reload(true);
        }, 200);
      }
    })
  })

});

