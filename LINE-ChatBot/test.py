#!/usr/bin/env python

# -*- coding: utf-8 -*-

import json
from src.news import *

new = get_lastest_news()

with open('haha', mode='wb') as fp:
	fp.write(json.dumps(new).encode('utf-8'))
