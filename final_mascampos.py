# -*- coding: utf-8 -*-
# IS602 final project
# Marco Siqueira Campos

#import csv
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pylab as pl

# Load data base
poa_db = pd.read_csv('https://raw.githubusercontent.com/MarcoSCampos/testdata/master/poa_database.csv')
poa_nbh = pd.read_csv('https://raw.githubusercontent.com/MarcoSCampos/testdata/master/poa_nbh.csv')

# Tiding
poa_db.rename(columns={'Bairro':'nbh','Area':'area', 'Valor':'value', 'Dormitorios':'rooms', 'Vagas':'parking'}, inplace=True)
poa_nbh.rename(columns={'bairro':'nbh'}, inplace=True)

#LabelEncoder
poa_nbh.insert(0, 'nbh_id', range(0, len(poa_nbh)))

# Merge with right join
poa_db2=pd.merge(poa_nbh, poa_db, on='nbh', how='right')
poa_db2.head()

poa_db2['nbh2']=pd.Series(poa_db2.nbh, index=poa_db2.index).str.replace('_',' ')
poa_nbh['nbh2']=pd.Series(poa_nbh.nbh, index=poa_nbh.index).str.replace('_',' ')

a=False
if a:
 #Linear modeling
 #lm=smf.ols(formula='value ~ area + rooms + parking + nbh', data=poa_db).fit()
 lm=smf.ols(formula='value ~ area + rooms + parking + nbh', data=poa_db2).fit()
 new={'area':[50],'rooms':[2],'parking':[1], 'nbh':['Centro']}
 z=lm.predict(new)[0]
 print z
else:
 new1=pd.DataFrame({'area':[50],'rooms':[2],'parking':[1], 'nbh_id':[12]})
 cols = ['area', 'rooms', 'parking','nbh_id']
 rf = RandomForestRegressor(n_estimators=150)
 rf.fit(poa_db2[cols], poa_db2.value)
 z=rf.predict(new1[cols])[0]
 print z

