import win32com.client as wincom

if __name__ == '__main__':
    s = "Welcome to RoboSpeaker "
    while True:
        speak = wincom.Dispatch(SAPI.SpVoice)
        x = input("Enter What Do You Want To Say)
        if x=='q':
            b = "bye bye friends"
            speak.Speak(b)
            break
        speak.Speak(x)





