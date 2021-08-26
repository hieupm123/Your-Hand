from general_web import *

general = general_web()
output_check = general.lay_ten_nguoi_dung()

speech = speech_and_say();

def speech_catch_error():
	text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
	speech.say_VN_by_Google(text_catch)

class zalo(object):

    browser = None

    def init(self):
        try:
            options = webdriver.ChromeOptions()
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.browser = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
            self.browser.get("https://chat.zalo.me/?null")
            time.sleep(3)
        except:
            speech_catch_error()

    def home(self):
        self.browser.get('https://chat.zalo.me/?null')

    def scroll_down(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + " + str(len) + " )")

    def scroll_up(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY - " + str(len) + " )")
    
class tin_nhan_zalo(zalo):

    def message(self):
        try:
            phu_luc = self.browser.find_elements_by_class_name('internal-icon')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(phu_luc[0]).click(phu_luc[0]).perform()
            sleep(1)
        except:
            speech_catch_error();

    def search_by_index(self,a=1):
        try:
            self.mo_tin_nhan()
            chon_nhan_tin = self.browser.find_elements_by_class_name('msg-item')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(chon_nhan_tin[a-1]).click(chon_nhan_tin[a-1]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def chat(self,a=''):
        try:
            text = speech.speech_none_pause();
            if(text != ''):
                a = text;
            nhantin = self.browser.find_element_by_id('input_line_0')
            nhantin.send_keys(a)
            sleep(1)
            nhantin.send_keys(Keys.RETURN)
        except:
            speech_catch_error()
    
    def bieu_cam_facebook(self ,stt_bieu_cam = 1):
        try:
            thaicon = self.browser.find_element_by_class_name('imgHolder')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(thaicon).click(thaicon).perform()
            sleep(1)
        except:
            speech_catch_error()


    

class tim_kiem_zalo(zalo):

    def type_in_search(self, nhap=''):
        try:
            text = speech.speech_none_pause();
            if(text != ''):
                nhap = text;
            tim_kiem = self.browser.find_element_by_id('contact-search-input')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(tim_kiem).click(tim_kiem).perform()    
            tim_kiem.send_keys(nhap)
            sleep(1)   
        except:
            speech_catch_error()

    # a là một số hãy giải quyết số đó 
    def chon_nguoi_muon_tim(self, a=1):
        try:
            text = speech.speech_none_pause()
            a = general.get_number(text);
            chon_tin_nhan = self.browser.find_elements_by_class_name('zl-avatar__photo')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(chon_tin_nhan[a+2]).click(chon_tin_nhan[a+2]).perform()    
            sleep(1)   
        except:
            speech_catch_error()

class danh_ba_zalo(zalo):

    def home_friend(self):
        try:
            phu_luc = self.browser.find_elements_by_class_name('internal-icon')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(phu_luc[1]).click(phu_luc[1]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def list_friend(self):
        try:
            danh_sach = self.browser.find_elements_by_class_name('fr-conv-item-avatar')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(danh_sach[0]).click(danh_sach[0]).perform()
            sleep(1)
        except:
            speech_catch_error()
    def danh_sach_nhom(self):
        try:
            danh_sach = self.browser.find_elements_by_class_name('fr-conv-item-avatar')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(danh_sach[1]).click(danh_sach[1]).perform()
            sleep(1)
        except:
            speech_catch_error()
        
    def truyen_file(self):
        try:
            danh_sach = self.browser.find_elements_by_class_name('zl-avatar__photo')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(danh_sach[3]).click(danh_sach[3]).perform()
            sleep(1)
        except:
            speech_catch_error()

class to_do(zalo):

    def mo_to_do(self):
        try:
            phu_luc = self.browser.find_elements_by_class_name('internal-icon')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(phu_luc[3]).click(phu_luc[3]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def to_do_toi_giao(self):
        try:
            cac_muc = self.browser.find_elements_by_class_name('td-tab')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(cac_muc[0]).click(cac_muc[0]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def to_do_can_lam(self):
        try:
            cac_muc = self.browser.find_elements_by_class_name('td-tab')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(cac_muc[1]).click(cac_muc[1]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def to_do_theo_gioi(self):
        try:
            cac_muc = self.browser.find_elements_by_class_name('td-tab')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(cac_muc[2]).click(cac_muc[2]).perform()
            sleep(1)
        except:
            speech_catch_error()
 
    def to_do_chua_xong(self):
        try:
            cac_muc = self.browser.find_elements_by_class_name('td-sub-tab')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(cac_muc[0]).click(cac_muc[0]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def to_do_da_xong(self):
        try:
            cac_muc = self.browser.find_elements_by_class_name('td-sub-tab')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(cac_muc[1]).click(cac_muc[1]).perform()
            sleep(1)
        except:
            speech_catch_error()

class cai_dat(zalo):

    def mo_cai_dat(self):
        try:
            phu_luc = self.browser.find_elements_by_class_name('internal-icon')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(phu_luc[6]).click(phu_luc[6]).perform()
            sleep(1)
            seting = self.browser.find_elements_by_class_name('fa-outline-settings')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(seting[1]).click(seting[1]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def tat_cai_dat(self):
        try:
            tat_cai_dat = self.browser.find_element_by_class_name('fa-close')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(tat_cai_dat).click(tat_cai_dat).perform()
            sleep(1)
        except:
            speech_catch_error()

class tai_khoan(zalo):

    def mo_tai_khoan(self):
        try:
            phu_luc = self.browser.find_elements_by_class_name('internal-icon')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(phu_luc[6]).click(phu_luc[6]).perform()
            sleep(1)
            seting = self.browser.find_elements_by_class_name('fa-outline-contact')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(seting[1]).click(seting[1]).perform()
            sleep(1)
        except:
            speech_catch_error()

    def tat_tai_khoan(self):
        try:
            tat_tai_khoan = self.browser.find_element_by_class_name('fa-close')
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(tat_tai_khoan).click(tat_tai_khoan).perform()
            sleep(1)
        except:
            speech_catch_error()

class check(zalo):

    def check_tin_nhan(self):
        if(self.browser == None):
            try:      
                options = webdriver.ChromeOptions() 
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
                PATH1 = PATH[:9] + output_check + PATH[9:]
                options.add_argument("user-data-dir=" + PATH1)
                driver_web = webdriver.Chrome(executable_path=r'D.\chromedriver\chromedriver.exe',chrome_options=options)
                driver_web.implicitly_wait(20)
                driver_web.get('https://id.zalo.me/')
                sleep(3)
                chamdo = driver_web.find_element_by_xpath('//*[@id="main-tab"]/div[2]/div[2]/div[1]/i[2]')
                text = chamdo.get_attribute("class")
                driver_web.close()
                text = text.replace('fa fa-num','Có ')
                text = text.replace('leftbar-unread unread-red','tin nhắn mới')
                text = text.replace('5plus','nhiều hơn 5')
                speech.say_VN_by_Google(text)
                return
            except:
                speech.say_VN_by_Google('Không có tin nhắn mới')
                return
        try:
            chamdo = self.browser.find_element_by_xpath('//*[@id="main-tab"]/div[2]/div[2]/div[1]/i[2]')
            text = chamdo.get_attribute("class")
            text = text.replace('fa fa-num','Có ')
            text = text.replace('leftbar-unread unread-red','tin nhắn mới')
            text = text.replace('5plus','nhiều hơn 5')
            speech.say_VN_by_Google(text)
            return
        except:
            speech.say_VN_by_Google('Không có tin nhắn mới')
            return
    
    def check_thong_bao(self):
        if(self.browser == None):
            try:  
                options = webdriver.ChromeOptions() 
                options.add_experimental_option("excludeSwitches", ["enable-logging"])
                PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
                PATH1 = PATH[:9] + output_check + PATH[9:]
                options.add_argument("user-data-dir=" + PATH1)
                driver_web = webdriver.Chrome(executable_path=r'D.\chromedriver\chromedriver.exe',chrome_options=options)
                driver_web.implicitly_wait(20)
                driver_web.get('https://id.zalo.me/')
                sleep(3)

                chamcam = driver_web.find_element_by_xpath('//*[@id="main-tab"]/div[2]/div[2]/div[3]/i[2]')
                text = chamcam.get_attribute("class")
                driver_web.close()
                text = text.replace('fa fa-num','Có ')
                text = text.replace('leftbar-unread unread-orange','thông báo mới')
                speech.say_VN_by_Google(text)
                return
            except:
                speech.say_VN_by_Google('Không có thông báo mới')
                return
        try:
            chamcam = self.browser.find_element_by_xpath('//*[@id="main-tab"]/div[2]/div[2]/div[3]/i[2]')
            text = chamcam.get_attribute("class")
            text = text.replace('fa fa-num','Có ')
            text = text.replace('leftbar-unread unread-orange','thông báo mới')
            speech.say_VN_by_Google(text)
            return
        except:
            speech.say_VN_by_Google('Không có thông báo mới')
            return

    def lay_ten_nguoi_gan_nhat(self):
        if(self.browser == None):
            try:      
                options = webdriver.ChromeOptions() 
                PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
                PATH1 = PATH[:9] + output_check + PATH[9:]
                options.add_argument("user-data-dir=" + PATH1)
                driver_web = webdriver.Chrome(executable_path=r'.\chromedriver\chromedriver.exe',chrome_options=options)
                driver_web.implicitly_wait(20)
                driver_web.get('https://id.zalo.me/')
                sleep(1)
                tennguoigannhat = driver_web.find_element_by_xpath('/html/body/div/div/div[2]/nav/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/span')
                a = tennguoigannhat.text 
                sleep(1)
                driver_web.close()
                speech.say_VN_by_Google(a)
                return
            except:
                speech_catch_error()
                return
        try:
            tennguoigannhat = self.browser.find_element_by_xpath('/html/body/div/div/div[2]/nav/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/span')
            a = tennguoigannhat.text 
            speech.say_VN_by_Google(a)
            return
        except:
            speech_catch_error()
            return