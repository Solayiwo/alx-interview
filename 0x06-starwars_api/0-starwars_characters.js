#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Fetch the movie details from the API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error fetching movie data:', err.message);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error(`Failed to fetch movie data. HTTP Status Code: ${res.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Function to fetch and print a character name
  const fetchCharacterName = (url, callback) => {
    request(url, (err, res, body) => {
      if (err) {
        callback(err, null);
        return;
      }
      if (res.statusCode !== 200) {
        callback(new Error(`HTTP Status Code: ${res.statusCode}`), null);
        return;
      }

      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  // Fetch and print all character names in order
  let completedRequests = 0;
  const characterNames = [];

  characterUrls.forEach((url, index) => {
    fetchCharacterName(url, (err, name) => {
      if (err) {
        console.error(`Error fetching character at ${url}:`, err.message);
        process.exit(1);
      }

      characterNames[index] = name;
      completedRequests++;

      // Print names only after all requests are completed
      if (completedRequests === characterUrls.length) {
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
