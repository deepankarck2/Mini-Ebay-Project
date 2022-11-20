function increaseValue() {
    var value = parseInt(document.getElementsByClassName('quan_input')[0].value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementsByClassName('quan_input')[0].value = value;
    console.log(value);
  }
  
function decreaseValue() {
    var value = parseInt(document.getElementsByClassName('quan_input')[0].value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    value--;
    document.getElementsByClassName('quan_input')[0].value = value;
}
