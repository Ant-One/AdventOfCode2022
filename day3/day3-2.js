const fs = require('fs');
const readline = require('node:readline');

let sum = 0;
let counter = 0;

let first = "";
let second = "";
let third = "";

const lowerCase = "abcdefghijklmnopqrstuvwxyz";
const upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const readInterface = readline.createInterface({
  input: fs.createReadStream('input'),
  console: false
});

readInterface.on('line', function(line) {

  if(counter % 3 == 0){
    first = line;
    counter++;
  }
  else if (counter % 3 == 1){
    second = line;
    counter++;
  }
  else{
    third = line;
    counter++;

    console.log("Comparing " + first + " " + second + " " + third);
    let intersection = new Set([...first].filter(x => second.includes(x)).filter(y => third.includes(y)));

    sum += priority(Array.from(intersection).join(""))


    console.log(intersection);
  }
  
  
  
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