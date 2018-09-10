#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

broker_url = os.getenv('CELERY_SCANNER_BROKER_URL', None)

worker_prefetch_multiplier = 1

task_queues = {
    'ahk3': {
        'exchange': 'ahk3',
        'exchange_type': 'direct',
        'routing_key': 'ahk3'
    },
    'gsk3': {
        'exchange': 'gsk3',
        'exchange_type': 'direct',
        'routing_key': 'gsk3'
    },
    'gxk3': {
        'exchange': 'gxk3',
        'exchange_type': 'direct',
        'routing_key': 'gxk3'
    },
    'gzk3': {
        'exchange': 'gzk3',
        'exchange_type': 'direct',
        'routing_key': 'gzk3'
    },
    'hebk3': {
        'exchange': 'hebk3',
        'exchange_type': 'direct',
        'routing_key': 'hebk3'
    },
    'hubk3': {
        'exchange': 'hubk3',
        'exchange_type': 'direct',
        'routing_key': 'hubk3'
    },
    'jsk3': {
        'exchange': 'jsk3',
        'exchange_type': 'direct',
        'routing_key': 'jsk3'
    },
    'shk3': {
        'exchange': 'shk3',
        'exchange_type': 'direct',
        'routing_key': 'shk3'
    },
    'xy1k3': {
        'exchange': 'xy1k3',
        'exchange_type': 'direct',
        'routing_key': 'xy1k3'
    }


}

task_routes = {
    'tasks.ahk3': {'queue': 'ahk3', 'routing_key': 'ahk3'},
    'tasks.gsk3': {'queue': 'gsk3', 'routing_key': 'gsk3'},
    'tasks.gxk3': {'queue': 'gxk3', 'routing_key': 'gxk3'},
    'tasks.gzk3': {'queue': 'gzk3', 'routing_key': 'gzk3'},
    'tasks.hebk3': {'queue': 'hebk3', 'routing_key': 'hebk3'},
    'tasks.hubk3': {'queue': 'hubk3', 'routing_key': 'hubk3'},
    'tasks.jsk3': {'queue': 'jsk3', 'routing_key': 'jsk3'},
    'tasks.shk3': {'queue': 'shk3', 'routing_key': 'shk3'},
    'tasks.xy1k3': {'queue': 'xy1k3', 'routing_key': 'xy1k3'},
}

beat_schedule = {
    'ahk3': {
        'task': 'tasks.ahk3',
        'schedule': 4*60-20,

    },
    'gsk3': {
        'task': 'tasks.gsk3',
        'schedule': 4*60-10,

    },
    'gxk3': {
        'task': 'tasks.gxk3',
        'schedule': 4*60+60,

    },
    'gzk3': {
        'task': 'tasks.gzk3',
        'schedule': 2*60+50,

    },
    'hebk3': {
            'task': 'tasks.hebk3',
            'schedule': 2*60+40,
    },
    'hubk3': {
        'task': 'tasks.hubk3',
        'schedule': 2*60+30,
    },
    'jsk3': {
        'task': 'tasks.jsk3',
        'schedule': 2*60+20,
    },
    'shk3': {
        'task': 'tasks.shk3',
        'schedule': 2*60+10,
    },
    # 'xy1k3': {
    #     'task': 'tasks.xy1k3',
    #     'schedule': 25,
    # },
}
