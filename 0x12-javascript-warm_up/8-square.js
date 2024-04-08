#!/usr/bin/node
const argOne = process.argv[2];
const x = parseInt(argOne);

if (!isNaN(x))
{
	let i, j;

	for (i = 0; i < x; i++)
	{
		let line = "";

		for (j = 0; j < x; j++)
		{
			line += "X";
		}
		console.log(line);
	}
}
else
{
	console.log("Missing size");
}
