import pyttsx3
import datetime
import os



try:
    unnamedExcept = False
    errorDate = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M")
except Exception as Datetime_Exception:
    unnamedExcept = True
    log = open(f"Error Log/Unlabeled Errors/Datetime Exception.txt", "w")
    log.write(str(Datetime_Exception))
    log.close()
    exceptionsCount = 0
    for errorLog in os.scandir("Error Log/Unlabeled Errors"):
        if errorLog.is_file():
            exceptionsCount += 1
    errorDate = f"Unnamed Exception {exceptionsCount}"

engine = pyttsx3.init()

#voice 8 = bells, 3 = french, 0 = cursed, using = 14
#possibility for ru speak = 19
def speak(audio):
    try:
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[14].id)
        
        engine.setProperty("rate", 170)
        engine.say(audio)
        engine.runAndWait()
    except Exception as Speech_Exception:
        if(unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Speech_Exception))
        log.close()
        print(f"Error with speech! {Speech_Exception}. I created an error file.")

def ruSpeak(audio):
    try:
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[19].id)
        
        engine.setProperty("rate", 170)
        engine.say(audio)
        engine.runAndWait()
    except Exception as Speech_Exception:
        if(unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Speech_Exception))
        log.close()
        print(f"Error with ruspeech! {Speech_Exception}. I created an error file.")


