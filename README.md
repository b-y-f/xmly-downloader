# xmly(Ximalaya)-downloader

## Requirements

>Node

>Python3

>Instant Data Scraper

## How to use?

Download chrome extension [`Instant Data Scraper`](https://chrome.google.com/webstore/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah), get all urls and titles as csv file, Only keep `text href` and `title` column.


1. Install node packages by: Go to folder `decrypt/` and run `npm install` or `npm i`.
2. Install python packages by: run `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt`.
3. Put csv file and `app.py` in same folder, run `python3 app.py <parsed file path(xx.csv)>` add flag `-i` to add index for some album.