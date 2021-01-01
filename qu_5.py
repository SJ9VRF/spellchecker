import re
from collections import Counter
import numpy as np
import pandas as pd
# DO NOT add any library

# WRITE as many function as you want for clean code


def delete_letter(word):
    
    delete_l = []
    for i in range(len(word)):
        delete_l.append(word[:i]+word[i+1:])
    delete_l = list(set(delete_l))
    return delete_l
    
def replace_letter(word):
    replace_l=[]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
    for i in range(len(word)):
        for item in alphabet:
            replace_l.append(word[:i]+item+word[i+1:])    
    replace_l = list(set(replace_l))   
    return replace_l
    
def insert_letter(word):
    insert_l = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
    alphabet = alphabet + ['s','t','u','v','w','x','y','z']
    for i in range(len(word)):
        for item in alphabet:
            insert_l.append(word[:i]+item+word[i:])
    insert_l = list(set(insert_l)) 
    return insert_l

def edit_one_letter(word):
    """
    Input:
        word: the string/word for which we will generate all possible wordsthat are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """
    edit_one_set = set()
    edit_one_set.update(delete_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    return edit_one_set
    
def edit_two_letters(word):
    
    edit_two_set = set()
    degree_one = edit_one_letter(word)
    for item in degree_one:
        edit_two_set.update(edit_one_letter(item))
    
    return edit_two_set   

def process_text(text):

    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

    return clean_words

def autoCorrect(word):
    # we call this function in judge
    # Write your main code here and generate correct word as result.
    # please do not modify parameters or this function name
    with open('/Users/arefeh/Downloads/project-3/'+'shakespeare.txt') as f:
        data = f.read()
    data = data.split(' ')
    data = (' '.join(data)).split(' ')
    data_u = set(data)
    if word in data:
        return word
    else:
        candid = set(edit_one_letter(word))
    z = candid.intersection(data_u)
    if len(z) == 0:
        candid = set(edit_two_letters(word))
        z = candid.intersection(data)
        if len(z) == 0:
            return []
        else:
            z = list(z)
            prob = []
            for ztem in z:
                prob.append(float(data.count(ztem))/len(data))
            return list(z)[np.argmax(prob)]
    else:
        z = list(z)
        prob = []
        for ztem in z:
            prob.append(float(data.count(ztem))/len(data))
        return list(z)[np.argmax(prob)]
    
    return result

autoCorrect('flw')