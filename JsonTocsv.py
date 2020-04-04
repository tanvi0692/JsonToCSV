import json 
import csv
import copy

# csv_dic=[]
# with open('cbsd-information/output1.json') as f:
#     data = json.load(f)
#     data_dic = dict(data)
#     print(data_dic.keys())
    # for key in data:
    #     if data[key] is dict:

def getKeys(data,res_):
    
    
  
    if not isinstance(data,dict):
        return ['']
    
    for key in data.keys():
            temp = copy.deepcopy(getKeys(data[key],res_))
            # print(temp)
            for i, element in enumerate(temp):
                # print(key+"."+ element)
                temp[i]= key+"."+ element

                print(res_,temp[i])
                try:
                    res_.remove(element)
                except ValueError:
                    pass
                res_+=[temp[i]]  

    return res_

def getKeys_(data):
    
    
  
    if not isinstance(data,dict):
        return ['']
    res_ = []
    for key in data.keys():
            temp = copy.deepcopy(getKeys_(data[key]))
            # print(temp)
            for i, element in enumerate(temp):
                # print(key+"."+ element)
                temp[i]= key+"."+ element
                res_.append(temp[i])
    

    return res_
    
with open('cbsd-information/output1.json','r') as f:
    data = json.load(f)

keys = getKeys_(data['cbsdList'][0])
print(keys)

for item in keys:
    key = item.split('.')
    num = len(key) -1

    n = 0
    temp = data['cbsdList'][0]
    
    while n<=num-1:

        temp = temp[key[n]]
        n+=1
    print(temp)
    
                     
            
    