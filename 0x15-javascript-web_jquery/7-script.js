const char_id = document.getElementById('character');
fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
	      char_id.textContent = data.name;
	    })
  .catch((err) => console.log(err));
