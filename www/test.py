#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
测试脚本：插入数据
'''

__author__ = 'Jay Yin'

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    #loop.run_forever()