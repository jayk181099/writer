import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import date


r= sr.Recognizer()
f = open("demofile.txt", "a")

mytext = (" This is a format of Formal Letter.  Please Speak your Address.")
print("Your Letter is designed Below:\n")
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")
playsound('welcome.mp3')
with sr.Microphone() as source:
    audio=r.listen(source)

try:
    sound=r.recognize_google(audio)
    f.write(sound+",")
    print(r.recognize_google(audio)+",")
except:
    print("Not Recognized")



#for city and Country
mytext = (" Speak your City and Country.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcomee.mp3")
playsound('welcomee.mp3')
with sr.Microphone() as source:
    #print('Speak Your Address!')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write("\n"+sound)
    print(r.recognize_google(audio))
except:
    print("Not Recognized")

#today = date.today()
#print("\n"+today)

#This function is for Your Name
mytext = ("Now, Can you please Speak Recievers Name.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome10.mp3")
playsound('welcome10.mp3')
with sr.Microphone() as source:
    #print('Speak Your Name!')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n"+r.recognize_google(audio))
except:
    print("Not Recognized")



#This function is for Recievers Address
mytext = ("Now, Can you please Speak Recievers Address.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome11.mp3")
playsound('welcome11.mp3')
with sr.Microphone() as source:
    #print('Speak Your Name!')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print(r.recognize_google(audio))
except:
    print("Not Recognized")



#for city and Country
mytext = (" Speak Recievers City and Country.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome12.mp3")
playsound('welcome12.mp3')
with sr.Microphone() as source:
    #print('Speak Your Address!')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write(sound)
    print(r.recognize_google(audio))
except:
    print("Not Recognized")


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
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("Subject: "+r.recognize_google(audio))

except:
    print("Not Recognized")




#For the Salutation
mytext = ("Please Tell us the Salutation for the receiver")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome2.mp3")
playsound('welcome2.mp3')
with sr.Microphone() as source:
    #print('Saltutation is ')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("Dear ",r.recognize_google(audio)+",")

except:
    print("Dear Ma'am")


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
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("\t\t"+r.recognize_google(audio)+".")

except:
    print("Not Recognized")

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
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print(r.recognize_google(audio)+".")

except:
    print("Not Recognized")

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
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n"+r.recognize_google(audio)+".")

except:
    print("Not Recognized")


#Ending of Letter
mytext = ("Now speak your Name and Designation")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome7.mp3")
playsound('welcome7.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    sound = r.recognize_google(audio)
    f.write(sound)
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n\nThankYou!\nYour Sincerly\n"+r.recognize_google(audio))

except:
    pass

mytext = ("Thank you for all the Information. Your output file of Formal Letter is Saved in your Device.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome8.mp3")
playsound('welcome8.mp3')
