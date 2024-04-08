#!/usr/bin/node
const args = process.argv.slice(2);
const i = args.map(x => parseInt(x)).filter(x => !isNaN(x));

i.sort((a, b) => b - a);

if (i.length < 2) {
  console.log(0);
} else {
  console.log(i[1]);
}
