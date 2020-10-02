# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:47:36 2020

@author: pavan
"""

import web_scrapper_jobs_selenium as ws
import pandas as pd
import os

##path = 'C:\\Users\\pavan\\ML\\salary_estimator\\'



df = ws.get_jobs('data scientist',20,False,20)