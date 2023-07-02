import json
import nltk
import numpy
import pickle
import random
import ssl
import tensorflow

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD

tags = []
patterns = []
finalComms = []
ignorePatterns = ["!", ".", ",", "?", ";", ":", "'", "~", "-", "/"]

lemmatize = WordNetLemmatizer()
dataset = json.loads(open("comms_ai/dataset.json").read())

for comms in dataset["Tasks Comms"]:
    for everyPattern in comms["patterns"]:
        listOfWords = nltk.word_tokenize(everyPattern)
        patterns.extend(listOfWords)
        finalComms.append((listOfWords, comms["tag"]))
        if comms["tag"] not in tags:
            tags.append(comms["tag"])

patterns = [lemmatize.lemmatize(allWords.lower()) for allWords in patterns if allWords not in ignorePatterns]
patterns = sorted(set(patterns))
tags = sorted(set(tags))
pickle.dump(patterns, open("Patterns.pkl", "wb"))
pickle.dump(tags, open("Tags.pkl", "wb"))

modelTraining = []
emptyNN = [0] * len(tags)

for final in finalComms:
    nnBag = []
    sentencePatterns = final[0]
    sentencePatterns = [lemmatize.lemmatize(allWords.lower()) for allWords in sentencePatterns]
    for allPatterns in patterns:
        nnBag.append(1) if allPatterns in sentencePatterns else nnBag.append(0)
    nnOutput = list(emptyNN)
    nnOutput[tags.index(final[1])] = 1
    modelTraining.append([nnBag, nnOutput])

random.shuffle(modelTraining)
modelTraining = numpy.array(modelTraining)
X = list(modelTraining[:, 0])
Y = list(modelTraining[:,1])

model = Sequential()
model.add(Dense(128, input_shape = (len(X[0]),), activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(len(Y[0]), activation = "softmax"))

sgd = SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
model.compile(loss = "categorical_crossentropy", optimizer = sgd, metrics = ["accuracy"])
compression = model.fit(numpy.array(X), numpy.array(Y), epochs = 1000, batch_size = 5, verbose = 1)
model.save("Model.h5", compression)

#print("YAAAAAAYYYYYY! Training Complete!")
