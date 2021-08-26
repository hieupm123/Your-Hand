import threading
from pyvi import ViTokenizer, ViPosTagger
from pyvi import ViUtils
import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from pystray._base import MenuItem as item
import pystray._win32
from pathlib import Path
import tkinter
import webbrowser

import speech_recognition
import pyttsx3
import schedule
import time,os,string
import playsound
from gtts import gTTS 
import time
from pygame import mixer
from mutagen.mp3 import MP3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import js2py
import time
from random import seed
from random import randint
from selenium.webdriver.common.action_chains import ActionChains 
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from time import sleep
import pickle

from os import get_terminal_size
from threading import Thread
import sqlite3
from Hardware_PC import *
from pack_and_run import *
from Web_chat import *
from Web_zalo import *
from Wed_google import *
from Wed_youtube import *
from general_web import *
from instagram import *

speech = speech_and_say()

# map chứ class
mapping_value = {"check_mess" : check_mess,"general_web" : general_web, "Hardware" : Hardware, "Instagram": Instagram,"operation_ins": operation_ins,"story_ins": story_ins,"story_ins_in": story_ins_in,"status_ins": status_ins,"status_ins_in": status_ins_in,"mess_ins": mess_ins, "facebook" : facebook,"Search_in_facebook" : Search_in_facebook,"story_facebook" : story_facebook,"story_facebook_in" : story_facebook_in,"Friend_facebook" : Friend_facebook,"watch_facebook" : watch_facebook,"watch_facebook_in" : watch_facebook_in,"status_facebook" : status_facebook,"check_tin_nhan_thong_bao" : check_tin_nhan_thong_bao,"messenger" : messenger,"zalo" : zalo,"tin_nhan_zalo" : tin_nhan_zalo,"tim_kiem_zalo" : tim_kiem_zalo,"danh_ba_zalo" : danh_ba_zalo,"to_do" : to_do,"cai_dat" : cai_dat,"tai_khoan" : tai_khoan,"check" : check, "google" : google, "youtube" : youtube,"video_kham_pha" : video_kham_pha,"search_youtube" : search_youtube,"video" : video,"trinh_phat_thu_nho" : trinh_phat_thu_nho}



exit_event= [threading.Event()]

# Phần giao tiếp nói chuyện
def get_id_giao_tiep(text):
    a = [];
    model = pickle.load(open("./Training/data_giao_tiep.pkl", 'rb'))
    a.append(text);
    y_pred = model.predict(a)
    return y_pred[0];

def get_giao_tiep(text):
    id = get_id_giao_tiep(text)
    data = sqlite3.connect("./Training/data_giao_tiep.db")
    c = data.cursor()
    c.execute(f"SELECT * FROM data_giao_tiep WHERE id = {id}")
    items = c.fetchall()
    data.commit()
    data.close()
    return items;

# Phần chức năng điều khiển
def get_id_chuc_nang(text):
    a = [];
    model = pickle.load(open("./Training/chuc_nang.pkl", 'rb'))
    a.append(text);
    y_pred = model.predict(a)
    return y_pred[0];

def get_chuc_nang(text):
    id = get_id_chuc_nang(text)
    data = sqlite3.connect("./Training/chuc_nang.db")
    c = data.cursor()
    c.execute(f"SELECT * FROM chuc_nang WHERE id = {id}")
    items = c.fetchall()
    data.commit()
    data.close()
    return items

def class_to_text(text):
    text = text.replace("Hardware_PC.","")
    text = text.replace("pack_and_run.","")
    text = text.replace("Web_chat.","")
    text = text.replace("Web_zalo.","")
    text = text.replace("Wed_google.","")
    text = text.replace("Wed_youtube.","")
    text = text.replace("general_web.","")
    text = text.replace("<class '","")
    text = text.replace("'>","")
    return text

ar = [check,check_mess,check_tin_nhan_thong_bao, Hardware]
value_is_runing = []
name_class_runing = [];
for i in ar:
    I = i();
    value_is_runing.append(I)
    name_class_runing.append(class_to_text(str(i)))
    
len_of_task_defaut = len(ar)
Thread_ar = []


    # setting_page
def create_wd_setting():      
    wd_setting = Toplevel();
    wd_setting.title('Setting')
    wd_setting.geometry("600x600")
    # wd_setting.configure(bg = "#C4C4C4")
    wd_setting.iconbitmap('./GUI/logo.ico')
    def close_window_setting():
        Thread_ar[2] = threading.Thread(target = luong_process, args=(2,))

    wd_setting.protocol('WM_DELETE_WINDOW', close_window_setting())
    canvas_setting = Canvas(
        wd_setting,
        height = 600,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_setting.place(x = 0, y = 0)
    b_g_1 = ImageTk.PhotoImage(Image.open("./GUI/bg_1_1.png"))
    canvas_setting.create_image(0,0,anchor=NW,image=b_g_1)  
    # wd_setting.image = b_g_1

    bg_1_1 = ImageTk.PhotoImage(Image.open("./GUI/bg_1_1.png")) 
    laybe_back_gr_st = tk.Label(
        master = canvas_setting,
        image = bg_1_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    laybe_back_gr_st.place(
        x=0,
        y=0
    )

    laybe_back_gr_st.img = bg_1_1
    title_st = ImageTk.PhotoImage(Image.open("./assets/name_st.png")) 
    tt_st_vl = tk.Label(
        master = canvas_setting,
        image = title_st,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    tt_st_vl.place(
        x=153,
        y=13
    )
    tt_st_vl.img = title_st


    def back_st_click():
        volume_in_mixer[0] =  scale_volume_st.get()
        value_scroll_st[0] = scale_scroll_st.get()
        speed_st_[0] = scale_speed_st.get()
        value_light_st[0] = scale_light_st.get()
        wd_setting.destroy()

    back_setting_img = ImageTk.PhotoImage(Image.open("./assets/back_st.png")) 
    back_setting = tk.Button(
        master = canvas_setting,
        image = back_setting_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_st_click(),
        relief="flat"
    )

    def on_leave_back_st(e):
        pause_img = PhotoImage(file = f"./assets/back_st.png") 
        back_setting.config(image = pause_img)
        back_setting.image = pause_img

    def on_enter_back_st(e):
        pause_hover = PhotoImage(file = f"./assets/back_hover_st.png") 
        back_setting.config(image = pause_hover)
        back_setting.image = pause_hover

    back_setting.place(
        x=0.0,
        y=39.0,
        width=90.0,
        height=77.0
    )
    back_setting.img = back_setting_img
    back_setting.bind("<Enter>", on_enter_back_st)
    back_setting.bind("<Leave>", on_leave_back_st)


    volume_setting_img = ImageTk.PhotoImage(Image.open("./assets/volume_st.png"))
    volume_setting = tk.Label(
        master = canvas_setting,
        image=volume_setting_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    
    volume_setting.place(
        x=66.0,
        y=139.0,
    )
    volume_setting.img = volume_setting_img

    scale_volume_st = tk.Scale(
        master = canvas_setting,
        bd = 0,
        resolution = 0.01,
        from_= 0.0,
        to=1.0,
        length=348,
        orient=HORIZONTAL,
        bg = '#9e9e9e',
    )
    scale_volume_st.place(
        x = 183,
        y = 150,
    )
    scale_volume_st.set(volume_in_mixer[0])

    scroll_page_img = ImageTk.PhotoImage(Image.open("./assets/scroll_st.png"))
    scroll_page = tk.Label(
        master = canvas_setting,
        image=scroll_page_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    scroll_page.place(
        x=66.0,
        y=313.0,
    )

    scale_scroll_st = tk.Scale(
        master = canvas_setting,
        bd = 0,
        resolution = 1,
        from_= 250,
        to=400,
        length=348,
        orient=HORIZONTAL,
        bg = '#9e9e9e',
    )
    scale_scroll_st.place(
        x = 182,
        y = 334,
    )
    scale_scroll_st.set(value_scroll_st[0])

    scroll_page.img = scroll_page_img

    light_setting_png = ImageTk.PhotoImage(Image.open("./assets/light_st.png"))
    light_setting = tk.Label(
        master = canvas_setting,
        image=light_setting_png,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    light_setting.place(
        x=55.0,
        y=409.0
    )
    light_setting.img = light_setting_png

    scale_light_st = tk.Scale(
        master = canvas_setting,
        bd = 0,
        resolution = 1,
        from_= 10,
        to=60,
        length=348,
        orient=HORIZONTAL,
        bg = '#9e9e9e',
    )
    scale_light_st.place(
        x = 182,
        y = 426,
    )
    scale_light_st.set(value_light_st[0])

    speech_setting_png = ImageTk.PhotoImage(Image.open("./assets/speed_st.png"))
    speech_setting = tk.Label(
        master = canvas_setting,
        image=speech_setting_png,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    speech_setting.place(
        x=63.0,
        y=228.0
    )
    speech_setting.img = speech_setting_png

    scale_speed_st = tk.Scale(
        master = canvas_setting,
        bd = 0,
        resolution = 1,
        from_= 0,
        to=10,
        length=348,
        orient=HORIZONTAL,
        bg = '#9e9e9e',
    )
    scale_speed_st.place(
        x = 182,
        y = 234,
    )
    scale_speed_st.set(speed_st_[0])



    cpu_img = ImageTk.PhotoImage(Image.open("./assets/cpu_st.png"))
    def get_cpu():
        lable_cpu_st.config(text=('CPU Using: ' +  str(psutil.cpu_percent(4))  + '%'))

    cpu = tk.Button(
        master = canvas_setting,
        image = cpu_img,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: get_cpu(),
        relief="flat"
    )
    cpu.place(
        x=55.0,
        y=505.0
    ) 
    cpu.img = cpu_img

    # cpu_shower = ImageTk.PhotoImage(Image.open('./assets/cpu_shower.png'))
    lable_cpu_st = tk.Label(
        master = canvas_setting,
        bg = '#cfcbcb',
        font=('Century Gothic',29),
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
    )
    lable_cpu_st.place(
        width=348,
        height=47,
        x = 182,
        y = 517,
    )
    lable_cpu_st.config(text=('CPU Using: ' +  str(psutil.cpu_percent(4))  + '%'))
    wd_setting.resizable(False, False) 




def luong_giao_dien():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    root = Tk()
    root.title('Your Hand')
    root.geometry("1000x600")
    # root.configure(bg = "#FFFFFF")


    root.iconphoto(False, tk.PhotoImage(file='./GUI/logo.png'))
    root.iconbitmap('./GUI/logo.ico')   



    # set tắt mở
    def quit_window(icon, item):
        icon.stop()
        exit_event[0].set()
        root.destroy()

# Define a function to show the window again
    def show_window(icon, item):
        icon.stop()
        root.after(0,root.deiconify())

# Hide the window and show on the system taskbar
    def close_window():
        exit_event[0].set()
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', close_window)
    # Hide windown
    def hiden_window():
        root.withdraw()
        image=Image.open("./GUI/logo.ico")
        menu=(item('Quit', quit_window), item('Show', show_window))
        icon=pystray.Icon("name", image, "My System Tray Icon", menu)
        icon.run()    


    # set giao diện
    canvas = Canvas(
        root,
        bg = "#FFFFFF",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    b_g = PhotoImage(file = "./GUI/bg_2.png") 
    canvas.create_image(0,0,anchor=NW,image=b_g)  
    name_pr = PhotoImage(file = "./assets/name_your_hand.png")
    canvas.create_image(146,28,anchor=NW,image=name_pr)    

    # main_page
    ar_po = [0]
    def on_click_pause(value):
        if(ar_po[0] == 0):
            exit_event[0].set()
            value.image = pause_cg
            ar_po[0] = 1;
        else:
            exit_event[0] = threading.Event()
            Thread_ar[0].start()
            value.image = pause_img
            ar_po[0] = 0
    button_image_1 = PhotoImage(
        file=relative_to_assets("pause.png"))
    pause = Button(
        master = root,        
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click_pause(pause),
        relief="flat"
    )
    pause_img = PhotoImage(file = f"./assets/pause.png") 
    pause_hover = PhotoImage(file = f"./assets/pause_hover.png") 
    pause_cg = PhotoImage(file = f"./assets/continue.png") 
    pause_cg_hover = PhotoImage(file = f"./assets/continue_hover.png")

    def on_leave_pause(e):
        if(ar_po[0] == 0):
            pause.config(image = pause_img)
            pause.image = pause_img
        elif(ar_po[0] == 1):
            pause.config(image = pause_cg)
            pause.image = pause_img            
    def on_enter_pause(e):
        if(ar_po[0] == 0):
            pause.config(image = pause_hover)
            pause.image = pause_hover
        elif(ar_po[0] == 1):
            pause.config(image = pause_cg_hover)
            pause.image = pause_cg_hover    
    pause.place(
        x=664.0,
        y=78.0,
        width=317.0,
        height=81.0
    )
    pause.bind("<Enter>", on_enter_pause)
    pause.bind("<Leave>", on_leave_pause)
    # pause.bind("<Button-1>", on_click_pause)

    button_image_2 = PhotoImage(
        file=relative_to_assets("setting.png"))
    setting = Button(
        master = root,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Thread_ar[2].start(),
        relief="flat"
    )
    def on_leave_setting(e):
        pause_img = PhotoImage(file = f"./assets/setting.png") 
        setting.config(image = pause_img)
        setting.image = pause_img

    def on_enter_setting(e):
        pause_hover = PhotoImage(file = f"./assets/setting_hover.png") 
        setting.config(image = pause_hover)
        setting.image = pause_hover

    setting.place(
        x=491.0,
        y=354.0,
        width=331.0,
        height=96.0
    )

    setting.bind("<Enter>", on_enter_setting)
    setting.bind("<Leave>", on_leave_setting)

    button_image_3 = PhotoImage(
        file=relative_to_assets("stop.png"))
    off_pro = Button(
        master = root,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: hiden_window(),
        relief="flat"
    )
    def on_leave_stop(e):
        pause_img = PhotoImage(file = f"./assets/stop.png") 
        off_pro.config(image = pause_img)
        off_pro.image = pause_img

    def on_enter_stop(e):
        pause_hover = PhotoImage(file = f"./assets/stop_hover.png") 
        off_pro.config(image = pause_hover)
        off_pro.image = pause_hover
    off_pro.place(
        x=576.0,
        y=202.0,
        width=322.0,
        height=98.0
    )
    off_pro.bind("<Enter>", on_enter_stop)
    off_pro.bind("<Leave>", on_leave_stop)

    button_image_4 = PhotoImage(
        file=relative_to_assets("about.png"))
    about_me = Button(
        master = root,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: messagebox.showinfo("Your hand", "Version 1.0.0"),
        relief="flat"
    )
    def on_leave_about(e):
        pause_img = PhotoImage(file = f"./assets/about.png") 
        about_me.config(image = pause_img)
        about_me.image = pause_img

    def on_enter_about(e):
        pause_hover = PhotoImage(file = f"./assets/about_hover.png") 
        about_me.config(image = pause_hover)
        about_me.image = pause_hover
    about_me.place(
        x=125.0,
        y=468.0,
        width=327.0,
        height=90.0
    )
    about_me.bind("<Enter>", on_enter_about)
    about_me.bind("<Leave>", on_leave_about)

    def contact_me():
            contact_me_page = Toplevel(canvas);
            contact_me_page.title('Contact me')
            contact_me_page.geometry("300x300")
            contact_me_page.iconbitmap('./GUI/logo.ico')
            canvas_contact_page = Canvas(
                contact_me_page,
                height = 300,
                width = 300,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            canvas_contact_page.place(x = 0, y = 0)
            b_g_2 = ImageTk.PhotoImage(Image.open("./GUI/bg_2_2.png"))
            canvas_contact_page.create_image(0,0,anchor=NW,image=b_g_2)
            laybe_back_gr_ct = tk.Label(
                master = canvas_contact_page,
                image = b_g_2,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            laybe_back_gr_ct.place(
                x=0,
                y=0
            )
            laybe_back_gr_ct.img = b_g_2

            title_ct = ImageTk.PhotoImage(Image.open("./assets/name_contact_us.png")) 
            tt_st_cl = tk.Label(
                master = canvas_contact_page,
                image = title_ct,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            tt_st_cl.place(
                x=53,
                y=5
            )
            tt_st_cl.img = title_ct

            cuong_img = ImageTk.PhotoImage(Image.open("./assets/cuong.png")) 
            hieu_img = ImageTk.PhotoImage(Image.open("./assets/hieu.png")) 
            bo_img = ImageTk.PhotoImage(Image.open("./assets/bo.png")) 

            cuong_ct = tk.Label(
                master = canvas_contact_page,
                image = cuong_img,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            cuong_ct.place(
                x=5,
                y=231
            )
            cuong_ct.img = cuong_img

            hieu_ct = tk.Label(
                master = canvas_contact_page,
                image = hieu_img,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            hieu_ct.place(
                x=7,
                y=152
            )
            hieu_ct.img = hieu_img

            bo_ct = tk.Label(
                master = canvas_contact_page,
                image = bo_img,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            bo_ct.place(
                x=6,
                y=74
            )
            bo_ct.img = bo_img
            # Cuong 
            cuong_i = ImageTk.PhotoImage(Image.open("./assets/cuong_i.png")) 
            cuong_i_ct = tk.Button(
                master = canvas_contact_page,
                image = cuong_i,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.instagram.com/cuongtran04/'),
                relief="flat"
            )
            cuong_i_ct.place(
                x = 261,
                y = 234,
                width= 36,
                height=39
            )
            cuong_i_ct.img = cuong_i

            cuong_f = ImageTk.PhotoImage(Image.open("./assets/cuong_f.png")) 
            cuong_f_ct = tk.Button(
                master = canvas_contact_page,
                image = cuong_f,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.facebook.com/profile.php?id=100012592357630'),
                relief="flat"
            )
            cuong_f_ct.place(
                x = 215,
                y = 235,
                width= 39,
                height=38
            )
            cuong_f_ct.img = cuong_f
            # Minh Hieu minh ne =))
            hieu_i = ImageTk.PhotoImage(Image.open("./assets/hieu_i.png")) 
            hieu_i_ct = tk.Button(
                master = canvas_contact_page,
                image = hieu_i,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.instagram.com/mhieu.comss/'),
                relief="flat"
            )
            hieu_i_ct.place(
                x = 250,
                y = 152,
                width= 39,
                height=40
            )
            hieu_i_ct.img = hieu_i

            hieu_f = ImageTk.PhotoImage(Image.open("./assets/hieu_f.png")) 
            hieu_f_ct = tk.Button(
                master = canvas_contact_page,
                image = hieu_f,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.facebook.com/minhhieu.vu.33449138/'),
                relief="flat"
            )
            hieu_f_ct.place(
                x = 204,
                y = 153,
                width= 38,
                height=38
            )
            hieu_f_ct.img = hieu_f

            # Bo
            bo_i = ImageTk.PhotoImage(Image.open("./assets/bo_i.png")) 
            bo_i_ct = tk.Button(
                master = canvas_contact_page,
                image = bo_i,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.facebook.com/bo.phanvan.188'),
                relief="flat"
            )
            bo_i_ct.place(
                x = 190,
                y = 73,
                width= 42,
                height=40
            )
            bo_i_ct.img = bo_i

            bo_f = ImageTk.PhotoImage(Image.open("./assets/bo_f.png")) 
            bo_f_ct = tk.Button(
                master = canvas_contact_page,
                image = bo_f,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: webbrowser.open('https://www.facebook.com/bo.phanvan.188'),
                relief="flat"
            )
            bo_f_ct.place(
                x = 147,
                y = 74,
                width= 37,
                height=41
            )
            bo_f_ct.img = bo_f

    bt_new_ct = PhotoImage(
        file=relative_to_assets("conact.png"))
    contact = Button(
        master = root,
        image=bt_new_ct,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: contact_me(),
        relief="flat"
    )

    def on_leave_contact(e):
        pause_img = PhotoImage(file = f"./assets/conact.png") 
        contact.config(image = pause_img)
        contact.image = pause_img

    def on_enter_contact(e):
        pause_hover = PhotoImage(file = f"./assets/conact_hover.png") 
        contact.config(image = pause_hover)
        contact.image = pause_hover
    contact.place(
        x=40.0,
        y=355.0,
        width=329.0,
        height=95.0
    )
    contact.bind("<Enter>", on_enter_contact)
    contact.bind("<Leave>", on_leave_contact)
    root.resizable(False, False)    
    root.mainloop()
def luong_chay_ngam():

    while(1):
        if(exit_event[0].is_set()):
            Thread_ar[0] = threading.Thread(target=luong_process,args=(0,))
            sys.exit()
        text = ''
        while(text == ''):
            if(exit_event[0].is_set()):
                Thread_ar[0] = threading.Thread(target=luong_process,args=(0,))
                sys.exit()
            text = speech.speech_none_pause()
            time.sleep(randint(1,2))
        # print(text)
        if(text != ''):
            if(exit_event[0].is_set()):
                Thread_ar[0] = threading.Thread(target=luong_process,args=(0,))
                sys.exit()
            text = text.lower()
            text = ViTokenizer.tokenize(text)
            print(text)
            task = get_chuc_nang(text)
            ok = 0;
            # print(text)
            if(task[0][2] == 'close_app()'):
                try:
                    value_is_runing[len_of_task_defaut].browser.close()
                    for i in range (len_of_task_defaut,len(name_class_runing)):
                        del name_class_runing[len_of_task_defaut];
                        del value_is_runing[len_of_task_defaut];
                    ok = 1
                except:
                    pass
                
            if(task[0][2] == 'init()' and task[0][1] in name_class_runing):
                try:
                    idex_ = name_class_runing.index(task[0][1]);
                    value_is_runing[idex_].home()
                    ok = 1
                except:
                    for i in range (len_of_task_defaut,len(name_class_runing)):
                        del name_class_runing[len_of_task_defaut];
                        del value_is_runing[len_of_task_defaut];

            if(task[0][2] == 'init()' and task[0][1] not in name_class_runing):
                try:
                    value = mapping_value[task[0][1]]()
                    speech.say_VN_by_Google(task[0][3])
                    try:
                        if(len(name_class_runing) > len_of_task_defaut):
                            value.browser = value_is_runing[len_of_task_defaut].browser
                            for lpq in range(0,3):
                                value_is_runing[lpq].browser = value.browser
                            value.home()
                            for i in range (len_of_task_defaut,len(name_class_runing)):
                                del name_class_runing[len_of_task_defaut];
                                del value_is_runing[len_of_task_defaut]
                        else:
                            value.init();
                            for lpq in range(0,3):
                                value_is_runing[lpq].browser = value.browser                        
                    except:
                        for i in range (len_of_task_defaut,len(name_class_runing)):
                            del name_class_runing[len_of_task_defaut];
                            del value_is_runing[len_of_task_defaut]
                        value.init()
                        for lpq in range(0,3):
                            value_is_runing[lpq].browser = value.browser
                    value_is_runing.append(value)
                    name_class_runing.append(task[0][1])
                    for vl in range(0,len(task)):
                        name_class_runing.append(task[vl][1])
                        val = mapping_value[task[vl][1]]()
                        val.browser = value.browser
                        value_is_runing.append(val)
                    ok = 1;
                except:
                    pass
            
            if(exit_event[0].is_set()):
                Thread_ar[0] = threading.Thread(target=luong_process,args=(0,))
                sys.exit()
            print(name_class_runing)
            # chạy chức năng nếu thỏa mãn
            if(ok == 0):
                for j in task:
                    if(ok == 0):
                        if(str(j[1]) in name_class_runing):
                            try:
                                print(j[1])
                                text_ = str(j[2]);
                                text_run = text_[:text_.find('(')]
                                r = text_
                                string_1 = ''.join(x for x in r if x.isdigit())
                                print(text_run)
                                print(string_1)
                                speech.say_VN_by_Google(str(j[3]))
                                index_ = name_class_runing.index(str(j[1]))
                                if(string_1 != ''):
                                    getattr(value_is_runing[index_], text_run)(int(string_1))
                                else:
                                    getattr(value_is_runing[index_], text_run)()
                                ok = 1
                            except:
                                pass
            

            if(exit_event[0].is_set()):
                Thread_ar[0] = threading.Thread(target=luong_process,args=(0,))
                sys.exit()
            # chạy giao tiếp nếu không thỏa mãn cái nào trong task
            if(ok == 0):
                giao_tiep = get_giao_tiep(text);
                print(giao_tiep[0][1])
                speech.say_VN_by_Google(giao_tiep[0][1])

        time.sleep(2);

def luong_process(x):
    if(x == 0):
        luong_chay_ngam()
    elif(x == 1):
        luong_giao_dien()
    elif(x == 2):
        create_wd_setting()

for out in range(0,3):
    new_luong_ngam = threading.Thread(target = luong_process, args=(out,))
    Thread_ar.append(new_luong_ngam)
Thread_ar[0].start()
Thread_ar[1].start()
speech.init()
