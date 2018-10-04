import requests
from bs4 import BeautifulSoup
import json
from declare import HEADERS as headers

page_count = 0
files_link = "https://mbasic.facebook.com/groups/454202081452200?view=files&p={}"
res = requests.get(files_link.format(0), headers=headers)


def numberOfFiles(content):
    soup = BeautifulSoup(content, 'lxml')
    file_count = soup.find(
        'div', id='objects_container').findAll('span')[-1].text
    print(file_count)
    return (int(file_count)//10)*10


def getFiles(page_link, page_num):
    print(page_num)
    res = requests.get(page_link, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    files_list = soup.find('div', id="root").find('div').findAll('a')
    for file in files_list:
        file_name = file.text.replace('_', ' ').replace('-',' ')
        print(file_name, file['href'])
        files_detials['https://www.facebook.com' + file['href']] = file_name

if __name__ == "__main__":
    page_count = numberOfFiles(res.content)
    print(page_count)
    files_detials = dict()
    for num in range(0, page_count+10, 10):
        getFiles(files_link.format(num), num)
    with open("files.json", 'w') as f:
        json.dump(files_detials, f)
