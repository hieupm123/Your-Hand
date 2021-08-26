from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import pyautogui
import sys
from datetime import datetime
import psutil
import screen_brightness_control as sbc
from pack_and_run import *

# Note: Tất cả các hàm và class có thể gọi = str nên nếu chắc năng nào cần viết nhiều hàm
# thì chúng ta sẽ gọi hàm = srt

speech = speech_and_say();
value_light_st = [int(10)]

def speech_catch_error():
	text_catch = 'Có gì đó không đúng bạn vui lòng xem lại yêu cầu của mình'
	speech.say_VN_by_Google(text_catch)


class Hardware:
	def __init__(self):
		# Thông số volume
		self.file_volume = open("in_volume.txt",'r')
		self.lines_volume = self.file_volume.readlines()
		self.M_volume = {}
		self.index_volume = 0
		for a in range(0,len(self.lines_volume)):
			self.lines_volume[a].replace("\n","")
			self.M_volume[self.index_volume] = float(self.lines_volume[a])
			self.index_volume += 2
		self.file_volume.close()

					

	# Hàm cho phép tắt phần mềm = task_manager	
	def killer(self,process_name):
		os.system('taskkill /f /im ' + process_name)

	# Hàm thay đổi âm lượng
	def change_volume(self,ok,value = 0):
		if(value % 2):
			value += 1
		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(
		    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		volume = cast(interface, POINTER(IAudioEndpointVolume))

		currentVolumeDb = volume.GetMasterVolumeLevel()
		_VALUE = [currentVolumeDb + 6,currentVolumeDb - 6,self.M_volume[value]] 

		# 0 : tăng, 1 : giảm, 2 : set âm thanh 
		try:
			volume.SetMasterVolumeLevel(_VALUE[ok], None)
		except:
			speech_catch_error()

	# Hàm về đổi unikey
	def change_unikey(self):
		try:
			pyautogui.hotkey('ctrl', 'shift')
			pyautogui.hotkey('alt', 'z')
		except:
			speech_catch_error()

	# Xem giờ
	def get_time(self):
		now = datetime.now()
		a = [now.strftime("%H"),now.strftime("%M"),now.strftime("%S")]
		speech.say_VN_by_Google(str(a[0]) + 'giờ' + str(a[1]) + 'phút' + str(a[2]) + 'giây')	

	# Xem ngày
	def get_day(self):
		now = datetime.now()
		a = [now.strftime("%d"),now.strftime("%m"),now.strftime("%Y")]
		print(a)
		speech.say_VN_by_Google('Ngày' + str(a[0]) + 'tháng' + str(a[1]) + 'năm' + str(a[2]))

	# Hàm cho máy đi ngủ
	def sleep_computer(self):
		try:
			os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
		except:
			speech_catch_error()
	# Hàm tắt máy tính
	def turn_off_computer(self):
		try:
			os.system("shutdown /s /t 1")
		except:
			speech_catch_error()
	# get ram
	def get_ram(self):
		speech.say_VN_by_Google(str(int(psutil.virtual_memory()[2])) + 'phần trăm')

	# get cpu
	def get_cpu(self):
		speech.say_VN_by_Google(str(int(psutil.cpu_percent(4))) + 'phần trăm')

	# get pin
	def get_battery(self):
		battery = psutil.sensors_battery()
		plugged = battery.power_plugged
		plugged_EL = "Plugged In" if plugged else "Not Plugged In"
		plugged_VN = "Đang sạc" if plugged else "Không sạc"
		speech.say_VN_by_Google(str(int(battery[0])) + 'Phần trăm' + plugged_VN)

	# Bật tiết kiệm pin
	def battery_saving_on(self):
		try:
			os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 100")
			os.system("powercfg /setactive scheme_current")
		except:
			speech_catch_error()
	# Tắt tiết kiệm pin
	def battery_saving_off(self):
		try:
			os.system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 5")
			os.system("powercfg /setactive scheme_current")
		except:
			speech_catch_error()
	# Tăng độ sáng
	def screen_brightness_up(self,light = ('+ ' + str(value_light_st[0]))):
		try:
			sbc.set_brightness(light)
		except:
			speech_catch_error()

	# Giảm độ sáng
	def screen_brightness_down(self,light = ('- ' + str(value_light_st[0]))):
		try:
			sbc.set_brightness(light)
		except:
			speech_catch_error()
	# Cài đặt độ sáng
	def screen_brightness_set(self,light):
		try:
			sbc.set_brightness(str(light))
		except:
			speech_catch_error()