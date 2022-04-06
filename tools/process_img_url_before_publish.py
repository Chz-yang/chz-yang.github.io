import os
import sys

def get_all_process_file_paths():
    process_file_paths = ['config.toml']
    for file_path, _, file_names in os.walk('content'):
        for file_name in file_names:
            process_file_paths.append('%s\\%s' % (file_path, file_name))
    return process_file_paths

def process_file_img_url(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()

        content = content.replace('= "/images/', '= "https://cdn.jsdelivr.net/gh/Chz-yang/GitHubPageImages/')
        content = content.replace('](/images/', '](https://cdn.jsdelivr.net/gh/Chz-yang/GitHubPageImages/')
        content = content.replace('img="/images/', '= "img="https://cdn.jsdelivr.net/gh/Chz-yang/GitHubPageImages/')

        with open(file_path, 'w', encoding='UTF-8') as file:
            file.write(content)

if __name__ == '__main__':
    list(map(process_file_img_url, get_all_process_file_paths()))
