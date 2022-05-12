var CryptoJS = require("crypto-js");

const PASSPARSE = "aaad3e4fd540b0f79dca95606e72bf93"

function getUrl(encUrl) {
    var Dt = CryptoJS
    return Dt.AES.decrypt({
        ciphertext: Dt.enc.Base64url.parse(encUrl)
    }, Dt.enc.Hex.parse(PASSPARSE), {
        mode: Dt.mode.ECB,
        padding: Dt.pad.Pkcs7
    }).toString(Dt.enc.Utf8)
}

process.stdout.write(getUrl(process.argv[2]))
