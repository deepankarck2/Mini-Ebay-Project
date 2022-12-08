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

});

