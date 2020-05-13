# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from datetime import datetime
import json
import os
import matplotlib.pyplot as plt

path = "data/piersul"

root0,dirs0,files0 = list(os.walk(path))[0]
infiles0 = [os.path.join(root0,f) for f in files0]
infiles0

dfs=[]
for f in infiles0:
    with open(f,'r') as inf:
        df = pd.read_csv(inf)
        dfs.append(df.drop_duplicates())
df_all = pd.concat(dfs)

df_all.drop('Unnamed: 0',axis=1,inplace=True)

print(df_all.shape)


# a=df_all.iloc[:5].to_csv(path+"/new.csv", index=False)
