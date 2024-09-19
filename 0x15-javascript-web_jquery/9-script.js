//This script fetches the translation of "hello" from the API and displays it in DIV#hello.
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
});
