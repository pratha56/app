# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:02:46 2021

@author: asus
"""

import pandas as pd
import streamlit as st 
import seaborn as sns
from pickle import dump
from pickle import load

st.title('plot graph')
data=pd.read_excel(r"C:\Users\asus\Desktop\my desk\project\project retail.xlsx")
st.subheader('info')
st.subheader('prathamesh deore')
if st.checkbox('show info data'):
    st.subheader('info data')
    st.write(data)
bar=pd.read_csv(r'C:\Users\asus\Desktop\my desk\DEPLOYMENT\bar.csv')
st.bar_chart(data)

df=pd.read_csv(r'C:\Users\asus\Desktop\my desk\DEPLOYMENT\salermonth.csv')
x=int(input('CustomerID:'))
y=(salepermonth.loc[salepermonth['CustomerID']==x])
y=y.drop(y.iloc[:,0:1],axis=1)

month=['Apr-2011', 'Aug-2011', 'Dec-2010', 'Dec-2011', 'Feb-2011', 'Jan-2011',
       'Jul-2011', 'Jun-2011', 'Mar-2011', 'May-2011', 'Nov-2011', 'Oct-2011',
       'Sep-2011']
z=pd.DataFrame(df.loc[df['CustomerID']==x])
fig=plt.figure(figsize=(14,10))
a=plt.bar(month,y.iloc[0],color='red',width=0.5)
plt.show()

  