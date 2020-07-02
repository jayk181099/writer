import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import date


r= sr.Recognizer()
print("Your SRS is designed Below:\n")

mytext = (" This is a format of a Project SRS.  Please Speak your College\Institution Name.")
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio.mp3")
playsound('SRSAudio.mp3')
with sr.Microphone() as source:
    audio=r.listen(source)

try:
    print("\t\t\t\t\t\t"+"\033[1m"+r.recognize_google(audio)+"\033[0m")
except:
    pass



#for city and Country
mytext = ("Speak your City and Country of College.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudioe.mp3")
playsound('SRSAudioe.mp3')
with sr.Microphone() as source:
    #print('Speak Your Address!')
    audio=r.listen(source)

try:
    print("\t\t\t\t\t\t\t\t"+r.recognize_google(audio))
except:
    pass

#today = date.today()
#print("\n"+today)

#This function is for Your Name
mytext = ("Now, Can you please Speak Recievers Name.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio10.mp3")
playsound('SRSAudio10.mp3')
with sr.Microphone() as source:
    #print('Speak Your Name!')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n"+r.recognize_google(audio))
except:
    pass



#This function is for Recievers Address
mytext = ("Now, Can you please Speak Recievers Address.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio11.mp3")
playsound('SRSAudio11.mp3')
with sr.Microphone() as source:
    #print('Speak Your Name!')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print(r.recognize_google(audio))
except:
    pass



#for city and Country
mytext = (" Speak Recievers City and Country.")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio12.mp3")
playsound('SRSAudio12.mp3')
with sr.Microphone() as source:
    #print('Speak Your Address!')
    audio=r.listen(source)

try:
    print(r.recognize_google(audio))
except:
    pass


#For Subject of Letter
mytext = ("\nNow, speak the subject of the letter.\n")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio3.mp3")
playsound('SRSAudio3.mp3')
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

myobj.save("SRSAudio2.mp3")
playsound('SRSAudio2.mp3')
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

myobj.save("SRSAudio4.mp3")
playsound('SRSAudio4.mp3')
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

myobj.save("SRSAudio5.mp3")
playsound('SRSAudio5.mp3')
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

myobj.save("SRSAudio6.mp3")
playsound('SRSAudio6.mp3')
with sr.Microphone() as source:
    #print('Content is ')
    audio=r.listen(source)

try:
    #print("You just said:\n"+r.recognize_google(audio))
    print("\n"+r.recognize_google(audio)+".")

except:
    pass


#Ending of Letter
mytext = ("Now speak your Name and Designation")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("SRSAudio7.mp3")
playsound('SRSAudio7.mp3')
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

myobj.save("SRSAudio8.mp3")
playsound('SRSAudio8.mp3')
