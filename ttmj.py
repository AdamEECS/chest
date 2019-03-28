from pyquery import PyQuery as PQ
from pprint import pprint


def parse_html(filename, pixel='720', sub='', download='magnet'):
    with open(filename, encoding='utf-8') as f:
        html_raw = f.read()
    html = PQ(html_raw)
    tr_all = html.find('#seedlist').find('tr')
    tr_selected = []
    a_selected = []
    for tr in tr_all:
        tr = PQ(tr)
        title = PQ(tr.find('a')[0]).text()
        if pixel in title and sub.lower() in title.lower():
            tr_selected.append(title)
            for a in tr.find('a'):
                href = a.attrib['href']
                if download in href:
                    a_selected.append(href)
                    break
    print('total:', len(tr_selected), 'find:', len(a_selected))
    # pprint(tr_selected)
    print('\n'.join(a_selected))


def main():
    parse_html('ttmj.html', pixel='720', sub='官方', download='magnet')


if __name__ == '__main__':
    main()
