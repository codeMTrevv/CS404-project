import random
import json
import pickle
import numpy as np


import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, activation, dropout
from tensorflow.keras.optimizers import Sgd

lammatizer = WordNetLemmatizer()

intents = json.load(open("intents.json").read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',', ';', ':', '(', ')', '[', ']', '{','}']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)