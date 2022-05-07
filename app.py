import requests
import urllib.request
import csv
import os
import sys
from tqdm import tqdm



def get_url(id): return f"https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1"


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-gpc': '1',
    'xm-sign': '24393343084be486d4ce4228bc83f4a8(92)0(21)1650440097876',
}

def download(file_in):
    out_dir=file_in.split('.')[0]
    with open(file_in, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in tqdm(reader):
            uid = row[0].split('/')[-1]
            name = row[1].strip()
            res = requests.get(get_url(uid), headers=headers).json()
            url = res['data']['src']
            path = f'./{out_dir}'
            if not os.path.exists(path):
                os.makedirs(path)
            urllib.request.urlretrieve(url, os.path.join(path,name+'.mp4') )


if __name__ == "__main__":
    if len(sys.argv)>1:
        download(sys.argv[1])
    else:
        print('Please include parsed csv file.')



