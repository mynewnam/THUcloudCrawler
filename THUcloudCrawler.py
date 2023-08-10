import requests
import json
import urllib.request
import os
import argparse
import re

def args_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, required=True, help='url to crawl')
    return parser.parse_args()

def get_id(url: str) -> str:
    pattern = re.compile('/d/([a-z0-9\-]+)/')
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        print('Error: invalid url')
        exit(1)

def file_download(repo_url: str, file_path_list: list): 
    # Download file
    file_download_url = repo_url + "files"

    # 加入param{"dl": 1}可以直接下载
    for path in file_path_list:
        params = {"p": path, "dl": 1}
        r = requests.get(file_download_url, params=params)
        file_url = r.url
        print(file_url)
        file_name = path.split("/")[-1]
        print("Downloading", file_name, "...")
        urllib.request.urlretrieve(file_url, file_name)

# Download directory
def dir_download(repo_url: str, path: str, url: str):
    params = {
        "thumbnail_size": "48",
        "path": path,
    }
    response = requests.get(url, params=params)
    response_items = json.loads(response.text)['dirent_list']
    dir_path_list = []
    file_path_list = []
    for item in response_items:
        if item['is_dir']:
            dir_path_list.append(item['folder_path'])
        else:
            file_path_list.append(item['file_path'])
    file_download(repo_url=repo_url, file_path_list=file_path_list)

    while len(dir_path_list) > 0:
        dir_path = dir_path_list.pop()
        # Create directory
        if not os.path.exists(dir_path.split('/')[-2]):
            os.makedirs(dir_path.split('/')[-2])
        # Change directory
        os.chdir(dir_path.split('/')[-2])
        dir_download(repo_url=repo_url, path=dir_path, url=url)
    if os.path.basename(os.getcwd()) != current_dir:
        os.chdir('..')
        return

if __name__ == "__main__":
    args = args_parse()

    current_dir = os.path.basename(os.getcwd())
    repo_url = args.url
    id = get_id(repo_url)
    url = f"https://cloud.tsinghua.edu.cn/api/v2.1/share-links/{id}/dirents"

    dir_download(repo_url, '/', url)


