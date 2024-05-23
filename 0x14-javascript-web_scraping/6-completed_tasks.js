#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
  console.log(completedTasks);
});
