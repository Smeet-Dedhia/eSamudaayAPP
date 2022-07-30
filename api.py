from fastapi import FastAPI
import pandas as pd
#import numpy as np
import json
#import requests

df = pd.read_csv(r'data.csv')

app = FastAPI()

#Function for API
#Function for API
#Function for API
def productsInfo(bizID):
    total = int(df.loc[df.BusinessID==bizID, 'TotalSKU'].values[0])
    img = int(df.loc[df.BusinessID==bizID, 'ImageMissing'].values[0])
    prop = int(df.loc[df.BusinessID==bizID, 'skuPropMissing'].values[0])
    name = int(df.loc[df.BusinessID==bizID, 'mfrNameMissing'].values[0])
    addr = int(df.loc[df.BusinessID==bizID, 'mfrAddMissing'].values[0])
    #if((img==0) and (prop==0) and (name==0) and (addr==0)):
    #    return 'No failed products! All products have passed'
    #else:
    x = {"TotalSKU":total,
        "ImageMissing":img,
        "SKUpropMissing":prop,
        "MFRnameMissing":name,
        "MFRaddMissing":addr}
    #x = '{"TotalSKU":{t},"ImageMissing":{i}, "SKUpropMissing":{p}, "MFRnameMissing":{n}, "MFRaddMissing": {a}}'.format(t=total,i=img,p=prop,n=name,a=addr)
    return json.loads(json.dumps(x,indent=4))

@app.get('/productInfo/{query}')
def fun(query:str):
    return productsInfo(query)