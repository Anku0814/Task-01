import pandas as pd
import re

def clean_col(col):
    col=re.sub(r'[^\w\s]','',col)
    return col.lower().strip().replace(' ','_')

def clean_dataset():
    df=pd.read_csv('data/raw.csv')
    df.columns=[clean_col(c) for c in df.columns]
    df.to_csv('data/cleaned.csv', index=False)

if __name__=='__main__':
    clean_dataset()
