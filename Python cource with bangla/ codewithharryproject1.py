# print()

# print("======================================================Code with Harry Project no : 1 ============================================================")


# print()















import pyttsx3

import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

print(voices[1].id)    #>>>>>>>>>>>>> "0" is the man voice and "1" is the woman voice  <<<<<<<<<<<<<<<<<<<<<<<<

engine.setProperty('voices',voices[1].id)








def speak():

    # pass
    engine.say(audio)
    engine.runAndWait()


def wishme():              #>>>>>>>>> line; 12 use korer <<<<<<<<<<<<<<<<<  
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("goood morning!")
    elif hour >=12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may i help You? sir")




if __name__== "__main__":
    # speak("harry is a good boy")
    wishme()

    
















