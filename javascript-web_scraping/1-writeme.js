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
const filePath = process.argv[2];
const texte =  process.argv[3];
fs.writeFileSync(filePath, texte);
