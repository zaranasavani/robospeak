import win32com.client as wincom

if __name__ == '__main__':
    speak = wincom.Dispatch(SAPI.SpVoice)
    hello = "Welcome to RoboSpeaker "
    speak.Speak(hello)
    while True:
        x = input("Enter What Do You Want To Say)
        if x=='q':
            b = "bye bye friends"
            speak.Speak(b)
            break
        speak.Speak(x)





