# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:14:56 2020

@author: 1426391
Writing Files
We can open a file object using the method write() to save the text file to a list.
 To write the mode, argument must be set to write w. 
 Let’s write a file Example2.txt with the line: “This is line A”
"""
#you will need the following library 
#!pip install ibm_watson wget
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"
iam_apikey_s2t = ""
#Consider the dataframe df, how would you find the element in the second-row and first column.
#  df.ix[1,0] or df.iloc[1,0]
import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df.head()

dft=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
dft['a']==1

df.to_csv("file.csv")