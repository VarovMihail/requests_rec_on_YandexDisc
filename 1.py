import requests
from pprint import pprint

class YaUploader:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        url = f'{self.host}/v1/disk/resources/upload/'
        params = {'path': path_to_file, 'overwrite': True}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        response = requests.get(url, params = params, headers = headers)
        upload_link = response.json()['href']
        print(upload_link)
        response = requests.put(upload_link,data = open('test.jpg', 'rb'))



if __name__ == '__main__':
    path_to_file = '/test.jpg'
    token = '---------------------'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)





