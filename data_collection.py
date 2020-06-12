#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:39:42 2020

@author: mark
"""

import glassdoor_scraper as gs
import pandas as pd

df = gs.get_jobs('data scientist', 15, False)
