#大赢家根据规则自动下注脚本

[![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)](https://www.python.org/)

### 环境设置

```
帐号 loginName  密码 loginPwd    支付id  accountId
```

 ### 启动项目前准备

```
pip install -r requirements
```

### 启动项目

```
1.保证已经启动redis
2.项目目录下运行
celery -A tasks beat -l info
celery -A tasks worker -l info
```
