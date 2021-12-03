# gogs

1， 按照 docker-compose 文件启动 gogs

2， 用户设置 - 管理 ssh 密钥：

- 你本机的公钥，用于提交代码

- 你服务器的公钥，用于部署代码。放在这里的好处是相同用户下的多个仓库不需要重复设置


# drone

1, 配置 docker-compose：

- 填写空缺字段

2，启动 drone 后，进入 settings/secrets

name: ssh_key
value: 服务器的私钥（该私钥对应的公钥需写入服务器的 authorized_keys）

3，仓库中需要包含 .drone.yml 文件
