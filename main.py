
# import os
#
# if __name__ == '__main__':
#     s = "Welcome to RoboSpeaker "
#     command1 = f"PowerShell -Command "f"Add-Type -AssemblyName System.Speech;(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
#     os.system(command1)
#     while True:
#         x = input("Enter What Do You Want To Say")
#         if x=='q':
#             b = "bye bye friends"
#             command2 = f"PowerShell -Command "f"Add-Type -AssemblyName System.Speech;(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{b}');"
#             os.system(command2)
#             break
#
#         command = f"PowerShell -Command "f"Add-Type -AssemblyName System.Speech;(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
#         os.system(command)


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



