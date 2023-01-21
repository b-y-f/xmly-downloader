# xmly(Ximalaya)-downloader

## Requirements

>Node

>Python3

>Instant Data Scraper

## How to use?

This you are outside China, please login and export cookie to terminal env. Like `export XMLY='<your cookie>'`. If you are using Chrome below is how to get cookie.

![cookie](assets/cookie.png)

Download chrome extension [`Instant Data Scraper`](https://chrome.google.com/webstore/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah), get all urls and titles as csv file, Only keep `text href` and `title` column.


1. Just run `make` in command line
2. Put csv file and `app.py` in same folder, run `python3 app.py <parsed file path(xx.csv)>` add flag `-i` to add index for some album.