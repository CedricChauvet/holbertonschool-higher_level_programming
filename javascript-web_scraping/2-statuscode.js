#!/usr/bin/node
// Get the file path from the command line arguments
const URL = process.argv[2];

const request = require('request');
request(URL, function (error, response, body) {
  //console.log('Code:', response && response.statusCode); // Print the response status code if a response was received
  process.stdout.write("code: " + Number(response && response.statusCode) + '\n');
});