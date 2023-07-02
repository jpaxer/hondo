import datetime
import random
import playsound
import pyjokes
import os
import speech_recognition
import re
import webbrowser
try:
    import pywhatkit
except:
    pass
import wikipedia
import pyautogui
from word2number import w2n
from num2words import num2words
from builtins import len
import clipboard
import inflect
from difflib import get_close_matches
from newsapi import NewsApiClient
import requests
import math

newsAPI = "6111de61fbe94349ae1c50e692069ee3"
weatherAPI = "b90e5c1ae8cefcf996a40b239477d26c"

from Engine import speak, ruSpeak, errorDate, unnamedExcept

#CHECK IF CONNECTED TO THE INTERNET
def connectionCheck():
    try:
        requests.get("https://google.com")
        return True
    except requests.RequestException:
        speak("Error while connecting to the Internet. Make sure you are connected to the Internet! Some tasks such as YouTube, News, and Weather may not work.")
        return False

#WORD TO NUMBER
def allWordToNum(sentence):
    sentenceS = sentence.split()
    for i in range(len(sentenceS)):
        try:
            a = int(sentenceS[i])               
        except:
            try:
                sentenceS[i] = w2n.word_to_num(sentenceS[i])
                sentenceS[i] = str(sentenceS[i])
            except:
                pass
    sentence = ' '.join(sentenceS)
    return sentence

#NUMBER TO WORDS
def allNumToWords(sentence):
    sentenceS = sentence.split()
    for i in range(len(sentenceS)):
        try:
            a = int(sentenceS[i])
            sentenceS[i] = num2words(sentenceS[i])
            sentenceS[i] = str(sentenceS[i])               
        except:
            pass
    sentence = ' '.join(sentenceS)
    return sentence

#SPEECH RECOGNITION
def speechRecognition():
    try:
        recognition = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as  source:
            recognition.adjust_for_ambient_noise(source)
            recognition.dynamic_energy_threshold = False
            recognition.energy_threshold = 400
            print("Listening...")
            try:
                audio = recognition.listen(source, timeout = 5)
            except Exception:
                pass
            try:
                print("Recognizing...")
                sentence = recognition.recognize_google(audio, language = "en-US")
            except Exception:
                pass
            finSentence = allNumToWords(sentence)
            return finSentence
    except Exception as Mic_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Mic_Exception))
        log.close()
        speak(f"There was an error, {Mic_Exception}")

#GIVE MESSAGE ON ERROR
def Error_Occurred(exception, message):
    if (message != ""):
        speak(message)
    else:
        speak(f"There was an error, {exception}. Please fix the error and/or try again later.")

#TIME##
def currentTime():
    try:
        getTime = datetime.datetime.now().strftime("%H:%M")
        answers = [
            f"It's {getTime}",
            f"It is {getTime}",
            f"It's currently {getTime}",
            f"It is currently {getTime}",
            f"Right now it's {getTime}",
            f"The time is {getTime}",
            f"The time is currently {getTime}",
            f"The current time is {getTime}",
            f"The time is currently {getTime}"
        ]
        speak(random.choice(answers))
    except Exception as Time_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Time_Exception))
        log.close()
        Error_Occurred(Time_Exception,"")

#DAY##
def currentDay():
    try:
        getDay = datetime.datetime.now().strftime("%A")
        answers = [
                f"It's {getDay}",
                f"It is {getDay}",
                f"It's {getDay} today",
                f"Today is {getDay}",
                f"The day is {getDay}",
                f"It is {getDay} today",
                f"Today's date is {getDay}"
        ]
        speak(random.choice(answers))
    except Exception as Day_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Day_Exception))
        log.close()
        Error_Occurred(Day_Exception,"")

#MONTH##
def currentMonth():
    try:
        getMonth = datetime.datetime.now().strftime("%B")
        answers = [
            f"It's {getMonth}",
            f"It is {getMonth}",
            f"The month is {getMonth}",
            f"The current month is {getMonth}",
            f"This month is {getMonth}",
            f"Right now it's {getMonth}",
            f"Right now it is {getMonth}"
            f"It's currently {getMonth}"
        ]
        speak(random.choice(answers))
    except Exception as Month_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Month_Exception))
        log.close()
        Error_Occurred(Month_Exception,"")

#DATE##
def currentDate():
    try:
        getDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
        answers = [
            f"It's {getDate}",
            f"Today is {getDate}",
            f"The date is {getDate}",
            f"The current date is {getDate}",
            f"Today's date is {getDate}",
            f"Today it is {getDate}"
        ]
        speak(random.choice(answers))
    except Exception as Date_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Date_Exception))
        log.close()
        Error_Occurred(Date_Exception,"")

#COINFLIP GAME##
def coinFlip():
    try:
        answers = [
            "Flipping now...",
            "Tossing the coin...",
            "Ok, i'll flip it now"
        ]
        speak(random.choice(answers))
        playsound.playsound("Sound Effects/coinFlip.mp3")
        coinSides = ["heads", "tails"]
        result = random.choice(coinSides)
        answerResult = [
            f"{result}!",
            f"It's {result}!",
            f"It landed on {result}!"
        ]
        speak(random.choice(answerResult))
    except Exception as Coinflip_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Coinflip_Exception))
        log.close()
        Error_Occurred(Coinflip_Exception,"")

#DICEROLL GAME##
def diceRoll():
    try:
        answers = [
            "Ok, i'll roll now.",
            "Rolling now...",
            "Give me a second to roll it.",
            "Let me roll it real quick here...",
            "Rolling the dice..."
        ]
        speak(random.choice(answers))
        playsound.playsound("Sound Effects/Diceroll.mp3")
        dicePoints = ["1", "2", "3", "4", "5", "6"]
        result = random.choice(dicePoints)
        answerResult = [
            f"I rolled a {result}!",
            f"It's {result}!",
            f"It's a {result}!",
            f"I rolled {result}!"
        ]
        speak(random.choice(answerResult))
    except Exception as Dice_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Dice_Exception))
        log.close()
        Error_Occurred(Dice_Exception,"")

#JOKES##
def Jokes():
    try:
        jokesList = [
            "What did one ocean say to the other ocean? Nothing, it just waved.",
            "Did you hear about the first restaurant on the moon? It had great food but no atmosphere.",
            "What do dentists call their x-rays? Tooth pics!",
            "There\'s a fine line between a numerator and a denominator. \(...Only a fraction of people will get this joke.\)",
            "What do you call a deer with no eyes? I got no eye deeeer. What do you call a deer with no eyes or legs? I STILL, got no eye deeeer.",
            "Two men walk into a bar, the third one ducks",
            "Do you want to hear a construction joke? Sorry, I'm still working on it.",
            "Did you hear about the fire at the circus? It  was in tents!",
            #"What does a nosy pepper do? It gets jalapeño buisiness.",
            "Why should you never trust stairs? They\'re always up to something.",
            "When does a joke become a dad joke? When is becomes apparent.",
            "Why did the bullet end up loosing his job? He got fired.",
            "I entered ten puns in a contest to see which would win. No pun in ten did.",
            "How do you measure a snake? In inches-they don't have feet.",
            "Where does a waitress with only one leg work? I hop.",
            "What does a house wear? Address!",
            "Why is Peter Pan always flying? Because he Neverlands. \(I love this joke because it never grows old.\)",
            "You heard the rumor going around about butter? Never mind, I shouldn't spread it.",
            "Two windmills are standing on a wind farm. One asks, \'What's your favorite kind of music?\' The other replies, \'I'm a big metal fan.\'"
        ]
        speak(random.choice(jokesList))
    except Exception as Jokes_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Jokes_Exception))
        log.close()
        Error_Occurred(Jokes_Exception,"")

#PROGRAMMING JOKES##
def proJokes ():
    try:
        speak(pyjokes.get_joke())
    except Exception as proJokes_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(proJokes_Exception))
        log.close()
        Error_Occurred(proJokes_Exception,"")

#BLACKJACK##
def blackjack():
    
    try:
        cards = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen", "Ace",
            2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen", "Ace",
            2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen", "Ace",
            2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen", "Ace"
        ]
        playerPlaying = True
        dealerPlaying = True
        playerHand = []
        dealerHand = []

        if(os.stat("Notes/Blackjack Tokens.txt").st_size == 0):
            speak("You don't have any tokens, two tokens were added.")
            with open("Notes/Blackjack Tokens.txt", "w") as balance:
                defaultTokens = 2
                balance.write(str(defaultTokens))
        else:
            pass
        with open("Notes/Blackjack Tokens.txt", "r") as balance:
            tokens = int(balance.read())
        if(tokens <= 0):
            speak("You don't have any tokens, two tokens were added.")
            with open("Notes/Blackjack Tokens.txt", "w") as balance:
                tokens = 2
                balance.write(str(tokens))
        def playerWon():
            with open("Notes/Blackjack Tokens.txt", "w") as balance:
                tokensWon = tokens + bet
                balance.write(str(tokensWon))
        def bettedTokens():
            with open("Notes/Blackjack Tokens.txt", "w") as balance:
                tokensLeft = tokens - bet
                balance.write(str(tokensLeft))
        def playerPushed():
            with open("Notes/Blackjack Tokens.txt", "w") as balance:
                tokensPayback = tokens
                balance.write(str(tokensPayback))

        def dealCard(drawnCard):
            card = random.choice(cards)
            drawnCard.append(card)
            cards.remove(card)
        def countScore(drawnCard):
            score = 0
            ace11 = 0
            for card in drawnCard:
                if(card in range(11)):
                    score += card
                elif(card in ["Jack", "Queen", "King"]):
                    score += 10
                else:
                    score += 11
                    ace11 += 1
            while(ace11 and score > 21):
                score -= 10
                ace11 -= 1
            return score
        def showDealerHand():
            if(len(dealerHand) == 2):
                return dealerHand[0]
            elif(len(dealerHand) > 2):
                return dealerHand[0], dealerHand[1]
        for _ in range(2):
            dealCard(dealerHand)
            dealCard(playerHand)

        while True:
            speak(f"Place your bet, you have {tokens} tokens.")
            bet = int(input("What amount do you want to bet?: "))
            if(bet > tokens):
                speak(f"You only have {tokens} tokens. That isn't enough to bet {bet} tokens.")
            elif(bet <= 0):
                speak(f"You can't bet zero or less. You have to bet more that your current bet of {bet} tokens.")
            else:
                speak(f"You successfully bet {bet} tokens! Let's play!")
                bettedTokens()
                break
        speak(f"Dealer shows {showDealerHand()}.")
        while(playerPlaying or dealerPlaying):
            if(playerPlaying):
                hitOrStand = input(f"You have {countScore(playerHand)}. Hit or stand?: ")
            if(countScore(dealerHand) > 16):
                dealerPlaying = False
            else:
                dealCard(dealerHand)
            if(hitOrStand == "stand"):
                playerPlaying = False
            else:
                dealCard(playerHand)
            if(countScore(playerHand) >= 21):
                break
            elif(countScore(dealerHand) >= 21):
                break
        if(countScore(dealerHand) == countScore(playerHand)):
            speak("You were pushed.")
            playerPushed()
        elif(countScore(playerHand) == 21):
            speak(f"Blackjack! You won {bet} tokens!")
            playerWon()
        elif(countScore(dealerHand) == 21):
            speak(f"Dealer has blackjack! You lost {bet} tokens.")
        elif(countScore(playerHand) > 21):
            speak(f"You busted! You lost {bet} tokens.")
        elif(countScore(dealerHand) > 21):
            speak(f"Dealer busted! You won {bet} tokens!")
            playerWon()
        elif((21 - countScore(dealerHand)) < (21 - countScore(playerHand))):
            speak(f"Dealer has {countScore(dealerHand)}. You lost {bet} tokens.")
        elif((21 - countScore(dealerHand)) >  (21 - countScore(playerHand))):
            speak(f"Dealer has {countScore(dealerHand)}. You won {bet} tokens.")
            playerWon()
    except Exception as Blackjack_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Blackjack_Exception))
        log.close()
        Error_Occurred(Blackjack_Exception,"")

#REPEAT AFTER ME
def repeatMe(sentence):
    try:
        replaceWords = ["repeat ", "me "]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        repeat = str(replacement)
        speak(repeat)
    except Exception as RepeatMe_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(RepeatMe_Exception))
        log.close()
        Error_Occurred(RepeatMe_Exception,"")

#GOOGLE SEARCH
def googleSearch(sentence):
    try:
        replaceWords = ["google ", "search ", "search google for ", "google for", "google search"]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        speak(f"Searching for {replacement}...")
        webbrowser.open(f"https://www.google.com/search?q={replacement}")
    except Exception as Search_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Search_Exception))
        log.close()
        Error_Occurred(Search_Exception,"")

#YOU.COM SEARCH
def youSearch(sentence):
    try:
        replaceWords = ["you.com", "search ", "search you for ", "search you.com for"]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        speak(f"Searching for {replacement}...")
        webbrowser.open(f"https://www.you.com/search?q={replacement}")
    except Exception as YouSearch_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(YouSearch_Exception))
        log.close()
        Error_Occurred(YouSearch_Exception,"")

#YOUTUBE
def playOnYt(sentence):
    try:
        replaceWords = ["play ", "on youtube"]
        replaceWith = ""
        videoName = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        speak(f"Playing {videoName} on YouTube.")
        pywhatkit.playonyt(videoName)
    except Exception as playOnYt_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(playOnYt_Exception))
        log.close()
        Error_Occurred(playOnYt_Exception,"")


#WIKEPEDIA
def wikiSearch(sentence):
    try:
        replaceWords = ["what ", "Who ", "when ", "is ", "was ", "were ", "about "]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        findOnWiki = wikipedia.summary(replacement, sentences = 2)
        speak(f"According to Wikepedia, {findOnWiki}.")
    except Exception as Wiki_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Wiki_Exception))
        log.close()
        Error_Occurred(Wiki_Exception,"")

#SCREENSHOTS
def screenshots():
    try:
        nameOfSS = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M")
        nameOfSS = f"Screenshots/{nameOfSS}.png"
        image = pyautogui.screenshot(nameOfSS)
        speak("A screenshot has been taken.")
        image.show()
    except Exception as SS_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(SS_Exception))
        log.close()
        Error_Occurred(SS_Exception,"")

#CALCULATOR
def calculator(sentence):
    try:
        sentence = allWordToNum(sentence)
        replaceWords = ["calculate ", "solve ", "compute ", "what's ", "what ", "is ", "by ", "calculate", "solve", "compute", "what's", "is", "and ", "what"]
        replaceWith = ""
        sentence = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        operator = sentence.split()
        print(str(operator))
        #operator.remove("calculate")
        if (operator[1] == "+" or operator[1] == "plus"):
            answerAdd = int(operator[0]) + int(operator[2])
            speak(f"{operator[0]} plus {operator[2]} equals {answerAdd}.")
        elif (operator[1] == "-" or operator[1] == "minus"):
            answerSubstract = int(operator[0]) - int(operator[2])
            speak(f"{operator[0]} minus {operator[2]} equals {answerSubstract}.")
        elif (operator[1] == "*" or operator[1] == "times" or operator[1] == "x"):
            answerMultiply = int(operator[0]) * int(operator[2])
            speak(f"{operator[0]} times {operator[2]} equals {answerMultiply}.")
        elif (operator[1] == "/" or operator[1] == "divide" or operator[1] == "÷" or operator[1] == "divided"):
            try:
                answerDivide = int(operator[0]) / int(operator[2])
                speak(f"{operator[2]} goes into {operator[0]} {answerDivide} times.")
            except Exception:
                speak("Sorry, you cannot divide by zero.")
        else:
            try:
                speak(f"Sorry, {operator[1]} not recognized as a valid operator.")
            except:
                speak("Sorry, couldn't find the operator.")
    
    except Exception as Calc_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Calc_Exception))
        log.close()
        Error_Occurred(Calc_Exception,"")

#VOLUME CONTROL
def volUp():
    for _ in range(3):
        pyautogui.press(u'KEYTYPE_SOUND_UP')

def volDown():
    for _ in range(3):
        pyautogui.press(u'KEYTYPE_SOUND_DOWN')

def muteVol():
    pyautogui.press(u'KEYTYPE_MUTE')

#READ THIS
def readThis():
    text = clipboard.paste()
    speak(str(text))

#OPEN/CLOSE APP
def openApp(sentence):
    try:
        apps = ["App Store", "Automator", "Blender", "Blockbench", "Books", "Calculator", "Calendar", 
        "CG/CGI Software", "Unity", "Unity Bug Reporter", "Chess", "Clock", "Contacts", "Dictionary", 
        "FaceTime", "Find My", "Font Book", "Home", "Image Capture", "iMovie", "krita", "Launchpad", 
        "Mail", "Malwarebytes", "Mapcraft", "Maps", "Messages", "Minecraft", "Mission Control", "Music", 
        "News", "Notes", "Original Prusa Drivers", "Objects", "Pronterface", "PrusaSlicer", "Photo Booth", 
        "Photos", "Podcasts", "Preview", "PrusaSlicer", "Python 3.11", "IDLE", "Python Launcher", 
        "QuickTime Player", "Raspberry Pi Imager", "Reminders", "Safari", "Shortcuts", "Siri", "Stickies", 
        "Stocks", "System Settings", "TextEdit", "Time Machine", "TV", "Typing Instructor for Kids Gold",
         "Unity Hub", "Utilities", "Activity Monitor", "AirPort Utility", "Audio MIDI Setup", 
         "Bluetooth File Exchange", "Boot Camp Assistant", "ColorSync Utility", "Console", 
         "Digital Color Meter", "Disk Utility", "Grapher", "Keychain Access", "Migration Assistant", 
         "Screenshot", "Script Editor", "System Information", "Terminal", "VoiceOver Utility", 
         "Visual Studio", "Visual Studio Code", "Voice Memos", "Weather", "zoom.us"]
        replaceWords = ["open ", "start ", "start up ", "please ", "can you "]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        #find closest match for app name
        app = get_close_matches(replacement, apps, 1)
        #convert closest match from list to string
        def listToString(s): 
    
            str1 =""
    
            return (str1.join(s))
        replaceName = ["[", "]", "\'"]
        app = listToString(app)
        appName = re.sub("|".join(sorted(replaceName, key = len, reverse = True)), replaceWith, app)
        os.system(f"open -a \"{appName}\"")
    
    except Exception as openApp_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(openApp_Exception))
        log.close()
        Error_Occurred(openApp_Exception,"")

def closeApp(sentence):
    try:
        apps = ["App Store", "Automator", "Blender", "Blockbench", "Books", "Calculator", "Calendar", 
        "CG/CGI Software", "Unity", "Unity Bug Reporter", "Chess", "Clock", "Contacts", "Dictionary", 
        "FaceTime", "Find My", "Font Book", "Home", "Image Capture", "iMovie", "krita", "Launchpad", 
        "Mail", "Malwarebytes", "Mapcraft", "Maps", "Messages", "Minecraft", "Mission Control", "Music", 
        "News", "Notes", "Original Prusa Drivers", "Objects", "Pronterface", "PrusaSlicer", "Photo Booth", 
        "Photos", "Podcasts", "Preview", "PrusaSlicer", "Python 3.11", "IDLE", "Python Launcher", 
        "QuickTime Player", "Raspberry Pi Imager", "Reminders", "Safari", "Shortcuts", "Siri", "Stickies", 
        "Stocks", "System Settings", "TextEdit", "Time Machine", "TV", "Typing Instructor for Kids Gold",
         "Unity Hub", "Utilities", "Activity Monitor", "AirPort Utility", "Audio MIDI Setup", 
         "Bluetooth File Exchange", "Boot Camp Assistant", "ColorSync Utility", "Console", 
         "Digital Color Meter", "Disk Utility", "Grapher", "Keychain Access", "Migration Assistant", 
         "Screenshot", "Script Editor", "System Information", "Terminal", "VoiceOver Utility", 
         "Visual Studio", "Visual Studio Code", "Voice Memos", "Weather", "zoom.us"]
        replaceWords = ["close ", "quit ", "stop ", "please ", "can you ", "shut down"]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        #find closest match for app name
        app = get_close_matches(replacement, apps, 1)
        #convert closest match from list to string
        def listToString(s): 
    
            str1 =""
    
            return (str1.join(s))
        replaceName = ["[", "]", "\'"]
        app = listToString(app)
        appName = re.sub("|".join(sorted(replaceName, key = len, reverse = True)), replaceWith, app)
        os.system(f"osascript -e 'quit app \"{appName}\"'")
    except Exception as closeApp_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(closeApp_Exception))
        log.close()
        Error_Occurred(closeApp_Exception,"")

#REMINDERS
def createReminder(sentence):
    try:
        replaceWords = ["remind ", "me ", "set "]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        with open("Notes/Reminders.txt", "w") as note:
            note.write(str(replacement))
            speak("Reminder created.")
    except Exception as crRem_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(crRem_Exception))
        log.close()
        Error_Occurred(crRem_Exception,"")

def remind():
    with open("Notes/Reminders.txt", "r") as note:
        speak(f"Your reminder is: {note.readlines()}. Clearing it now...")
    with open("Notes/Reminders.txt",'w') as delete:
        pass

#NEWS
def currentNews(sentence):
    try:
        replaceWords = ["please ", "tell ", "me ", "what ", "is ", "news ", "about ", "latest "]
        replaceWith = ""
        replacement = re.sub("|".join(sorted(replaceWords, key = len, reverse = True)), replaceWith, sentence)
        topic = replacement
        news = NewsApiClient(api_key = newsAPI)
        getNews = news.get_everything(q = topic, language = "en", page_size = 4)
        latestNews = []
        inflecter = inflect.engine()
        for everyHeadline in getNews["articles"]:
            latestNews.append(everyHeadline["title"])
        for number in range(len(latestNews)):
            newsEnumeration = inflecter.number_to_words(inflecter.ordinal(number + 1))
            listOfNews = newsEnumeration, latestNews[number]
            speak(str(listOfNews))
        speak("That's all for now.")
    except Exception as News_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(News_Exception))
        log.close()
        Error_Occurred(News_Exception,"")

#WEATHER
def getWeather(weatherAPI):
    try:
        openWeatherMap = f"https://api.openweathermap.org/data/2.5/weather?lat=37.221340&lon=-121.979640&appid={weatherAPI}&units=imperial"
        sendRequest = requests.get(openWeatherMap).json()
        temperature = math.floor(sendRequest["main"]["temp"])
        feelsLike = math.floor(sendRequest["main"]["feels_like"])
        humidity = math.floor(sendRequest["main"]["humidity"])
        windSpeed = math.floor(sendRequest["wind"]["speed"])
        description = sendRequest["weather"][0]["description"]
        return {
            "temperature": temperature,
            "feelsLike": feelsLike,
            "humidity": humidity,
            "windSpeed": windSpeed,
            "description": description
        }

    except Exception as Weather_Exception:
        if (unnamedExcept == True):
            log = open(f"Error Log/Unlabeled Errors/{errorDate}.txt", "w")
        else:
            log = open(f"Error Log/Labeled Errors/{errorDate}.txt", "w")
        log.write(str(Weather_Exception))
        log.close()
        Error_Occurred(Weather_Exception,"")

def weather():
    currentWeather = getWeather(weatherAPI)
    temperature = currentWeather["temperature"]
    feelsLike = currentWeather["feelsLike"]
    humidity = currentWeather["humidity"]
    windSpeed = currentWeather["windSpeed"]
    description = currentWeather["description"]
    if (temperature % 10 == 1):
        degreesStrTemp = "degree"
    else:
        degreesStrTemp = "degrees"
    if (feelsLike % 10 == 1):
        degreesStrFeel = "degree"
    else:
        degreesStrFeel = "degrees"
    if (windSpeed % 10 == 1):
        wsStr = "mile"
    else:
        wsStr = "miles"
    speak(f"the temperature is {temperature} {degreesStrTemp} fahrenheight, "
    f"and it feels like {feelsLike} {degreesStrFeel}.,"
    f"The wind speed is {windSpeed} {wsStr} per hour, with {humidity} percent humidity.,"
    f"Current conditions are: {description}.")

#ROUTINES
def startMyDay():
    speak("Hello sir. ")
    currentDate()
    currentTime()
    weather()

def workMode():
    pywhatkit.playonyt("study with me with lofi music | Pomodoro (25 min study x 5 min rest)")

#ru mode
def ruMode():
    speak("Activating Russian mode... Removing fun... Installing piano practice... Making apartments lumpy and boring")
    ruSpeak("Russian mode activated!")
