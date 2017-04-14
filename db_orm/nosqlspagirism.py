import time
from pymongo import *

# mongodb config
db_name = 'mongo_default'
client = MongoClient("mongodb://localhost:27017")
db = client[db_name]


def timestamp():
    return int(time.time())


def next_id(name):
    query = {
        'name': name,
    }
    update = {
        '$inc': {
            'seq': 1
        }
    }
    kwargs = {
        'query': query,
        'update': update,
        'upsert': True,
        'new': True,
    }
    doc = db['data_id']
    new_id = doc.find_and_modify(**kwargs).get('seq')
    return new_id


class MongoModel(object):
    __fields__ = [
        '_id',
        ('id', int, -1),
        ('type', str, ''),
        ('deleted', bool, False),
        ('created_time', int, 0),
        ('updated_time', int, 0),
    ]

    @classmethod
    def has(cls, **kwargs):
        return cls.find_one(**kwargs) is not None

    def mongos(self, name):
        return db[name].find()

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @classmethod
    def new(cls, form=None, **kwargs):
        name = cls.__name__
        m = cls()
        fields = cls.__fields__.copy()
        fields.remove('_id')
        if form is None:
            form = {}

        for f in fields:
            k, t, v = f
            if k in form:
                setattr(m, k, t(form[k]))
            else:
                setattr(m, k, v)
        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)
            else:
                raise KeyError
        m.id = next_id(name)
        ts = int(time.time())
        m.created_time = ts
        m.updated_time = ts
        m.type = name.lower()
        m.save()
        return m

    @classmethod
    def _new_with_bson(cls, bson):
        m = cls()
        fields = cls.__fields__.copy()
        fields.remove('_id')
        for f in fields:
            k, t, v = f
            if k in bson:
                setattr(m, k, bson[k])
            else:
                setattr(m, k, v)
        setattr(m, '_id', bson['_id'])
        m.type = cls.__name__.lower()
        return m

    @classmethod
    def all(cls):
        return cls.find()

    # TODO, 还应该有一个函数 find(name, **kwargs)
    @classmethod
    def find(cls, **kwargs):
        name = cls.__name__
        kwargs['deleted'] = kwargs.pop('deleted', False)
        flag_sort = '__sort'
        sort = kwargs.pop(flag_sort, None)
        ds = db[name].find(kwargs)
        if sort is not None:
            ds = ds.sort(sort)
        l = [cls._new_with_bson(d) for d in ds]
        return l

    @classmethod
    def find_raw(cls, **kwargs):
        name = cls.__name__
        ds = db[name].find(kwargs)
        l = [d for d in ds]
        return l

    @classmethod
    def _clean_field(cls, source, target):
        ms = cls.find()
        for m in ms:
            v = getattr(m, source)
            setattr(m, target, v)
            m.save()

    @classmethod
    def get(cls, id):
        can = isinstance(id, str) and id.isdigit()
        if can == True:
            id = int(id)
        return cls.find_one(id=id)

    @classmethod
    def find_one(cls, **kwargs):
        # TODO 过滤掉被删除的元素
        # kwargs['deleted'] = False
        l = cls.find(**kwargs)
        if len(l) > 0:
            return l[0]
        else:
            return None

    @classmethod
    def upsert(cls, query_form, update_form, hard=False):
        ms = cls.find_one(**query_form)
        if ms is None:
            query_form.update(**update_form)
            ms = cls.new(query_form)
        else:
            ms.update(update_form, hard=hard)
        return ms

    def update(self, form, hard=False):
        for k, v in form.items():
            if hard or hasattr(self, k):
                setattr(self, k, v)
        self.save()

    def save(self):
        name = self.__class__.__name__
        db[name].save(self.__dict__)

    @classmethod
    def logical_delete(cls, id):
        name = cls.__name__
        query = {
            'id': id,
        }
        values = {
            '$set': {
                'deleted': True,
            },
        }
        db[name].update_one(query, values)

    def delete(self):
        name = self.__class__.__name__
        query = {
            'id': self.id,
        }
        values = {
            '$set': {
                'deleted': True,
            },
        }
        db[name].update_one(query, values)
        # self.deleted = True
        # self.save()

    def blacklist(self):
        b = [
            '_id',
        ]
        return b

    def json(self):
        _dict = self.__dict__
        d = {k: v for k, v in _dict.items() if k not in self.blacklist()}
        return d

    def data_count(self, cls):
        name = cls.__name__
        fk = '{}_id'.format(self.__class__.__name__.lower())
        query = {
            fk: self.id,
        }
        count = db[name].find(query).count()
        return count
