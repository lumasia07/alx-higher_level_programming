#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const argOne = parseInt(process.argv[2]);
const argTwo = parseInt(process.argv[3]);
if (!isNaN(argOne) && !isNaN(argTwo)) {
  console.log(add(argOne, argTwo));
} else {
  console.log('Invalid integers');
}
