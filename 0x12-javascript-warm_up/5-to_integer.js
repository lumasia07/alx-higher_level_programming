#!/usr/bin/node
const argOne = process.argv[2];
const args = parseInt(argOne);
if (!isNaN(args)) {
  console.log(`My number: ${args}`);
} else {
  console.log('Not a number');
}
