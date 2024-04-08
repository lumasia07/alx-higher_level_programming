#!/usr/bin/node
const argOne = process.argv[2];
const x = parseInt(argOne);
if (!isNaN(x)) {
  let i;
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
