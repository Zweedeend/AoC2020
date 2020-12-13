fs = require('fs');


run = (instr) => {
    let ip = 0, acc = 0, seen = new Array();
    while (seen.findIndex(ip) === -1) {
        let line = instr[ip];
        break
    }
    return line
}

solve = async (text) => {
    let lines = text.split("\n");
    return run(lines)
}

fs.promises.readFile("day8.txt", "utf-8").then(solve).then(console.log)
