import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import date


r= sr.Recognizer()

mytext = (" This is a format of an Application.  Please Speak the Designation for the Reciever.")
print("Your Application is designed Below:\n")
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")
playsound('welcome.mp3')
with sr.Microphone() as source:
    audio=r.listen(source)

try:
    print("To,\nThe ",r.recognize_google(audio)+",")
except:
    print("Sorry, Can't Understand")



#For Subject of Letter
mytext = ("\nNow, speak the subject of the letter.\n")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome3.mp3")
playsound('welcome3.mp3')
with sr.Microphone() as source:
    #print('Subject is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("Subject: "+r.recognize_google(audio))

except:
    pass




#For the Salutation
mytext = ("Please Speak the Relation or Name of the receiver")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome2.mp3")
playsound('welcome2.mp3')
with sr.Microphone() as source:
    #print('Saltutation is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("Dear ",r.recognize_google(audio)+",")

except:
    pass


#First Intro Para
mytext = ("Now Speak a short Introduction Paragraph for your letter")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome4.mp3")
playsound('welcome4.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("\t\t"+r.recognize_google(audio)+".")

except:
    pass

#Miidle Paragraph
mytext = ("Now provide more details for your letter")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome5.mp3")
playsound('welcome5.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print(r.recognize_google(audio)+".")

except:
    pass

#Closing Para of Letter
mytext = ("Now provide the closing for your letter")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome6.mp3")
playsound('welcome6.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n"+r.recognize_google(audio)+".")

except:
    pass


#Ending of Letter
mytext = ("Now speak your Name")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome7.mp3")
playsound('welcome7.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n\nThankYou!\nYour Sincerly\n"+r.recognize_google(audio))

except:
    pass

mytext = ("Thank you for all the Information. Your output file of Formal Letter is Saved in your Device.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome8.mp3")
playsound('welcome8.mp3')
