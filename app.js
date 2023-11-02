const fs = require('fs');
const https = require('https');
const path = require('path');
const process = require('process');



function read_json(p) {
    let rawdata = fs.readFileSync(p);
    return JSON.parse(rawdata);
}

function get_name_and_url(o) {
    let info = o["trackInfo"];
    return [info["title"], info["playPath"]];
}

function download_file(url, local_path) {
    let directory = path.dirname(local_path);
    if (!fs.existsSync(directory)){
        fs.mkdirSync(directory, { recursive: true });
    }
    const file = fs.createWriteStream(local_path);
    https.get(url, function(response) {
        response.pipe(file);
    });
}

function run(bookName, reverse=true) {
    let D = read_json(bookName);
    let data = D["data"];
    if (reverse) {
        data = data.reverse();
    }
    for (let idx = 0; idx < data.length; idx++) {
        let obj = data[idx];
        let [name, url] = get_name_and_url(obj);
        download_file(url, `${bookName.split(".")[0]}/${idx}_${name}.mp4`);
    }
}

let args = process.argv.slice(2);
let bookName = args[0];
let reverse = args.includes("-r");

run(bookName, reverse);
