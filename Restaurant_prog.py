import speech_recognition as sr
from speech_recognition import UnknownValueError
import vlc
import gtts
import time
import pandas as pd
import numpy as np
import smtplib
items=pd.read_excel("/home/rajkumar/Desktop/machine_learning_training/restaurant/food_menu_items.xlsx",4)
order1=[]
idn=[]
cn=[]
r=sr.Recognizer()
def order():
    bill=0
    while(1):
        text=''
        f=np.array(items['Id'])
        f1=f.tolist()
        c=np.array(items['cost'])
        c1=c.tolist()
        n=np.array(items['items'])
        n1=n.tolist()
        with sr.Microphone() as Source:
            print('listening')
            audio=r.listen(Source)
            print('Replying')
            try:
                data1=r.recognize_google(audio)
            except UnknownValueError:
                print('I am waiting for your order')
            if data1=='confirm order':
                for con in order1:
                    m=order1.index(con)
                    text=text+str(idn[m])+' '+con+' '+str(cn[m])+'\n'
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login('teatimecomedy@gmail.com','Raj Kumar')
                server.sendmail('teatimecomedy@gmail.com','princerajkumar1431@gmail.com',text)
                server.close()
                print('Order Confirmed')
                player=vlc.MediaPlayer('order_confirmed.mp3')
                player.play()
                time.sleep(2)
                player.stop()
                break
            else:
                try:
                    dd1=float(data1)
                except:
                    print('Sorry sir!please Check the id again')
                    print(2)
                if dd1 in f1:
                    m=f1.index(dd1)
                    order1.append(n1[m])
                    idn.append(dd1)
                    cn.append(c1[m])
                    bill=bill+int(c1[m])
                    print(dd1,' Added')
                elif dd1==0.0:
                    print('Changing Type')
                    player=vlc.MediaPlayer('change_type.mp3')
                    player.play()
                    time.sleep(3)
                    player.stop()
                    break
                else:
                    print('Sorry sir!please Check the id again')
while(1):
    with sr.Microphone() as Source:
        print('listening')
        print('1')
        audio=r.listen(Source)
        print('Replying')
        try:
            data=r.recognize_google(audio)
        except UnknownValueError:
            print('say [hello techienest] to activate me')
        try:
            if data=='hello techienest':
                player=vlc.MediaPlayer('hello.mp3')
                player.play()
                time.sleep(5)
                player.stop()
                break
        except:
            print('say [hello techienest] to activate me')
while(1):
    with sr.Microphone() as Source:
        print('listening')
        audio1=r.listen(Source)
        print('Replying')
        try:
            data=r.recognize_google(audio1)
            print('tried')
        except UnknownValueError:
            player=vlc.MediaPlayer('sorry.mp3')
            player.play()
            time.sleep(5)
            player.stop()
        if data=="play some music":
            player=vlc.MediaPlayer('[iSongs.info] 03 - You & Me(1).mp3')
            player.play()
            time.sleep(30)
            player.stop()
        elif data=="I want food":
            player=vlc.MediaPlayer('food_menu.mp3')
            player.play()
            time.sleep(6)
            player.stop()
        elif data=="North Indian":
            player=vlc.MediaPlayer('North_Indian.mp3')
            player.play()
            time.sleep(6)
            player.stop()
            print('North Indian Food Menu\n')
            d1=pd.read_excel("/home/siva/Desktop/machine_learning_training/restaurant/food_menu_items.xlsx",0)
            print(d1)
            print('\nSay the item Ids of your wish one by one from above menu,Say zero to go to previous Menu to select type of food\n')
            player=vlc.MediaPlayer('choose.mp3')
            player.play()
            time.sleep(9)
            player.stop()
            order()
        elif data=="South Indian":
            player=vlc.MediaPlayer('South_Indian.mp3')
            player.play()
            time.sleep(3)
            player.stop()
        elif data=="veg":
            player=vlc.MediaPlayer('South_Indian_veg.mp3')
            player.play()
            time.sleep(4)
            player.stop()
            print("South Indian Veg Menu\n")
            d2=pd.read_excel("/home/siva/Desktop/machine_learning_training/restaurant/food_menu_items.xlsx",1)
            print(d2)
            print('\nSay the item Ids of your wish one by one from above menu,Say zero to go to previous Menu to select type of food\n')
            player=vlc.MediaPlayer('choose.mp3')
            player.play()
            time.sleep(9)
            player.stop()
            order()
        elif data=="non veg":
            player=vlc.MediaPlayer('South_Indian_nonveg.mp3')
            player.play()
            time.sleep(5)
            player.stop()
            print("South Indian Non Veg Menu\n")
            d3=pd.read_excel("/home/siva/Desktop/machine_learning_training/restaurant/food_menu_items.xlsx",2)
            print(d3)
            print('\nSay the item Ids of your wish one by one from above menu,Say zero to go to previous Menu to select type of food\n')
            player=vlc.MediaPlayer('choose.mp3')
            player.play()
            time.sleep(9)
            player.stop()
            order()
        elif data=="Chinese":
            player=vlc.MediaPlayer('chinese.mp3')
            player.play()
            time.sleep(4)
            player.stop()
            print("Chinese Menu")
            d4=pd.read_excel("/home/siva/Desktop/machine_learning_training/restaurant/food_menu_items.xlsx",3)
            print(d4)
            print('\nSay the item Ids of your wish one by one from above menu,Say zero to go to previous Menu and select type of food\n')
            player=vlc.MediaPlayer('choose.mp3')
            player.play()
            time.sleep(9)
            player.stop()
            order()
        elif data=="bill please":
            text=''
            b=0
            for con in order1:
                m=order1.index(con)
                text=text+str(idn[m])+' '+con+' '+str(cn[m])+'\n'
                b=b+int(cn[m])
            print('Your Bill on Screen sir')
            player=vlc.MediaPlayer('your_bill.mp3')
            player.play()
            time.sleep(2)
            player.stop()
            print(text)
            print("\n")
            print("You Need To Pay "+str(b)+" Rupees")
            script="You Need To Pay "+str(b)+" Rupees"
            obj=gtts.gTTS(text=script,lang='en')
            obj.save('run.mp3')
            player=vlc.MediaPlayer('run.mp3')
            player.play()
            time.sleep(3)
            player.stop()
        elif data=="thank you":
            print('its my privilige to serve you sir.\nI will wait to see you back Again.\nHave a nice day.')
            player=vlc.MediaPlayer('thanks.mp3')
            player.play()
            time.sleep(7)
            player.stop()
            break
        else:
            player=vlc.MediaPlayer('sorry.mp3')
            player.play()
            time.sleep(5)
            player.stop()
            print(data)
