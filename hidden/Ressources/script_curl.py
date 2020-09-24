import requests
import re
from time import sleep

baseUrl = 'http://192.168.56.101/.hidden/'

def searchCurrentPath(path):
    request = requests.get(baseUrl + path)
    folder = re.findall('href=\"([a-z]*\/)\"', str(request.content))
    readmeReq = requests.get(baseUrl + path + '/README')
    print(baseUrl + path, readmeReq.content)
    if len(folder) > 0:
        for subFolder in folder:
            sleep(0.05)
            searchCurrentPath(path + subFolder)

def main():
    baseReq = requests.get(baseUrl)
    baseFol = re.findall('href=\"([a-z]*\/)\"', str(baseReq.content))
    for folder in baseFol:
        searchCurrentPath(folder)

if __name__ == "__main__":
    main()
