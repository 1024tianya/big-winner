# Version: 1.0
FROM huakai/base_env:3.6.4

WORKDIR /usr/src/app/scan-rpc

COPY requirements.txt ./
COPY supervisord.conf ./

RUN pip install -i http://pypi.douban.com/simple --no-cache-dir -r requirements.txt --trusted-host pypi.douban.com
