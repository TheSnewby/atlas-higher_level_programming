$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status, type) => {
    data.results.forEach(arr => {
      $('UL#list_movies').append(`<li>${arr.title}</li>`);
    });
  });
});
