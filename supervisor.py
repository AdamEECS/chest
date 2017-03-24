'''
下面的所有命令都是 root 用户去执行的, 不重复说明了

安装 supervisor
apt-get install supervisor

启动 supervisor
service supervisor start

重启 supervisor
service supervisor restart


配置一个 supervisor 监控的服务, 以 weibo 为例

在 /etc/supervisor/conf.d 目录下建立任意名字的 .conf 文件
这里用 weibo.conf 为例子, 然后填入下面的四行
第一行指定这个服务的名字, weibo, 随便不要重复的名字就好
第二行是启动程序的命令, 这里用了绝对路径来确保不出错(--pid /tmp/weibo.pid 这个参数是套路)
第三行是你启动程序之前, 先要进到的目录
第四行是自动启动
第五行是自动重启

[program:weibo]
command=/usr/local/bin/gunicorn wsgi --bind 127.0.0.1:8000 --pid /tmp/weibo.pid
directory=/home/wor/weibo_flask
autostart=true
autorestart=true




在你配置好了之后, 直接重启 supervisor 就好了(上面有重启的命令)


'''
