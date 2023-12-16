# xmly(Ximalaya)-downloader

## Requirements

- Node.js

## How to use

1. open any one of the audio.

1. find the __first track of the album__ link like below ![Alt text](image.png)

1. right click and copy cURL

```bash
https://www.ximalaya.com/m-revision/page/track/queryRelativeTracksById?trackId=<id>&preOffset=1&nextOffset=<total_audio_num>&countKeys=play&order=2
```

1. modify url's `preOffset` parameter to the index of audio in album. `nextOffset` means load how many audios.

1. open `terminal`, paste and add `> xxx.json`

1. run `node app.js <xxx.json>`
