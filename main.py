
import datarobot as dr
from datarobot import Project, Deployment
import pandas as pd
from pandas import json_normalize
import numpy as np
import datetime as dt
from datetime import datetime
import dateutil.parser
import os
import re 
from importlib import reload




# DR connection here: 
# dr.Client(config_path='path-to-drconfig.yaml')

# pull sample data
from src.raw_data.sample_data import sample_data_raw
df = sample_data_raw()



# plot - Remove this later
# import matplotlib.pyplot as plt
# df.pivot(index='Date', columns='Store', values='Sales').plot(figsize=(18, 8));
# plt.show()




# Defaults
HOLDOUT_START_DATE  =  pd.to_datetime('2014-04-12')
HOLDOUT_DURATION    =  dr.helpers.partitioning_methods.construct_duration_string(years=0, months=0, days=64)   

# Known In Advance columns
KIA_VARS   = ['Store_Size', 'Marketing', 'TouristEvent']

FEATURE_SETTINGS = []
for column in KIA_VARS:
    FEATURE_SETTINGS.append(dr.FeatureSettings(column, known_in_advance=True, do_not_derive=False))
    
# Create a calendar from a dataset
# data_path = 'https://docs.datarobot.com/en/docs/api/guide/common-case/Calendar.csv'
# dataset = dr.Dataset.create_from_url(data_path)
# CAL = dr.CalendarFile.create_calendar_from_dataset(
#     dataset.id
# )
# CAL_ID = CAL.id

print(FEATURE_SETTINGS)
print(' ')
# print(CAL_ID)