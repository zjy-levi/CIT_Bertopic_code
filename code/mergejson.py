import os
import json
from jsonpath import jsonpath
import pandas as pd
import numpy as np

def mergejson(filename):
    j_all = {}
    for i in os.scandir():
        if i.name.split('.')[-1] == 'json':
            with open(f'{i.name}','r',encoding='utf-8') as f:
                a = json.load(f)
                j_all[i.name.split('.')[0]]=a

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(j_all, f,ensure_ascii=False)

def construct_traindata():
    # merge all ratings and reviews information
    review=[]
    rating=[]
    title=[]
    kind=[]
    join =[]
    subtime = []
    attribution = []
    photo_num = []
    vote_num = []
    hotelrating = []
    for i in os.scandir(): 
        if i.name.split('.')[-1] =='json': 
            with open(f'{i.name}','r',encoding='utf-8') as f:
                a=json.load(f)
                if len(jsonpath(a,'$[*].content'))!=len(jsonpath(a,'$[*].memberInfo.joinTime')):
                    for j in jsonpath(a,'$[*]'):
                        try:
                            jointime = jsonpath(j,'$..memberInfo.joinTime')[0]
                            join.append(jointime)
                        except:
                            join.append(np.nan)
                else:
                    join.extend(jsonpath(a,'$[*].memberInfo.joinTime'))
                review.extend(jsonpath(a,'$[*].content'))
                rating.extend(jsonpath(a,'$[*].rating'))
                hotelrating.extend(jsonpath(a,'$[*].locationInfo.rating'))
                title.extend(jsonpath(a,'$[*].title'))
                kind.extend(jsonpath(a,'$[*].tripTypeString'))
                subtime.extend(jsonpath(a,'$[*].submitTime'))
                attribution.extend(jsonpath(a,'$[*].attribution'))
                photo_num.extend(list(map(lambda x:len(x) if isinstance(x,list) else 0,jsonpath(a,'$[*].photos'))))
                vote_num.extend(jsonpath(a,'$[*].voteCount'))
            print(f'{i.name} have finished')
    df=pd.DataFrame({'title':title,'review':review,"kind":kind,"jointime":join,"subtime":subtime,"attribution":attribution,"photo_num":photo_num,"rating":rating,'hotelrating':hotelrating,"vote_num":vote_num})
    df.to_csv('reviews&rating.csv')
    return df

if __name__ == '__main__':
    os.chdir('../data')
    filename = 'all_hotel.json'
    mergejson(filename)
    df = construct_traindata()
    
    