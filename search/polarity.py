from __future__ import division, print_function, absolute_import
import tflearn
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.datasets import imdb
import numpy as np
import re
#from collections import Counter
import word2vec
from textblob import TextBlob

def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def CreateModel():

    net = tflearn.input_data([None, 100])
    net = tflearn.embedding(net, input_dim=10000, output_dim=128)
    net = tflearn.lstm(net, 128, dropout=0.8)
    net = tflearn.fully_connected(net, 2, activation='softmax')
    net = tflearn.regression(net, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')
    model = tflearn.DNN(net, tensorboard_verbose=0)
    return model

def FitModel(model):
    train, test, _ = imdb.load_data(path='imdb.pkl', n_words=10000,
                                    valid_portion=0.1)
    trainX, trainY = train
    testX, testY = test
    trainX = pad_sequences(trainX, maxlen=100, value=0.)
    testX = pad_sequences(testX, maxlen=100, value=0.)
    trainY = to_categorical(trainY, nb_classes=2)
    testY = to_categorical(testY, nb_classes=2)
    model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, batch_size=32)
    model.save("MyModel.pkl")

def sentiment(test):
    model = CreateModel()
    #FitModel(model)
    Vector = word2vec.load("vectors.bin")
    print()
    vec=Vector[test]
    print(vec)
    t = model.predict(vec)
    print(t)
    return t
def gsentiment(tweet):
        analysis = TextBlob(clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0.5
        else:
            return 0

k=gsentiment("Fuck you")
print(k)
