import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import re
import nltk
nltk.download('punkt_tab')
from nltk import word_tokenize, sent_tokenize
import gc
import torch
from torch import tensor
import torch.nn as nn
import torch.nn.functional as F


def load_data(file_path):
    return open(file_path).read()

def clean_data(file_content):
    repl='' # string for replacement

    # removing all open brackets
    file_content = re.sub('\(', repl, file_content)
    
    # removing all closed brackets
    file_content = re.sub('\)', repl, file_content)
    
    # removing all the headings in data
    for pattern in set(re.findall("=.*=", file_content)):
        file_content = re.sub(pattern, repl, file_content)
    
    # removing unknown words in data
    for pattern in set(re.findall("<unk>", file_content)):
        file_content = re.sub(pattern, repl, file_content)
    
    # removing all the non-alphanumerical characters
    for pattern in set(re.findall(r"[^\w ]", file_content)):
        repl = ''

        if pattern == '-':
            repl=' '

        # retaining period, apostrophe
        if pattern != '.' and pattern != "\'":
            file_content = re.sub("\\" + pattern, repl, file_content)
            
    return file_content

def split_data(file_content, num_sentences=-1):
    # sentence tokenization
    if num_sentences == -1:
        sentences = sent_tokenize(file_content)

    else:
        sentences = sent_tokenize(file_content)[:num_sentences]
    
    # word tokenization
    words = set()
    for sent in sentences:
        for word in str.split(sent, ' '):
            words.add(word)
    words = list(words)
    
    # adding empty string in list of words to avoid confusion while padding.
    # padded zeroes can be interpreted as empty strings.
    words.insert(0, "")
    
    return sentences, words


if __name__ == "__main__":
    file_content = load_data("data/test.txt")
    file_content = clean_data(file_content)
    data = split_data(file_content, num_sentences=10)

    print(data)