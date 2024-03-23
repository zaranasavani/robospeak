
import win32com.client as wincom

if __name__=='__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
    hello = "welcome to robospeak by zarana"
    speak.Speak(hello)
    while True:

        x=input("Enter what you want to say:")
        if x=="q":
            b="bye bye frieds"
            break

print("the end.....")



