#!/usr/bin/node
const fs = require('fs');
// Get the file path from the command line arguments
const filePath = process.argv[2];
const texte =  process.argv[3];
fs.writeFileSync(filePath, texte);
