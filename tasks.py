#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery import Celery
from cluster.api import index
import redis
import requests
import json
import redis_lock
app = Celery(__name__)
app.config_from_object("celeryconfig")

r_cache = redis.StrictRedis(host='127.0.0.1', port=6379, db=7)


def runk3(k3):
    with redis_lock.Lock(r_cache, '{0}-r-w-lock'.format(k3)):
        try:
            num = int(r_cache.get(k3))
            if num == 1:
                return
        except:
            r_cache.set(k3, 1)
    index(k3)
    with redis_lock.Lock(r_cache, '{0}-r-w-lock'.format(k3)):
        r_cache.set(k3, '结束')


@app.task
def ahk3():
    """
    AHK3
    :return:
    """
    # 链接redis
    runk3('AHK3')


@app.task
def gsk3():
    """
    GSK3
    :return:
    """
    runk3('GSK3')

@app.task
def gxk3():
    """
    GXK3
    :return:
    """
    runk3('GXK3')


@app.task
def gzk3():
    """
    GZK3
    :return:
    """
    runk3('GZK3')


@app.task
def hebk3():
    """
    HEBK3
    :return:
    """
    runk3('HEBK3')


@app.task
def hubk3():
    """
    HUBK3
    :return:
    """
    runk3('HUBK3')


@app.task
def jsk3():
    """
    JSK3
    :return:
    """
    runk3('JSK3')


@app.task
def shk3():
    """
    SHK3
    :return:
    """
    runk3('SHK3')


@app.task
def xy1k3():
    """
    XY1K3
    :return:
    """
    # print(1111111111111111)
    runk3('XY1K3')
