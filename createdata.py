# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 00:33:19 2016
@author: zhuchao1
"""
import csv as csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random as rd
import pandas.io.data as web
from datetime import datetime
if __name__ == "__main__":
    #stock symbols list
    SYMBOL=['A','AAPL','ORCL','C','GOOG','HOG','HPQ','INTC','KO','LUV','MMM','MSFT','T','TGT','TXN','WMT']
    start = datetime(2014,1,1)
    end = datetime(2014,12,31)
    stockRawData = web.DataReader(SYMBOL, 'yahoo', start, end)
    sliceKey = 'Adj Close'
    adjCloseData = stockRawData.ix[sliceKey]
    adjCloseData=np.log(adjCloseData, dtype='float64')
    mean=adjCloseData.mean()
    std=adjCloseData.std()
    #stock symbols
    SYMBOL_n=len(SYMBOL)    
    n=300
    date1=pd.date_range('1/1/2014',periods=n)
    #output the data to a csv file
    with open('/Users/zhuchao1/q/data.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['DATE','TIME','SYMBOL','PRICE','VOLUME'])
        for k in range(n):
            date=date1[k].strftime('%d/%m/%Y')
            date_begin=date+' 10:00:00'
            date_end=date+' 16:00:00'
            rng = pd.date_range(start=date_begin,end=date_end,freq='S')
            M=len(rng)
            for kk in range(M):
                field1=rng[kk].strftime('%Y%m%d')
                field2=rng[kk].strftime('%H:%M:%S')
                r=rd.randint(0,SYMBOL_n-1)
                field3=SYMBOL[r]
                field4=eval("rd.lognormvariate({0},{1})".format(mean[field3],std[field3]))
                field5=rd.randint(1000,10000)
                filed=[field1,field2,field3,field4,field5]
                spamwriter.writerow(filed)
    
                
                
                
                
            
        
        