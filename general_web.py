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
from pack_and_run import *
model = pickle.load(open("su_li_so.pkl", 'rb'))

speech = speech_and_say();

value_scroll_st = [325];

def speech_catch_error():
	text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
	speech.say_VN_by_Microsoft(text_catch)

class general_web:

	def lay_ten_nguoi_dung(self):
		output_check = ''
		file_check_chrome = open('check_chrome_version.txt','r+');
		output_check = file_check_chrome.read()
		if(output_check == ''):
			driver = webdriver.Chrome('./chrome_driver/chromedriver.exe')
			driver.get('chrome://version/')
			time.sleep(randint(1,2))
			profile_path = driver.find_element_by_id('profile_path').text
			def cleanup_str_profile_path():
				ans = ''
				str(profile_path)
				for i in range (9,len(profile_path),1):
					if(profile_path[i] != '\\'):
						ans += profile_path[i]
					else:
						break
				return ans

			file_check_chrome.write(cleanup_str_profile_path())
			driver.close()
			output_check = cleanup_str_profile_path() 
		file_check_chrome.close()
		return output_check
		



	def kiem_tra_trong_view(self,drivers, elem):
	    elem_left_bound = elem.location.get('x')
	    elem_top_bound = elem.location.get('y')
	    elem_width = elem.size.get('width')
	    elem_height = elem.size.get('height')
	    elem_right_bound = elem_left_bound + elem_width
	    elem_lower_bound = elem_top_bound + elem_height

	    win_upper_bound = drivers.execute_script('return window.pageYOffset')
	    win_left_bound = drivers.execute_script('return window.pageXOffset')
	    win_width = drivers.execute_script('return document.documentElement.clientWidth')
	    win_height = drivers.execute_script('return document.documentElement.clientHeight')
	    win_right_bound = win_left_bound + win_width
	    win_lower_bound = win_upper_bound + win_height

	    return all((win_left_bound <= elem_left_bound,
	                win_right_bound >= elem_right_bound,
	                win_upper_bound <= elem_top_bound,
	                win_lower_bound >= elem_lower_bound)
	               )

	def click_to_any_button(self, PATH):
		self.driver_web.execute_script("arguments[0].click();",self.driver_web.find_element_by_xpath(PATH))
		time.sleep(randint(1,2))

	def write_the_text(self,PATH, text = ''):
		try:
			driver = self.driver_web.find_element_by_xpath(PATH)
			driver.send_keys(text)
			time.sleep(randint(1,2))
		except:
			speech_catch_error()

	def scroll_up(self,driver,len  = 325):
		try:
			driver.execute_script("window.scrollTo(0, window.scrollY + " + str(len) + " )")
		except:
			speech_catch_error()

	def scroll_down(self,driver,len  = 325):
		try:
			driver.execute_script("window.scrollTo(0, window.scrollY - " + str(len) + " )")
		except:
			speech_catch_error()

	def get_number(self, text):
		try:
			number = int(text);
			return number;
		except:
			ar = [text];
			y_pred = model.predict(ar)
			return int(y_pred[0])
		return 2;

