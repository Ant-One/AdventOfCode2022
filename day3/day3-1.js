const fs = require('fs');
const readline = require('node:readline');

sum = 0;

const lowerCase = "abcdefghijklmnopqrstuvwxyz";
const upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const readInterface = readline.createInterface({
  input: fs.createReadStream('input'),
  output: process.stdout,
  console: false
});

readInterface.on('line', function(line) {
  let size = line.length/2;
  let first = line.slice(0, size);
  let second = line.slice(size);
  
  let intersection = new Set([...first].filter(x => second.includes(x)));

  sum += priority(Array.from(intersection).join(""))


  console.log(intersection);
  
});

readInterface.on('close', function(line) {
  console.log("\nFINISHED WITH SUM = " + sum);
  
});

function priority(arg){

  if (lowerCase.includes(arg)){
    return lowerCase.indexOf(arg) + 1;
  }
  else if (upperCase.includes(arg)){
    return upperCase.indexOf(arg) + 27;
  }
  else{
    console.log("Something's wrong... String not found")
  }
}