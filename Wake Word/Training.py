import datetime
import librosa, librosa.display
import numpy
import os
import pandas
import sounddevice
import tensorflow

from scipy.io.wavfile import write
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.utils import to_categorical

def recWW(dir, times):
    #times = int(times)
    input("Press ENTER to record.")
    for nthTime in range(times):
        soundRate = 44100
        seconds = 2
        wwRec = sounddevice.rec(int(seconds * soundRate), samplerate = soundRate, channels = 2)
        sounddevice.wait()
        recordingName = datetime.datetime.now().strftime("%Y-%B-%H-%M-%S")
        write(dir + str(recordingName) + ".wav", soundRate, wwRec)
        input(f"Press ENTER to continue - {nthTime + 1}/{times}.")

def recBD(dir, times):
    input("Press ENTER to record.")
    for nthTime in range(times):
        soundRate = 44100
        seconds = 2
        bdRec = sounddevice.rec(int(seconds * soundRate), samplerate = soundRate, channels = 2)
        sounddevice.wait()
        recordingName = datetime.datetime.now().strftime("%Y-%B-%H-%M-%S")
        write(dir + str(recordingName) + ".wav", soundRate, bdRec)
        print(f"{nthTime + 1}/{times}.")

recBD("Wake Word/Background Data/", 50)
#WW iterations: Hondo J, Hey hondo J, hello hondo J, activate hondo J, hondo turn on J, hi hondo J

#processing function
def  processData():
    allData = []
    dataDir = {
        0: ["Wake Word/Background Data/" + fileDir for fileDir in os.listdir("Wake Word/Background Data/")],
        1: ["Wake Word/WW Data/" + fileDir for fileDir in os.listdir("Wake Word/WW Data/")]
    }
    for dataClass, allFiles in dataDir.items():
        for everyFile in allFiles:
            dataFile, soundRate = librosa.load(everyFile)
            mfcc = librosa.feature.mfcc(y = dataFile, sr = soundRate, n_mfcc = 40)
            processMfcc = numpy.mean(mfcc.T, axis = 0)
            allData.append([processMfcc, dataClass])
        print(f"Data class {dataClass} processing done.")
    dataset = pandas.DataFrame(allData, columns = ["feature", "dataClass"])
    dataset.to_pickle("Dataset.csv")


#Model training function
def trainModel():
    dataset = pandas.read_pickle("Wake Word/Dataset.csv")
    X = dataset["feature"].values
    X = numpy.concatenate(X, axis = 0).reshape(len(X), 40)
    Y = numpy.array(dataset["dataClass"].tolist())
    Y = to_categorical(Y)
    xTraining, xTesting, yTraining, yTesting = train_test_split(X, Y, test_size = 0.2, random_state = 42)
    model = Sequential([
        Dense(256, input_shape = xTraining[0].shape),
        Activation("relu"),
        Dropout(0.5),
        Dense(256),
        Activation("relu"),
        Dropout(0.5),
        Dense(2, activation = "softmax")
    ])
    print(model.summary())
    model.compile(
        loss = "categorical_crossentropy",
        optimizer = "adam",
        metrics = ["accuracy"]
    )
    trainingHistory = model.fit(xTraining, yTraining, epochs = 1000)
    model.save("Model.h5")
    trainingScore = model.evaluate(xTesting, yTesting)
    print(trainingHistory)
    print(trainingScore)
    yPrediction = numpy.argmax(model.predict(xTesting), axis = 1)
    confusionMatrix = confusion_matrix(numpy.argmax(yTesting, axis = 1), yPrediction)
    print(classification_report(numpy.argmax(yTesting, axis = 1), yPrediction))
    ConfusionMatrixDisplay(confusionMatrix, classes = ["0 - Not detected", "1 - Detected"])
