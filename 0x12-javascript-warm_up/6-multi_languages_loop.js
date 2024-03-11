#!/usr/bin/node
const arr = { first: 'C is fun', second: 'Python is cool', third: 'JavaScript is amazing' };
let i;
for (i in arr) {
  console.log(arr[i]);
}
