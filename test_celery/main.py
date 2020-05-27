from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://아이디:패스워드@호스트/vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
