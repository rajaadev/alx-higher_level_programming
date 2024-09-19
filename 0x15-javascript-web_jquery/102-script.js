//This script fetches and displays the translation of "Hello" based on the user input.
$('#btn_translate').click(function() {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
        $('#hello').text(data.hello);
    });
});
