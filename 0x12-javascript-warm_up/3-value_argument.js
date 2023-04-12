#!/usr/bin/node

const x = process.argv.slice(2);
// console.log(x);
if (typeof x[0] === 'undefined') {
  console.log('No argument');
} else {
  console.log(x[0]);
}
