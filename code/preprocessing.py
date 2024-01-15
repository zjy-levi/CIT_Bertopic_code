import re
import jieba
from jieba import posseg as pseg
import pandas as pd
import os
import bertopic


def clean_text_lavn(text):
    '''
    jieba分词词性选择：
    名词（不要人名）
    动词类
    形容词类
    成语（如果有的话）
    '''
    stopwords = ['西安','酒店','你们','他们','我们','还有','感觉','时候']
    words= pseg.lcut(text)
    words = [i for i,f in words if len(i)>=2 and (f=='n' or f.startswith('v') or f.startswith('a') or f.startswith('l'))]
    return ' '.join(words)

if __name__  == "__main__":
    os.chdir("../data")
    
    data = pd.read_csv('reviews&rating.csv',index_col=0)
    # concate title with reviews
    data['text']=data['title'].str.cat(data['review'],sep='。')
    # string preprocessing, get rid of those names or frequent but no information words
    data['content']=data['text'].astype(str).apply(clean_text_lavn)
    # drop the "zero_information_reviews"
    data.dropna(inplace=True)
    data.to_csv('酒店评论_语料.csv')
    
    
    # Bertopic
    topic_model = bertopic.BERTopic(language="chinese (simplified)", calculate_probabilities=True, 
    verbose=True, nr_topics='auto')
    # positive topics
    topics1, probs = topic_model.fit_transform(data['content'].to_list())
    os.chdir('../model')
    topic_model.save('中文分词模型_new')
    topic_model.visualize_term_rank()#.
    # negetive topics
    chaping = data[data['label']==-1]
    chaping[['content','topic']]
    haopin = data[data['label']==1]
    topics = chaping['topic'].value_counts()[chaping['topic'].value_counts()>10].index[1:9]
    
    