
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string


# In[2]:


path_train = '/Users/arefeh/Downloads/train/train.csv'
path_test = '/Users/arefeh/Downloads/train/test.csv'


# In[3]:


data_train = pd.read_csv(path_train)  
data_test = pd.read_csv(path_test) 


# In[27]:


data_train = data_train.dropna()
#data_train = data_train.fillna('')
#data_test = data_test.fillna('')


# In[5]:


#Need to download stopwords
nltk.download('stopwords')


# In[6]:


def process_text(text):

    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

    return clean_words


# In[7]:


from sklearn.feature_extraction.text import CountVectorizer


# In[36]:


all_data = data_train['Text'].append(data_test['Text'], ignore_index=True)


# In[43]:


len(all_data)


# In[38]:


messages_bow = CountVectorizer(analyzer=process_text).fit_transform(all_data)


# In[58]:


M = messages_bow.toarray()


# In[68]:


X_train = M[:len(data_train)]
X_test = M[len(data_train):]


# In[70]:


y_train = data_train['Class']


# In[71]:


from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X_train, y_train)


# In[ ]:


#Print the predictions
print(classifier.predict(X_train))
#Print the actual values
print(y_train.values)


# In[26]:


messages_bow_test = CountVectorizer(analyzer=process_text).fit_transform(data_test['Text'])


# In[72]:


res = classifier.predict(X_test)


# In[76]:


with open('/Users/arefeh/Downloads/'+'submission.csv','w') as f:
    for item in res:
        f.write(str(item)+',')

