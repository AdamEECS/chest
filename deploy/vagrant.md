vargrant 虚拟机:


安装 vagrant
Mac 直接输入下面命令
brew cask install vagrant

Windows 可以下载安装包
https://www.vagrantup.com/downloads.html

添加 box(box 相当于 windows 一键装机的镜像)
vagrant box add ubuntu/trusty64

注意, 如果在命令中安装, 可能会比较慢, 可以提前下载好 box 文件, 然后指定 box 的路径添加
Vagrant box add /<path>/<boxname>

卸载
vagrant box remove ubuntu/trusty64



创建目录
mkdir vagrant_demo

进入目录
cd vagrant_demo

初始化
vagrant init

修改 Vagrantfile 配置文件, 这里的 boxname 与前面添加的一致, 例子中是 ubuntu/xenial64
config.vm.box = "ubuntu/xenial64"



启动 vagrant 虚拟机
vagrant up

使用 ssh 的方式连接虚拟机
vagrant ssh

切换 root 用户
sudo su

安装软件
sudo apt-get install 软件名称



vagrant 有一个图形化的管理工具 vagrant manager, 使用很方便
Mac 安装:
brew cask install vagrant-manager

windows 安装:
http://vagrantmanager.com/windows/


https://atlas.hashicorp.com/ubuntu/boxes/xenial64/versions/20170417.0.0/providers/virtualbox.box
