import speech_recognition
import pyttsx3
import schedule
import time,os,string
import playsound
from gtts import gTTS 
import time
from pygame import mixer
from mutagen.mp3 import MP3

# sau này chúng ta sẽ phát triển cái database riêng chứa các nội dung text
# phát triển chương trình sau random text đồng nghĩa phù hợp 

volume_in_mixer = [float(1.0)] 
speed_st_ = [int(5)]
class speech_and_say:
    def init(self):
        name = ''
        self.say_VN_by_Google('chào bạn cùng bắt đầu nhé')

    def say_VN_by_Google(self,text):
        try:
            e = gTTS(text=text,lang = 'vi')
            e.save('abc.mp3')
            time.sleep(1)
            audio = MP3("abc.mp3")
            mixer.init()
            mixer.music.load('abc.mp3')
            mixer.music.set_volume(volume_in_mixer[0])
            mixer.music.play()
            time.sleep(int(audio.info.length) + 0.5)
            mixer.music.stop()
            mixer.quit()
            os.remove('abc.mp3')
        except:
            pass
            
    def say_VN_by_Microsoft(self, text):
        e = pyttsx3.init()
        voice_VN_id = ""
        try:
            voice_VN_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
            e.setProperty('voice',voice_VN_id)
        except:
            self.say_VN_by_google(text)
            return
        e.say(text)
        e.runAndWait()
        
    def speech_none_pause(self):
        text = '';
        sp = speech_recognition.Recognizer();
        with speech_recognition.Microphone() as mic:
            sp.adjust_for_ambient_noise(mic, duration=0.2)
            audio = sp.record(mic, duration=3)
        try:
            text = sp.recognize_google(audio,language="vi-VI");
        except:
            pass;
        return text;

    def speech_with_pause(self):
        sp = speech_recognition.Recognizer();
        with speech_recognition.Microphone() as mic:
            audio = sp.listen(mic)
        try:
            text = sp.recognize_google(audio,language="vi-VI");
        except:
            text = ''
        return text

    def say(self,text):
        e = pyttsx3.init();
        e.say(text)
        e.runAndWait()
            
            



