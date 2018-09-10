#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import os

def login():
    url = 'https://www.dyjaomen.com/tools/_ajax/login'
    headers = {'authority': 'www.dyjaomen.com',
               'method': 'POST',
               'path': '/tools/_ajax/XY1K3/betSingle',
               'scheme': 'https',
               'accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9',
               'content-type': 'application/json',
               'origin': 'https://www.dyjaomen.com',
               'referer': 'https://www.dyjaomen.com/lottery/K3/XY1K3',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/68.0.3440.106 Safari/537.36'}
    data = {"loginName": os.getenv('loginName'), "loginPwd": os.getenv('loginPwd'), "validCode": "",
            "validateDate": "{0}", "isdefaultLogin": 'true'}
    s = requests.session()
    r = s.post(url, headers=headers, data=json.dumps(data))
    with open('./log/Cookie.log', 'r+') as f:
        f.seek(0)
        f.write(str(dict(s.cookies)['JSESSIONID']))


def headers():
    cookie = open('./log/Cookie.log', 'r+')
    cookie_read = cookie.read()
    headers = {'authority': 'www.dyjaomen.com',
               'method': 'POST',
               'path': '/tools/_ajax/cache/lotterySetting',
               'scheme': 'https',
               'accept': '*/*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9',
               'content-length': '3277',
               'content-type': 'application/json',
               'cookie': 'JSESSIONID={0}'.format(cookie_read),
               'origin': 'https://www.dyjaomen.com',
               'referer': 'https://www.dyjaomen.com/lottery/K3/XY1K3',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36'}
    cookie.close()
    return headers


def requt(k3):
    url = 'https://www.dyjaomen.com/tools/_ajax/cache/lotteryOpenCache'

    data = json.dumps({"requirement": ["{0}".format(k3)]})
    try:
        r = requests.post(url, headers=headers(), data=data, verify=False).json()
        if r['code'] != 'success':
            login()
            r = requests.post(url, headers=headers(), data=data, verify=False).json()
        return r
    except:
        time.sleep(3)
        r = requests.post(url, headers=headers(), data=data, verify=False).json()
        print('查询出错啦')
        return r


def pose_send(money, issue, result, k3):
    url = 'https://www.dyjaomen.com/tools/_ajax/XY1K3/betSingle'

    data = {"accountId": os.getenv('accountId'), "clientTime": int(time.time()), "gameId": k3, "issue": "{0}".format(issue),
            "item": ["{\"methodid\":\"K3002001001\",\"nums\":1,\"rebate\":\"0.00\",\"times\":\""
                     ""+"{0}".format(money)+"\",\"money\":"+"{0}".format(money)+",\"mode\":1,\"issueNo\":\""
                     ""+"{0}".format(issue)+"\",\"codes\":\""+"{0}".format(result)+"\",\"playId\":[\"K3002001009\"]}"]}
    try:
        r =requests.post(url, headers=headers(), data=json.dumps(data))
    except:
        r = requests.post(url, headers=headers(), data=json.dumps(data))
