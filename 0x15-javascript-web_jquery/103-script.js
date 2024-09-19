//script fetches the translation when the user presses Enter or clicks the button.
$('#btn_translate').click(function() {
    fetchTranslation();
});

$('#language_code').keypress(function(e) {
    if (e.which === 13) {
        fetchTranslation();
    }
});

function fetchTranslation() {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
        $('#hello').text(data.hello);
    });
}
