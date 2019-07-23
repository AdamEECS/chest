from pyquery import PyQuery as PQ
from pprint import pprint


def parse_html(filename, download='磁力'):
    with open(filename, encoding='utf-8') as f:
        html_raw = f.read()
    html = PQ(html_raw)
    alist = html.find('a')
    for a in alist:
        if download in PQ(a).text():
            print(a.attrib['href'])


def main():
    parse_html('zimuxia.html', download='电驴')


if __name__ == '__main__':
    main()
