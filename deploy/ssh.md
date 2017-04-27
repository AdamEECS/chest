# linux 主机设置

## 生成 ssh-key

Mac 用户直接打开终端输入命令

Win 用户安装 Github Desktop 离线包后, 打开桌面的 git shell 程序, 在里面输入下面的命令

>注意 下面的 mykey 随便换一个你喜欢的名字, 这是一个标注, 方便你看的

```
ssh-keygen -C mykey
```

会提示你生成的文件的地址, 并且让你输入密码, 你不要输入密码, 直接回车。

这样你就得到了一对 ssh-key, 这是用于登录服务器用的。默认你会得到两个文件：

* id_rsa 是私钥 自己保存 不要给别人看

* id_rsa.pub 是公钥 是要到处使用的

## 重建服务器并且配置 ssh-key

去 vultr 的管理界面

先删除(Destory)现有的服务器

新建服务器的时候, 把刚才才生成的 id_rsa.pub 文件(用 atom/pycharm 可以打开)里面的内容加入到 ssh-key 步骤中
这样你就可以不用密码, 自动登录服务器了(windows 用户请看「windows上用bitvise软件使用sshkey登录.pdf」这个文件)

## 如果你不想重建服务器, 配置 ssh-key 的方法如下

在服务器把本机生成的 public key 添加到 /root/.ssh/authorized_keys 文件中

1. 用 root 用户登录到服务器, 创建 .ssh 目录
```
cd /root
mkdir .ssh
```
2. 编辑 authorized_keys 文件, 把刚才生成的 id_rsa.pub 文件里面的内容粘贴进去并保存退出

>注意, 这里可以粘贴多个 key, 一行一个
```
nano .ssh/authorized_keys
```

## 禁用服务器密码登录

```
nano /etc/ssh/sshd_config
```
找到并修改 `PasswordAuthentication no`，然后重启服务。
```
service sshd restart
```

## 服务器初始化配置, 复制这些命令粘贴到服务器终端中执行


安装 配置 打开 ufw 防火墙
```
apt-get install ufw
ufw allow 22
ufw allow 80
ufw allow 443
ufw default deny incoming
ufw default allow outgoing
ufw status verbose
ufw enable
```

## 安装必备软件

```
apt-get install git python3 python3-pip python3-setuptools supervisor mongodb redis-server zsh

```

## 安装 oh-my-zsh 配置(方便你使用命令行的配置)
```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

```
## 安装 gunicorn
```
pip3 install gunicorn
```

## 服务器中文编码问题

编辑下面的文件, 不要拼错
```
nano /etc/environment
```
加入下面的内容, 保存退出
```
LC_CTYPE="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
```
