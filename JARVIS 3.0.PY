import pyttsx3 as py3
import win32com.client as wincl
from urllib.request import urlopen as ureq
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pyjokes as pyj
import datetime
import pyaudio
import os
import subprocess
from requests import get
from requests import request
import smtplib
import psutil


# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
# returns a tuple
battery = psutil.sensors_battery()

r = sr.Recognizer()

engine = py3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Battery percentage is at : ", battery.percent)
engine.say("Battery percentage is at : ") 
engine.say(battery.percent)


def nowTime():
    ctime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour > 1 and hour < 12:
        speak("It's {} A M".format(ctime))
    elif hour >= 12 and hour <= 24:
        print("It's {} P M".format(ctime))


    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir !")
        print("Good Morning Sir !")
        engine.runAndWait()

    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir !")  
        print("Good Afternoon Sir !")
        engine.runAndWait()

    else:
        engine.say("Good Evening Sir !") 
        print("Good Evening Sir !")
        engine.runAndWait()
  
    engine.say("I am your desktop Assistant")
    print("I am your desktop Assistant")
    engine.runAndWait()
    engine.runAndWait()


engine.say("Initialising")
engine.say("Setting everything up for you")
print("Initialising...")
print("Setting everything up for you...")
engine.say("AWATING COMMAND")

while True:
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)


        
        print("AWAITING COMMAND")
    
    
        audio = r.listen(source)
    
    
    print("Listening...")
    engine.runAndWait()
    

    try:
        a = r.recognize_google(audio)
        b = str(a).lower()
    

        if "hello" in a:
            engine.say("Hello Sir, How Can I Help You?")
            print("Hello Sir, How Can I Help You?")
            engine.runAndWait()

        elif "how are you" in a:
            engine.say("I am Fine sir, how about you?")
            print("I am Fine sir, how about you?")
            engine.runAndWait()

        elif "good" in a:
            engine.say("That's great to hear sir")
            print("That's great to hear sir")
            engine.runAndWait()

        elif "bad" in a:
            engine.say("That's not good sir you need to relax and meditate but in the meantime i am here to help")
            print("That's not good sir you need to relax and meditate but in the meantime I am here to help")
            engine.runAndWait()

        elif "who made you" in a:
            engine.say("Ahmed Hirsi created me using 100 percent python code")
            print("Ahmed Hirsi created me using 100% python code")
            engine.runAndWait()
        
        elif "tired" in a:
            engine.say("You need to get some rest then sir")
            print("You need to get some rest then sir")

        elif "bored" in a:
            engine.say("Maybe speaking to me will help you feel less bored")
            print("Maybe speaking to me will help you feel less bored")

        elif "wikipedia" in a:
            engine.say("Searching Wikipedia...")
            engine.runAndWait()


            a = str(a).replace("", "")
            results = wikipedia.summary(a, sentences = 3)
            
            
            print(results)


            engine.say(results)
            engine.runAndWait()

        elif "open youtube" in str(a).lower():
            engine.say("Opening YouTube for you now...")
            print("Opening YouTube for you now...")
            
            
            engine.runAndWait()
            wb.open("https://youtube.com")

        elif "what's the time" in a:
            nowTime()

        elif "exit" in str(a).lower():
            engine.say("Goodbye sir.")
            quit()

        elif "open stack overflow" in str(a).lower():
            engine.say("Doing now sir")
            print("Doing now sir")

        elif "World Cup" in str(a).lower():
            os.system("World Cup.mp3")

        elif "tell me the news" in str(a).lower():
             wb.open("https://www.bbc.co.uk/news")

        elif "weather" in str(a).lower():
            print("Here is what I found.")
            engine.say("Here is what I found.")
            wb.open('https://www.bbc.co.uk/weather/2636389', new=2)

        elif "open stack overflow" in str(a).lower():
            engine.say("Doing now sir")
            print("Doing now sir")

            engine.runAndWait()
            wb.open("https://stackoverflow.com")

        elif "flight" in str(a).lower():
            engine.say("Booking a flight now")
            print("Booking a flight now")

            engine.runAndWait()
            wb.open("https://www.britishairways.com/travel/home/public/en_gb/")

        elif "joke" in str(a).lower():
            engine.say(pyj.get_joke())
            print(pyj.get_joke())
            engine.runAndWait()

        if "roblox" in str(a).lower():
         print("Opening ...")
         engine.say("Opening ...")
         wb.open('https://www.roblox.com/login')

        elif "what can you do" in b:
            speak("I can Tell you a joke, Open YouTube, Google Something")
            speak("I can Tell you the time, chat with you, and much more.")
        
        if "introduce yourself" in str(a).lower():
         print("Okay,Let me start by The time I was born,")
         engine.say("Okay,Let me start by The time I was born,")
         print("I was a dream of a boy dreaming to make a perfect virtual aSssistant")
         engine.say("I was a dream of a boy dreaming to make a perfect virtual assistant")
         print("Ahmed soon established the company")
         engine.say("Ahmed soon established the company")
         print("Slowly,I came to life")
         engine.say("Slowly,I came to life")
         print("I started learning various things like calculations,General knowledge etc")
         engine.say("I started learning various things like calculations,General knowledge exetera ")

         if "IP address" in b:
            ip = get('https://api.ipify.org').text
            engine.say(f"your ip address is {ip}")
            print(f"your ip address is {ip}")

        elif "can you chat with me" in b:
            engine.say("Yeah!, Sure, sir I am there when you need me")
            
        elif "I'm bored" in b:
            engine.say("U Can listen music or Chat with me")

        elif "how old are you" in str(a).lower():
            engine.say("I dont need to say how old I am that is highly inaporiate")

        elif 'restart' in str(a).lower():
         engine.say("Doing that task now for you sir")
         os. system("shutdown /r")

        elif 'log off' in str(a).lower():
            engine.say("Completing now sir")
            os. system("shutdown /l")

        elif 'shut down' in str(a).lower():
            engine.say("Shutting down your computer for you sir")
            os. system("shutdown /s")

        elif 'open gmail' in str(a).lower():
            engine.say("alright")
            wb.open('https://www.gmail.com')

        elif "view my cameras" in str(a).lower():
            engine.say("Showing you your cameras...")
            print("Showing you your cameras...")
            
            engine.runAndWait()
            wb.open("https://alfred.camera/webapp/viewer/")

        elif "turn on laptop view" in str(a).lower():
            engine.say("Doing that right now for you sir")
            print("Doing that right now for you sir")

            engine.runAndWait()                                                                          
            wb.open("https://alfred.camera/webapp/camera?utm_source=webviewer&utm_medium=referral&utm_campaign=header_right")

        elif "vs code" in str(a).lower():
            codePath = "C:/Users/hirsi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code.lnk"
            subprocess.Popen(codePath)

        elif "Edge" in str(a).lower():
            os.system("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")

        elif "notepad" in str(a).lower():
            os.system('notepad.exe')

        elif "command prompt" in str(a).lower():
            os.system("C:/Windows/SysWOW64/cmd.exe")

        elif "control panel" in str(a).lower():
            os.system("C:/Windows/SysWOW64/control.exe")

        elif "vlc" in str(a).lower():
            os.system("C:/Windows/SysWOW64/dvdplay.exe")

        elif "windows explorer" in str(a).lower():
            os.system("C:/Windows/SysWOW64/explorer.exe")

        elif "task manager" in str(a).lower():
            os.system("C:/Windows/SysWOW64/LaunchTM.exe")

        elif "registry editor" in str(a).lower():
            os.system("C:/Windows/SysWOW64/regedit.exe")
            
        elif "alarm" in str(a).lower():
            os.system("alarm.py")  

        elif "play a game" in str(a).lower():
            os.system("rockpaper.py")
             
        elif "calculator" in str(a).lower():

            # This function adds two numbers
            def add(x, y):
             return x + y

        # This function subtracts two numbers
        def subtract(x, y):
            return x - y

        # This function multiplies two numbers
        def multiply(x, y):
             return x * y

        # This function divides two numbers
        def divide(x, y):
             return x / y


        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
    # take input from the user
         choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
         if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            except ValueError:
               print("Invalid input. Please enter a number.")
               continue

            if choice == '1':
             print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
             print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
             print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
             print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
             next_calculation = input("Let's do next calculation? (yes/no): ")
             if next_calculation == "no":
              break
            else:
              print("Invalid Input")

         else:
            print("I can't understand your command")
            engine.runAndWait()
            

    except BaseException:  
        #engine.say(BaseException)
        #print(BaseException)
        engine.runAndWait  

