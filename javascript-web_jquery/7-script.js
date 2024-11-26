$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, status, type) => {
    $('DIV#character').append(data.name);
  });
});
