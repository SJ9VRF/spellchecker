

# In[4]:


def is_in_sentencce(sentence, substring):
    sentence = pre_process(sentence)
    sentence = sentence.split()
    if  substring in sentence:
        return 1
    else:
        return 0


# In[5]:


def pre_process(str_in):
    str_out = str_in.replace(',',' ')
    str_out = str_out.replace('.',' ')
    str_out = str_out.replace('-',' ')
    str_out = str_out.replace('-',' ')
    return str_out


# In[9]:


s_2 = input()
s_1 = input()


# In[10]:


print(is_in_sentencce(s_1, s_2))

