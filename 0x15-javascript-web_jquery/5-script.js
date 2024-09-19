// Use jQuery to add a new line element to the list
//when the user clicks on DIV#add_item
$('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
});
