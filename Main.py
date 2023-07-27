print("Importing Modules...")
import json
print("Imported json")
import librosa
import nltk
import numpy
import pickle
import random
import re
import sounddevice

from nltk import WordNetLemmatizer
from scipy.io.wavfile import write
from keras.models import load_model

from Tasks import *
from Engine import speak

#connectionCheck()

lemmatize = WordNetLemmatizer()
comms = json.loads(open("comms_ai/dataset.json").read())
patterns = pickle.load(open("comms_ai/Patterns.pkl", "rb"))
tags = pickle.load(open("comms_ai/Tags.pkl", "rb"))
modelComms = load_model("comms_ai/Model.h5")

def setupSentence(sentence):
    sentencePatterns = nltk.word_tokenize(sentence)
    sentencePatterns = [lemmatize.lemmatize(allWords) for allWords in sentencePatterns]
    print("code reached, end of setupSentence function")
    return sentencePatterns

def setupWords(sentence):
    sentencePatterns = setupSentence(sentence)
    pattern = [0] * len(patterns)
    for s in sentencePatterns:
        for tag, allPatterns in enumerate(patterns):
            if allPatterns == s:
                pattern[tag] = 1
    print("code reached, end of setupWords function")
    return numpy.array(pattern)

def prediction(sentence):
    userInput = setupWords(sentence)
    gotInput = modelComms.predict(numpy.array([userInput]))[0]
    lowestPred = 0.90
    finalPred = [[sentencePatterns, prediction] for sentencePatterns, prediction in enumerate(gotInput) if prediction > lowestPred]
    finalPred.sort(key = lambda x:x[1], reverse = True)
    prediction = []
    for pred in finalPred:
        prediction.append({"Tag": tags[pred[0]], "Accuracy": str(pred[1])})
    print(f"code reached, end of prediction function. prediction = {prediction}")
    return prediction

def tasksExecution(commsTags, CommsJson, sentence):
    try:
        getTag = commsTags[0]["Tag"]
        getComms = CommsJson["Tasks Comms"]
        for tag in getComms:
            if tag["tag"] == getTag:
                print(getTag)
                finalTag = getTag
                print(finalTag)
                answer = random.choice(tag["responses"])
                print(f"ANSWER = {answer}")
                # speak(random.choice(tag["responses"]))
                print("End of the function")
                break
        
        if finalTag == "Time":
            print("code reached, if finalTag == time has been called")
            currentTime()
        elif finalTag == "Day":
            currentDay()
        elif finalTag == "Month":
            currentMonth()
        elif finalTag == "Date":
            currentDate()
        elif finalTag == "Coinflip":
            coinFlip()
        elif finalTag == "Diceroll":
            diceRoll()
        elif finalTag == "Jokes":
            Jokes()
        elif finalTag == "Programming Jokes":
            proJokes()
        elif finalTag == "Blackjack":
            blackjack()
        elif finalTag == "Repeat After Me":
            repeatMe(sentence)
        elif finalTag == "Google Search":
            googleSearch(sentence)
        elif finalTag == "You.com Search":
            youSearch(sentence)
        elif finalTag == "Youtube":
            playOnYt(sentence)
        elif finalTag == "Wikipedia":
            wikiSearch(sentence)
        elif finalTag == "Screenshots":
            screenshots()
        elif finalTag == "Calculator":
            calculator(sentence)
        elif finalTag == "Volume Up":
            volUp()
        elif finalTag == "Volume Down":
            volDown()
        elif finalTag == "Mute Volume":
            muteVol()
        elif finalTag == "Read This":
            readThis()
        elif finalTag == "Open App":
            openApp(sentence)
        elif finalTag == "Close App":
            closeApp(sentence)
        elif finalTag == "Create Reminder":
            createReminder(sentence)
        elif finalTag == "Remind":
            remind()
        elif finalTag == "News":
            currentNews(sentence)
        elif finalTag == "Weather":
            weather()
        elif finalTag == "Start My Day":
            startMyDay()
        elif finalTag == "Work Mode":
            workMode()
        elif finalTag == "Ru Mode":
            ruMode()
    except Exception:
        speak("Sorry, I didn't get that.")

def center():
    answers = [
        "Yes?",
        "I'm listening",
        "How can I help you?",
        "What is it?",
        "How can I be of assistance?",
        "What?"
    ]
    speak(random.choice(answers))
    #while True:
    sentence = speechRecognition().lower()
    print(f"""
    
    You: {sentence}.
    
    """)
    multiTasks(sentence)
    #print("code reached, end of center function")

#Multiple Tasks at once
def multiTasks(sentence):
    try:
        splitWords = re.split(" and | then | also | too | moreover ", sentence)
        for tasks in splitWords:
            predictTasks = prediction(tasks)
            tasksExecution(predictTasks, comms, tasks)

    except Exception as multiTasks_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(multiTasks_Exception))
        log.close()
        Error_Occurred(multiTasks_Exception,"")
    #print("code reached, end of multiTaskFunction")

#Wake Word Detection:
def wwDetect():
    soundRate = 44100
    seconds = 2
    lastRec = "Wake Word/Last Rec.wav"
    wwModel = load_model("Wake Word/Model.h5")
    while True:
        print("Detecting...")
        newRec = sounddevice.rec(int(seconds * soundRate), samplerate = soundRate, channels = 2)
        sounddevice.wait()
        write(lastRec, soundRate, newRec)
        audio, sampleRate = librosa.load(lastRec)
        mfcc = librosa.feature.mfcc(y = audio, sr = sampleRate, n_mfcc= 40)
        processMfcc = numpy.mean(mfcc.T, axis = 0)
        prediction = wwModel.predict(numpy.expand_dims(processMfcc, axis = 0))
        if(prediction[:, 1] > 0.99):
            print(f"Wake word detected! Prediction percent - {prediction[:, 1]}")
            center()
        else:
            pass

if __name__ == "__main__":
    wwDetect()