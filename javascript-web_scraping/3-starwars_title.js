#!/usr/bin/node
// Import the built-in 'fs' module for file system operations
const fs = require('fs');
const { stdout } = require('process');

// Check if a file path argument is provided
if (process.argv.length < 3) {
    console.error('Usage: node readFile.js <file-path>');
    process.exit(1);
}

// Get the file path from the command line arguments
const movie = process.argv[2];

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + movie, function (error, response, body) { 
    //console.error('error:', error); // Print the error if one occurred
    //console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    //stringify(body); // Print the HTML for the Google homepage.
    var titles = JSON.parse(body);
    process.stdout.write(titles.title + '\n');
});