//script fetches and displays the character name from the Star Wars API when the page loads.
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
});
