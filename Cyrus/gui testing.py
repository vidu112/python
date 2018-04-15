from turtle import *
import time
from datetime import datetime
import speech_recognition as sr
import os
from gtts import gTTS
from translate import translator
# Record Audio
r = sr.Recognizer()
lan='en'
def polygon(sides,lenght):
    for x in range(sides):
        forward(100)
def say(text,lan):
        if lan!='en':
            text=translator('en',lan,text)
        tts = gTTS(text=text, lang=lan)
        tts.save("good.mp3")
        os.system("good.mp3")
def codetype(address):
   with open(address,'r') as rd:
      c=0
      rd.seek(0)
      lent=rd.readlines()
      for le in lent: 
         c=c+1
         print(le)
      c=c+1   
      co=str(c)
      code=(('0'*(4-len(co)))+co)
   return(code)
def new_question(x,y):
   with open('question.txt','a') as fa:
       fa.write(x)
       lent=codetype('question.txt')
       fa.write(lent+'\n')
       with open('answers.txt','a') as aa:
        show_text('pls enter anser for your question',line=y+1)   
        ans=input('pls enter anser for your question')
        tts = gTTS(ans,'en')
        tts.save(+".mp3")
        aa.write(lent+ans+'\n')
       
def found(ques,c):
    #print(ques)
    x=len(ques)-4
    code=ques[x:]
    #print(code)
    with open('answers.txt') as ans:
        answer=ans.readline()
        answer=answer.strip()
        while (len(answer)>0):  
          if (answer[:4] == code):
            time.sleep(0)
            print(answer[4:])
            show_text(answer[4:],c+2)
            #tts = gTTS
            #tts.save(code+".mp3")
            os.system(code+".mp3")
            break
          else:
           answer=ans.readline()
           answer=answer.strip()
           
       # print('end')   
def aval(c,question,x):
   
   with open('question.txt') as f:
     found_ques='false'
     line=f.readline()
     line=line.strip()
     while (len(line)>0): 
        if (line[:len(line)-4] == question):
      #      print('found')
            found_ques='true'
            found(line,x)
            break
        else:
           line=f.readline()
           line=line.strip()
     #print('endo')
     if found_ques=='false':
            new_question(question,x+1)
         

     
     up()
def show_text(text, line=0):
    line = 16 * line
    goto(0,250 - line)
    write(text, align="center", font=("Courier", 15, "bold"))

def main():
  peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")
  reset()
  Screen()
  show_text('LOADING PLS WAIT')
  tracer(False)
  shape("triangle")
  f =   0.793402
  phi = 9.064678
  s = 5
  c = 1
  # create compound shape
  sh = Shape("compound")
  for i in range(10):
        shapesize(s)
        p =get_shapepoly()
        s *= f
        c *= f
        tilt(-phi)
        sh.addcomponent(p, (c, 0.25, 1-c), "black")
  register_shape("multitri", sh)
  # create dancers
  shapesize(1)
  shape("multitri")
  pu()
  setpos(0, -200)
  dancers = []
  for i in range(180):
        fd(7)
        tilt(-4)
        lt(2)
        update()
        if i % 12 == 0:
          dancers.append(clone())
  home()
  clearscreen()
  
  for c in range(200):
    
      
    up()
    goto(-320,-195)
    width(50)
    x=c*4
    show_text('enter question or enter end to end',line=x)  
    #question=input('enter question ')
    with sr.Microphone() as source:
      print("Say something!")
      question=input('sdfg')
      #audio = r.listen(source)
      print('heard')
# Speech recognition using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
       
      # question=r.recognize_google(audio)
       print("You said: " + question)
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    question=question.lower()
    #if (question.find('hey cyrus')!=-1):
     #show_text(question,line=x+1)
     #question=input('sdfg')
     #with sr.Microphone() as source:
      #print("Say something!")   
      #audio = r.listen(source)
      #question=r.recognize_google(audio)
    #print('heard')
    #print("You said: " + question)
    print('heard')
    if (question.find('end')!=-1):
        break
    elif (question.find('music')!=-1):
        os.system("vidu.mp3")
    elif (question.find('time')!=-1):
        print(str(datetime.now())[11:])
        show_text(question,line=x)
        x=len(str(datetime.now()))-8
        say(str(datetime.now())[11:x],lan)
    elif (question.find('date')!=-1):
        print(str(datetime.now())[11:])
    else:
       aval(c,question,x) 
  
           
    

##    for pcolor in peacecolors:
##        color(pcolor)
##        down()
##        forward(500)
##        up()
##        backward(500)
##        left(90)
##        forward(66)
##        right(90)
    
instructions1 = " "
instructions2 = "spacebar to quit"
if __name__ == "__main__":
    main()
    mainloop()
