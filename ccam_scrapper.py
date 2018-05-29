import re
import urllib
import requests


def get_html_code(url):
    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = str(resp.read())
    return respData


def get_ccam_Free(url):
    print(url)
    html = get_html_code(url)
    reg_expr = re.findall(r'<iframe src="(.*?)"', html)
    ccam = []
    for match in reg_expr:
        html = get_html_code(match)
        print(match)
        reg = re.findall(r'<h1>(.*?)</h1>', html)
        for match in reg:
            ccam.append(match[:-2])
            print(match[:-2])
    return ccam


def export_ccam(ccam):
    with open('CCcam.cfg', 'w', encoding='utf-8') as file:
        for url in ccam:
            file.write(url)


if __name__ == '__main__':
    url = 'http://cccampowerful.com/cccam-free/'
    ccam = get_ccam_Free(url)
    export_ccam(ccam)
