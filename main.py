import requests
import json
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from lxml import html
import lxml

__author__ = '3000'
'''
账号：18640346924
密码：6bnbgatn
'''
app = Flask(__name__)
db_path = 'weibo.sqlite'
db = SQLAlchemy()
manager = Manager(app)


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


def timestamp():
    return int(time.time())


class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = ({1})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{0}:\n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()


class Person(db.Model, Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    sex = db.Column(db.Text)
    follow = db.Column(db.Integer)
    fans = db.Column(db.Integer)
    weibos = db.Column(db.Integer)
    add = db.Column(db.Text)
    created_time = db.Column(db.Integer, default=0)

    def __init__(self):
        self.id = -1
        self.name = ''
        self.sex = ''
        self.follow = -1
        self.fans = -1
        self.weibos = -1
        self.add = -1
        self.created_time = timestamp()

    def insert(self):
        person_in_db = Person.query.get(self.id)
        if person_in_db is None:
            self.save()
        else:
            person_in_db.update(new=self)
            person_in_db.save()

    def update(self, new):
        self.name = new.name
        self.sex = new.sex
        self.follow = new.follow
        self.fans = new.fans
        self.weibos = new.weibos
        self.add = new.add
        self.created_time = new.created_time


def person_from_li(div):
    person = Person()
    data = div.xpath('./@action-data')[0]
    data = data.split('&')
    dic = {i.split('=')[0]: i.split('=')[1] for i in data}
    person.id = int(dic.get('uid', -1))
    person.name = dic.get('fnick', '')
    person.sex = dic.get('sex', '')
    person.follow = int(div.xpath('.//div[@class="info_connect"]/span/em/a')[0].text)
    person.fans = int(div.xpath('.//div[@class="info_connect"]/span/em/a')[1].text)
    person.weibos = int(div.xpath('.//div[@class="info_connect"]/span/em/a')[2].text)
    person.add = div.xpath('.//div[@class="info_add"]/span')[0].text
    person.insert()
    return person


def divs_from_url(url, headers):
    r = requests.get(url, headers=headers)
    r = r.content.decode()
    # print(r)
    r = r.split('<script>parent.FM.view(')[1]
    r = r.split(')</script>')[0]
    dict_r = json.loads(r)
    r = dict_r.get('html')
    # print(r)
    try:
        root = html.fromstring(r)
        person_divs = root.xpath('//li[@class="follow_item S_line2"]')
        persons = [person_from_li(div) for div in person_divs]
        print(len(persons))
    except lxml.etree.XMLSyntaxError:
        print(r)
        with open('log.html', 'w', encoding='utf-8') as f:
            f.write(r)


def requests_with_headers(url):
    headers = {
        'Cookie': 'login_sid_t=8863b2ce370ad171f82d294b4464be3d; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; YF-V5-G0=d8809959b4934ec568534d2b6c204def; _s_tentry=www.google.com; Apache=2912496465019.687.1482808897562; SINAGLOBAL=2912496465019.687.1482808897562; ULV=1482808897602:1:1:1:2912496465019.687.1482808897562:; YF-Page-G0=bf52586d49155798180a63302f873b5e; WB_register_version=783d99334509299a; __gads=ID=e21cf0c1e50c0ee6:T=1482809021:S=ALNI_MYa_Eju0e69mKOBKVpe6_KF1h8xcA; appkey=; SSOLoginState=1482818565; WBtopGlobal_register_version=783d99334509299a; UOR=www.google.com,weibo.com,www.liaoxuefeng.com; WBStorage=c9869827d4fcf310|undefined; SCF=ArvpvuL1UzXaXmqv9Jj-NVWkl9xWv6WPLvdxFQpVyTElvsn3SRbqfcw0dQ9TcgAmv_DKy844xBQ6bBin2SlcrbA.; SUB=_2A251Zws6DeRxGeBO41EU8i7NzDSIHXVWFXvyrDV8PUNbmtANLUH7kW9uD9MTEuOVZbhhvllthIcJ56bzYQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFy3IlWAegLYa3r132kHbij5JpX5K2hUgL.Foq71hefeo5pS0n2dJLoIEBLxKML1K5L1-zLxKBLB.2LBKMLxKBLBonL1hMLxK-L1hqL1-zt; SUHB=0wnFQyr6U29BIK; ALF=1514450665; un=18640346924',
        'Host': 'weibo.com',
        'Upgrade - Insecure - Requests': '1',
        'Referer': 'http://weibo.com/drwujun?refer_flag=1001030201_&is_hot=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    divs_from_url(url, headers)


@manager.command
def main():
    print('crawler run')
    pages = 4
    url = 'http://weibo.com/p/1035052887339314/follow?pids=Pl_Official_HisRelation__61&relate=fans&page={}&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fp%2F1035052887339314%2Ffollow%3Frelate%3Dfans%26from%3D103505%26wvr%3D6%26mod%3Dheadfans%26current%3Dfans%23place&_t=FM_148282001854539'.format(pages)
    requests_with_headers(url)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
    main()
