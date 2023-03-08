const fs = require('fs');
const readline = require('node:readline');

const range = (start, stop) => Array(stop-start + 1).fill(0).map((_, index) => index + start);

let sum = 0;
let tmp = 0;

const readInterface = readline.createInterface({
  input: fs.createReadStream('input'),
  console: false
});

readInterface.on('line', function(line) {
    let splitted = line.split(",");
    first_array = splitted[0].split("-");
    second_array = splitted[1].split("-"); 
    
    const first = range(parseInt(first_array[0]), parseInt(first_array[1]));
    const second = range(parseInt(second_array[0]), parseInt(second_array[1]));

    let set1 = new Set([...first].filter(x => !second.includes(x)));
    let set2 = new Set([...second].filter(x => !first.includes(x)));

    if (set1.size == 0 || set2.size == 0){
        sum++;
    }
});

readInterface.on('close', function(line) {
  console.log("FINISHED : " + sum + " overlapping entries");
});
