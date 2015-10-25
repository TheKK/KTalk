#!/usr/bin/env python

# -*- coding: utf-8 -*-

import json
from pprint import pprint
from src.news import *
from src.atms import *
from src.branches import *

a = Atm()
a.show_atm_direction()

b = Branch()
b.show_branch_direction()
