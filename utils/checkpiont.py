

==========================================
# 高级知识
==========================================



## Python
* Python中的元类(metaclass)
* 用共享属性实现单例模式
* GIL 线程全局锁
* 协程
* 闭包



## 操作系统
* select,poll和epoll
* 静态链接和动态链接
* 虚拟内存技术
* 页面置换算法
* 边沿触发和水平触发
* *nix进程间通信方式(IPC) (管道，信号)



## 数据库
* Redis原理
* MVCC
* MyISAM和InnoDB



## 网络
* 四次挥手
* c10k问题
* SOAP
* RPC
* CGI和WSGI



## 算法编程











==========================================
# 中级知识
==========================================



## Python

* Python函数式编程 filter map zip reduce
    ``` python


    ```
* 迭代器和生成器
* 面向切面编程AOP和装饰器 (wrap)
* 用装饰器实现单例模式
* 鸭子类型
* Python中单下划线和双下划线
* 字符串格式化: format()
* 新式类和旧式类
* Python里的拷贝 (copy deepcopy)
* Python垃圾回收机制
    *引用计数
    * 2 标记-清除机制
    * 3 分代技术

* Python的List
* Python2和3的区别
* super.__init__()




## 操作系统
* 调度算法
* 死锁
* 程序编译与链接
    *预处理
    * 2 编译
    * 3 汇编
    * 4 链接
* 分页和分段
    * 分页与分段的主要区别



## 数据库
* 事务
* 数据库索引
* 乐观锁和悲观锁




## 网络
* 三次握手
* ARP协议
* urllib和urllib2的区别
* Post和Get
* Cookie和Session
* apache和nginx的区别
* 网站用户密码保存
* HTTP和HTTPS (ssl , 非对称加密握手，对称加密传输)
* XSRF和XSS
    * CSRF(Cross-site request forgery)跨站请求伪造
    * XSS(Cross Site Scripting)跨站脚本攻击
    CSRF重点在请求,XSS重点在脚本
* 幂等 Idempotence
* RESTful架构(SOAP,RPC)
* 中间人攻击
* socket
* 浏览器缓存
* HTTP1.0和HTTP1.1
* Ajax



## 算法编程



==========================================
# 基础知识
==========================================



## Python
* 用import 文件的方法实现单例模式
    ``` python
    #1.初始化 models.py
        Class Model():
        model = Model()
    #2. 引用
        from models import model
    ```

* lambda 函数
    ```python
      # 匿名函数 一句
      # python3 ,  返回迭代器
    ```

* Python的函数参数传递
    ```python
    # 1. 只检查参数个数
    # 2. 不检查参数类型
    # 3. 如果传入的是 list, dict 等, 如果在函数内改变，函数外也会改变；如果传入的是 字符串，数字，布尔型，就不会。
    ```

* *args and **kwargs
    ```python
      # 用于传递 不确定个数的参数
      # args 是tuple元组(,)， 按顺序解包参数
      # kwargs 是 dict字典 {}
      def func(*args, **kwargs):
          pass
    ```
* 字典推导式
    ```python
    ```

* 类变量和实例变量  （注意 []{}）
    ```python
      # 实例变量的默认值是类变量的默认值，但不同的实例变量有各自的命名空间
      # 注意 如果类变量的默认值是 数组或字典，改值时并不改变它的引用地址，所以会一起改变

    ```

* @staticmethod和@classmethod
    ```python
    # 类的静态方法，staticmethod ,类仅仅提供了一个命名空间, 和把函数放到.py文件里引用是一样的
    # 类的类方法，@classmethod ，默认提供了一个可以引用类变量和（其他）类函数的 cls 的参数
    ```

* Python的is 和 ==
    ```python
    # is 比较地址 type(None) <class 'NoneType'>
    # == 比较值
    ```
* file 文件 read,readline和readlines
    ```python
    file.read(n)      # 读取所有, n 默认为所有，否则指前几位
    file.readline(n)  # 读取一行，n 默认为所有，否则指前几位 , 超出不管
    file.readlines()  # 读取所有行
    # 值得注意是，读取是从文件指针开始的，所以注意用 f.seek(0)
    ```
* range-and-xrange
    ```python
    # python3 只有 range
    # python2 range 返回队列， xrange 返回迭代器<type 'xrange'>
    # n 值超大时，建议使用 xrange
    ```

## 算法编程
* 去除列表中的重复元素
    ```python
    ```
* 创建字典的方法
    * 1 直接创建:
    * 2 工厂方法:
    * 3 fromkeys()方法:

    ```python
    ```

* 合并两个有序列表
```python


```

* 二分查找
```python

```
* 求两棵树是否相同
```python

```

* 单链表逆置
```python
```


* 两个字符串是否是变位词

```python

```
