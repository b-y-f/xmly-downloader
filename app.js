const fs = require("fs");
const https = require("https");
const path = require("path");
const process = require("process");

function read_json(p) {
  let rawdata = fs.readFileSync(p);
  return JSON.parse(rawdata);
}

function get_name_and_url(o) {
  let info = o["trackInfo"];
  return [info["title"], info["playPath"]];
}

function getFileExtension(url) {
  const parts = url.split(".");
  return parts[parts.length - 1];
}

async function download_file_async(url, local_path) {
  let directory = path.dirname(local_path);
  if (!fs.existsSync(directory)) {
    fs.mkdirSync(directory, { recursive: true });
  }
  const file = fs.createWriteStream(local_path);
  await new Promise((resolve, reject) => {
    https
      .get(url, function (response) {
        response.pipe(file);
        file.on("finish", function () {
          file.close(resolve);
        });
      })
      .on("error", function (err) {
        fs.unlink(local_path);
        reject(err.message);
      });
  });
}

async function run(bookName, reverse = true) {
  let D = read_json(bookName);
  let data = D["data"];
  if (reverse) {
    data = data.reverse();
  }
  const totalLength = data.length;
  for (let idx = 0; idx < data.length; idx++) {
    let obj = data[idx];
    let [name, url] = get_name_and_url(obj);
    const ext = getFileExtension(url);
    await download_file_async(
      url,
      `${bookName.split(".")[0]}/${idx}_${name}.${ext}`
    );
    console.log(`${idx + 1}/${totalLength}`);
  }
}

let args = process.argv.slice(2);
let bookName = args[0];
let reverse = args.includes("-r");

run(bookName, reverse);
