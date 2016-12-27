import requests
import json
from lxml import html

__author__ = '3000'
'''
账号：18640346924
密码：6bnbgatn
Request URL:
http://weibo.com/p/1035052887339314/follow?
relate=fans
&from=103505
&wvr=6
&mod=headfans
&current=fans
&ajaxpagelet=1
&ajaxpagelet_v6=1
&__ref=%2Fdrwujun%3Frefer_flag%3D1001030201_%26is_hot%3D1
&_t=FM_148282001854531

__ref:/drwujun?refer_flag=1001030201_&is_hot=1
'''


class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = ({1})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{0}:\n  {1}\n>'.format(class_name, '\n  '.join(properties))


class Movie(Model):
    def __init__(self):
        super(Movie, self).__init__()
        self.name = ''
        self.score = 0
        self.quote = ''


class Topic(Model):
    def __init__(self):
        self.id = -1
        self.name = ''


class Content(Model):
    def __init__(self):
        self.name = ''
        self.content = ''


def movie_from_div(div):
    movie = Movie()
    movie.name = div.xpath('.//span[@class="title"]')[0].text
    movie.score = div.xpath('.//span[@class="rating_num"]')[0].text
    movie.quote = div.xpath('.//span[@class="inq"]')[0].text
    return movie


def movies_from_url(url):
    page = requests.get(url)
    root = html.fromstring(page.content)
    movie_divs = root.xpath('//div[@class="item"]')
    movies = [movie_from_div(div) for div in movie_divs]
    return movies


def topics_from_url(url):
    headers = {
        'Cookie': 'login_sid_t=8863b2ce370ad171f82d294b4464be3d; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; YF-V5-G0=d8809959b4934ec568534d2b6c204def; _s_tentry=www.google.com; UOR=www.google.com,weibo.com,www.google.com; Apache=2912496465019.687.1482808897562; SINAGLOBAL=2912496465019.687.1482808897562; ULV=1482808897602:1:1:1:2912496465019.687.1482808897562:; YF-Page-G0=bf52586d49155798180a63302f873b5e; WB_register_version=783d99334509299a; __gads=ID=e21cf0c1e50c0ee6:T=1482809021:S=ALNI_MYa_Eju0e69mKOBKVpe6_KF1h8xcA; appkey=; SCF=ArvpvuL1UzXaXmqv9Jj-NVWkl9xWv6WPLvdxFQpVyTElrXHyCYHm0OloPpiGMpESVBAsrr7CaQd06YpNqoT1OSk.; SUB=_2A251ZnRVDeRxGeBO41EU8i7NzDSIHXVWEuKdrDV8PUJbmtANLU3ukW9TFKkmXQPrQHsfkMSvTymgsKDIBw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFy3IlWAegLYa3r132kHbij5JpX5K2hUgL.Foq71hefeo5pS0n2dJLoIEBLxKML1K5L1-zLxKBLB.2LBKMLxKBLBonL1hMLxK-L1hqL1-zt; SUHB=0idbryljp2aCHI; SSOLoginState=1482818565; un=18640346924; wvr=6; WBtopGlobal_register_version=783d99334509299a',
        'Host': 'weibo.com',
        'Upgrade - Insecure - Requests': '1',
        'Referer': 'http://weibo.com/drwujun?refer_flag=1001030201_&is_hot=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    '''
    Host: weibo.com
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Referer: http://weibo.com/drwujun?refer_flag=1001030201_&is_hot=1
    Accept-Encoding: gzip, deflate, sdch
    Accept-Language: zh-CN,zh;q=0.8
    Cookie: login_sid_t=8863b2ce370ad171f82d294b4464be3d; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; YF-V5-G0=d8809959b4934ec568534d2b6c204def; _s_tentry=www.google.com; UOR=www.google.com,weibo.com,www.google.com; Apache=2912496465019.687.1482808897562; SINAGLOBAL=2912496465019.687.1482808897562; ULV=1482808897602:1:1:1:2912496465019.687.1482808897562:; YF-Page-G0=bf52586d49155798180a63302f873b5e; WB_register_version=783d99334509299a; __gads=ID=e21cf0c1e50c0ee6:T=1482809021:S=ALNI_MYa_Eju0e69mKOBKVpe6_KF1h8xcA; appkey=; SCF=ArvpvuL1UzXaXmqv9Jj-NVWkl9xWv6WPLvdxFQpVyTElrXHyCYHm0OloPpiGMpESVBAsrr7CaQd06YpNqoT1OSk.; SUB=_2A251ZnRVDeRxGeBO41EU8i7NzDSIHXVWEuKdrDV8PUJbmtANLU3ukW9TFKkmXQPrQHsfkMSvTymgsKDIBw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFy3IlWAegLYa3r132kHbij5JpX5K2hUgL.Foq71hefeo5pS0n2dJLoIEBLxKML1K5L1-zLxKBLB.2LBKMLxKBLBonL1hMLxK-L1hqL1-zt; SUHB=0idbryljp2aCHI; SSOLoginState=1482818565; un=18640346924; wvr=6; WBtopGlobal_register_version=783d99334509299a
    '''
    # data = {
    #     '_xsrf': '23562d03a0e521d8099d556a696e77dc',
    # }
    page = requests.get(url, headers=headers)
    print(page.encoding)
    print(page.text)
    return
    # dict = page.json()
    # print(dict['msg'][0])
    # print(dict['msg'][1])
    # return
    # for i in dict['msg'][1]:
    #     # print(i)
    #     print('topic='+i[0][1], 'id='+i[0][2])
    # return dict
    # root = html.fromstring(page.content)
    # return root
    # movie_divs = root.xpath('//div[@class="item"]')
    # topics = [movie_from_div(div) for div in movie_divs]
    # return topics


def main():
    url = 'http://weibo.com/p/1035052887339314/follow?pids=Pl_Official_HisRelation__61&relate=fans&page=2&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fp%2F1035052887339314%2Ffollow%3Frelate%3Dfans%26from%3D103505%26wvr%3D6%26mod%3Dheadfans%26current%3Dfans%23place&_t=FM_148282001854539'
    topics = topics_from_url(url)
    print(topics)


if __name__ == '__main__':
    main()
