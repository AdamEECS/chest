from pyquery import PyQuery as PQ
from pprint import pprint

import requests


def parse_html(filename):
    with open(filename, encoding='utf-8') as f:
        html_raw = f.read()
    html = PQ(html_raw)
    data = html.find('#data_list')
    alist = data.find('a')
    url_base = 'http://www.36dm.club/'
    for a in alist:
        if 'show' in a.attrib['href']:
            u = url_base + a.attrib['href']
            # print(u)
            r = requests.get(u)
            # print(r.content)
            sub_html = PQ(r.content.decode('utf-8'))
            sub_a = sub_html.find('#magnet')
            # print(sub_a)
            print(sub_a[0].attrib['href'])
            # break


def main():
    parse_html('dm36.html')


if __name__ == '__main__':
    main()
