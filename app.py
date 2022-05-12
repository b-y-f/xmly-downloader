import requests
import urllib.request
from tqdm import tqdm
import csv
import os
from subprocess import check_output
import argparse
import const



def get_total_rows(file_in):
    with open(file_in, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        total = len(list(reader))
    return total


def get_real_url(enc_url):
    real_url = check_output(['node', './decrypt/app.js',enc_url]).decode('UTF-8')
    return real_url

def download(file_in, add_index):
    out_dir=file_in.split('.')[0]

    with open(file_in, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        index= 1
        for row in tqdm(reader, total=get_total_rows(file_in)):
            uid = row[0].split('/')[-1]
            name = row[1].strip()
            res = requests.get(const.get_url(uid), headers=const.headers).json()
            url = res['trackInfo']['playUrlList'][0]['url']
            url = get_real_url(url)
            path = f'./{out_dir}'
            if not os.path.exists(path):
                os.makedirs(path)
            if add_index:
                urllib.request.urlretrieve(url, os.path.join(path, "".join([str(index)," " , name , '.mp4'])) )
            else:
                urllib.request.urlretrieve(url, os.path.join(path, "".join([name , '.mp4'])) )
            index += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store_true', help="toggle if add index for filename")
    parser.add_argument('file_input', type=str, help='file input')
    args = parser.parse_args()
    
    if args.file_input:
        download(args.file_input, args.i)
    else:
        print('Please include parsed csv file.')



