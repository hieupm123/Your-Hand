from os import get_terminal_size
from general_web import *
general = general_web()
output_check = general.lay_ten_nguoi_dung()

speech = speech_and_say();

def speech_catch_error():
    text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
    speech.say_VN_by_Google(text_catch)

class google(object):
    browser = None;

    def init(self):
        try:
            options = webdriver.ChromeOptions()
            PATH = r"C:\Users\\AppData\Local\Google\Chrome\User Data\Profile 2"
            PATH1 = PATH[:9] + output_check + PATH[9:]
            options.add_argument("user-data-dir=" + PATH1)
            self.browser = webdriver.Chrome(executable_path=r'./chrome_driver/chromedriver.exe',chrome_options=options)
            self.browser.get("https://www.google.com/")
            time.sleep(3)
        except:
            speech_catch_error()

    def home(self):
        # try:
            self.browser.get('https://www.google.com/')
            time.sleep(2)
        # except:
        #     speech_catch_error()

    def scroll_down(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + " + str(len) + " )")

    def scroll_up(self,len  = value_scroll_st[0]):
        self.browser.execute_script("window.scrollTo(0, window.scrollY - " + str(len) + " )")

    def type_in_search(self,nhap = ''):
        try:
            text_ = speech.speech_none_pause()
            if(text_ != ''):
                nhap = text_;
            self.browser.get('https://www.google.com/search?q=' + nhap)
            sleep(2)
        except:
            speech_catch_error()

    def select_link(self,a=1):
        try:
            id = speech.speech_none_pause()
            a = general.get_number(id)
            chon = self.browser.find_elements_by_class_name("LC20lb")
            self.browser.implicitly_wait(10)
            ActionChains(self.browser).move_to_element(chon[a-1]).click(chon[a-1]).perform()
            time.sleep(randint(1,2));
        except:
            speech_catch_error()