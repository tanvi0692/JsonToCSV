import json 
import csv
import copy
import pandas as pd
import argparse




def getKeys_(data):  
    if not isinstance(data,dict):
        return ['']
    res_ = []
    for key in data.keys():
            temp = copy.deepcopy(getKeys_(data[key]))
            for i, element in enumerate(temp):
                if element == '':
                    temp[i]= key
                else:
                    temp[i]= key+"."+ element
                res_.append(temp[i])
    return res_
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='file-path')
    parser.add_argument('-f', dest='filename', help='add file name')
    res = parser.parse_args()
    
    
     
    with open('{}'.format(res.filename),'r') as f:
        data = json.load(f)

    keyList = getKeys_(data["India"][0])
    keyDict = {key: [] for key in keyList} 
    for value in data["India"]:
        for item in keyList:
            key = item.split('.')
            temp,num,n = value,len(key)-1, 0
            while n<=num:
                try:
                    temp = temp[key[n]]
                    n+=1
                except KeyError:
                    temp = None
                    break
            keyDict[item].append(temp)

    df = pd.DataFrame(keyDict)
    df.to_csv('{}.csv'.format(res.filename.split('.')[0]), sep='\t')
    
                     
            
    