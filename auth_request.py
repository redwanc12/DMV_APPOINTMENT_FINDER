import requests


LINK = "https://www12.honolulu.gov/csdarts/default.aspx"

data = {
    '__EVENTVALIDATION':'/wEWAwKU3IaBCgLV0d+YCwKUxcvrDiqKoMUs7ZCNmsXtEkz+Fhbby933',
    '__VIEWSTATE':'/wEPDwUJNjkzODE5NjE1D2QWAgIBD2QWBAIBD2QWBAIBDxYCHgdWaXNpYmxlaGQCAg8WAh8AaGQCBQ8PFgIeBFRleHQFyQQ8cD48Qj5MT0NBVElPTlM6PC9CPjxicj5DaGVjayBmb3IgYXZhaWxhYmxlIHJvYWQgdGVzdCBkYXRlcyBhbmQgdGltZXMgYXQgdGhlIGZvbGxvd2luZyBkcml2ZXIgbGljZW5zZSBsb2NhdGlvbnMuPHA+PGI+S0FQQUxBTUEgwrcgPC9iPjkyNSBEaWxsaW5naGFtIEJvdWxldmFyZCwgU3VpdGUgIzEwMSwgSG9ub2x1bHUsIEhJIDk2ODE3IMK3ICg4MDgpIDc2OC05MTI3PGJyPjxiPktBUE9MRUkgwrcgPC9iPjEwMDAgVWx1b2hpYSBTdHJlZXQgwrcgKDgwOCkgNzY4LTMxMDA8YnI+PGI+S09PTEFVIMK3IDwvYj40Ny0zODggSHVpIEl3YSBTdHJlZXQgwrcgU3VpdGUgMTkgwrcgKDgwOCkgMjM5LTYzMDE8YnI+PGI+V0FISUFXQSDCtyA8L2I+MzMwIE4uIENhbmUgU3RyZWV0IMK3ICg4MDgpIDc2OC00MDU0PGJyPjxiPldBSUFOQUUgwrcgPC9iPjg1LTY3MCBGYXJyaW5ndG9uIEhpZ2h3YXkgwrcgKDgwOCkgNzY4LTQyMjIgKFR1ZXNkYXkgYW5kIFRodXJzZGF5IG9ubHkpICogIE9mZmljZSBIb3VyczogIDc6NDUgQU0g4oCTIDExOjMwIEFNLCBhbmQgMTI6MzAgUE0g4oCTIDQ6MDAgUE0uICBDbG9zZWQgb24gSG9saWRheXMuPGJyPjwvcD5kZGRDC2zJfPgOTHLkWIoR+1hd92qCcg==',
    '__VIEWSTATEGENERATOR':'881F2DE3',
    'btnAcceptTop':'I have met the eligibility requirements and accept the terms stated below.  Go to scheduling page.'
}

headers = {
    'Origin':'https://www12.honolulu.gov',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

def GetAuthorizedPage():
    page = requests.post(
        LINK,
        data=data,
        headers=headers,
    )
    return page.text


file = open('authTest.html', 'w')
file.write(GetAuthorizedPage())
file.close()