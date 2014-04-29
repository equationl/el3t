import android
#coding=utf-8
droid = android.Android()

from check import *
from function import *

#..............
#robot.py......
#EL3T电脑函数库..
#..............

#主类
class Robot:

	def __init__(s, allclickchess, lastclickchess):
		s.allclickchess = allclickchess
		s.lastclickchess = lastclickchess
		
	def shouldclick(s):
		acc = s.allclickchess
		lc = s.lastclickchess
		
		threatenchess = Check_Threaten(lc, acc).check()
		if threatenchess == 'no':
			return randomclick(acc)
		if check_click(threatenchess, acc) == 'yes':
			return randomclick(acc)
		return threatenchess