from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

speech = speech_and_say();

def speech_catch_error():
	text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
	speech.say_VN_by_Google(text_catch)
    
class Instagram(object):
    browser = None
    # Khởi tạo ins với phần mềm google chrome
    def init(self):
        options =   webdriver.ChromeOptions()
        PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
        PATH1 = PATH[:9] + output_check + PATH[9:]
        options.add_argument("user-data-dir=" + PATH1)
        self.browser = webdriver.Chrome(executable_path=r'.//chrome_driver/chromedriver.exe',chrome_options=options)
        self.browser.get("https://www.instagram.com/")
        time.sleep(randint(1,2));

    # Quay trở lại trang chỉ ins
    def home(self):
            self.browser.get('https://www.instagram.com/')
            time.sleep(randint(1,2))
            
    def scroll_down(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + " + str(len) + " )")

    def scroll_up(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY - " + str(len) + " )")
class operation_ins(Instagram):
    # Gõ vào thanh tìm kiếm
    def type_in_search(self,nhap='Vũ Minh Hiếu'):
        try:
            text = speech.speech_none_pause();
            if(text != ''):
                nhap = text;
            timkiem = None;
            try:
                timkiem = self.browser.find_element_by_xpath('//input[@placeholder="Tìm kiếm"]')
            except:
                try:
                    timkiem = self.browser.find_element_by_xpath('//input[@placeholder="Search"]')
                except:
                    pass
            timkiem.send_keys(nhap)
            timkiem.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # Chọn phần tử khi tìm kiếm
    def search_by_index(self, id = 0):
        try:
            id_ = speech.speech_none_pause()
            id = general.get_number(id_)
            time.sleep(randint(1,2))
            use = self.browser.find_elements_by_class_name('-qQT3')
            self.browser.execute_script("arguments[0].click();",use[id]);
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # Chọn vào la bàn
    def turn_compass(self):
        try:
            self.browser.get('https://www.instagram.com/explore/');
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

# Phần clas về story
class story_ins(Instagram):
    # chọn story
    def chon_video(self, id = 0):
        try:
            id_ = speech.speech_none_pause()
            id = general.get_number(id_)
            time.sleep(randint(1,2))
            use = self.browser.find_elements_by_class_name('_6q-tv')
            self.browser.execute_script("arguments[0].click();",use[id]);
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

class story_ins_in(Instagram):
    # Story tiếp theo
    def next_video(self):
        try:
            use = self.browser.find_element_by_class_name('coreSpriteRightChevron')
            self.browser.execute_script("arguments[0].click();",use);
            time.sleep(randint(1,2)) 
        except:
            speech_catch_error()

    # Bình luận story
    def comment(self, text = 'Thử comment tý thôi!'):
        try:
            nhap = speech.speech_none_pause()
            if(nhap != ''):
                text = nhap;
            use = self.browser.find_element_by_class_name('Xuckn');
            use.send_keys(text);
            time.sleep(randint(1,2))
            use.send_keys(Keys.RETURN)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()
class status_ins(Instagram):

    # Hàm này để tìm phần tử nào đang trên màn hình
    def find_index(self):
        click1 = 0; click2 = 0; click3 = 0; click4 = 0
        for i in range(0,350):
            try:
                click1_use = self.browser.find_elements_by_class_name('Ppjfr.UE9AK.wdOqh')
                click1 = general.kiem_tra_trong_view(drivers = self.browser, elem = click1_use[i])
            except:
                pass

            try:
                click2_use = self.browser.find_elements_by_class_name('_9AhH0')
                click2 = general.kiem_tra_trong_view(drivers = self.browser, elem = click2_use[i])
            except:
                pass

            try:
                click3_use = self.browser.find_elements_by_class_name('ltpMr.Slqrh')
                click3 = general.kiem_tra_trong_view(drivers = self.browser, elem = click3_use[i])
            except:
                pass

            try:
                click4_use = self.browser.find_elements_by_class_name('sH9wk._JgwE')
                click4 = general.kiem_tra_trong_view(drivers = self.browser, elem = click4_use[i])
            except:
                pass

            time.sleep(randint(1,2));

            if(click1 or click2 or click3 or click4):
                return i

        return -10;        

    # thả trái tim trên status không được đổi tên hàm
    def bieu_cam_facebook(self, stt_bieu_cam = 0):
        try:
            id = speech.speech_none_pause()
            stt_bieu_cam = general.get_number(id)
            stt_bieu_cam = self.find_index();
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[' + str(stt_bieu_cam + 1) + ']/div[3]/section[1]/span[1]/button');
            self.browser.execute_script('arguments[0].click()',use)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # Gõ bình luận status
    def comment(self, text = 'Thử comment nè!'):
        try:
            text_ = speech.speech_none_pause()
            if(text_ != ''):
                text = text
            stt = self.find_index();
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[' + str(stt + 1) + ']/div[3]/section[3]/div/form/textarea');
            use.send_keys(text);
            time.sleep(randint(1,2))
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article[' + str(stt + 1) + ']/div[3]/section[3]/div/form/button[2]');
            self.browser.execute_script("arguments[0].click();",use)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()
    # Lưu bài viết
    def save_and_follow(self, chose = 1):
        try:
            text = speech.speech_none_pause()
            chose = general.get_number(text)
            chose = self.find_index();
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article[' + str(chose + 1) + ']/div[3]/section[1]/span[4]/div/div/button');
            self.browser.execute_script("arguments[0].click();",use)
        except:
            speech_catch_error()

class status_ins_in(Instagram):
    # Thả biểu cảm khi bên trong status
    def bieu_cam_facebook(self, stt_bieu_cam = 0):
        try:
            id = speech.speech_none_pause()
            stt_bieu_cam = general.get_number(id)
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button');
            self.browser.execute_script('arguments[0].click()',use)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # comment trong status
    def comment(self, text = 'Thử comment nè!'):
        try:
            text_ =  speech.speech_none_pause()
            if(text_ != ''):
                text = text_;
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea');
            use.send_keys(text);
            time.sleep(randint(1,2))
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]');
            self.browser.execute_script("arguments[0].click();",use)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # Lưu bài viết
    def save_and_follow(self, chose = 1):
        try:
            id = speech.speech_none_pause()
            chose = general.get_number(id)
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[4]/div/div/button');
            self.browser.execute_script("arguments[0].click();",use)
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

class mess_ins(Instagram):
    # mở message ở trong Instagram
    def message(self):
        try:
            self.browser.get('https://www.instagram.com/direct/inbox/')
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # Chọn người muốn nhắn tin
    def search_by_index(self, id = 0):
        try:
            text = speech.speech_none_pause()
            id = general.get_number(text)
            use = self.browser.find_elements_by_class_name('-qQT3.rOtsg');
            self.browser.execute_script('arguments[0].click()',use[id])
            time.sleep(randint(1,2))
        except:
            speech_catch_error()

    # nhắn tin với người kia
    def chat(self, text = 'Mình là chatbot xin lỗi đã làm phiền'):
        try:
            text_ = speech.speech_none_pause()
            if(text_ != ''):
                text = text_;
            use = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            use.send_keys(text);
            time.sleep(randint(1,2))
            use.send_keys(Keys.RETURN);
            time.sleep(randint(1,2));
        except:
            speech_catch_error()