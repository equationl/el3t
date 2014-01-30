import android
#coding=utf-8
droid = android.Android()

from config import *
import random

#............
#function.py.
#EL3T函数库...
#............

#检测该坐标是否存在
def check_click(i, clickchess):
	if i in clickchess:
		return 'yes'
	else:
		return 'no'
		
#播放音乐
def playaudio(name):
	droid.mediaPlay(AUDIOPATH + name)

#随机生成一个未点击的坐标
def randomclick(acc):
	while True:
		chess = random.choice(ALLCHESS)
		if chess in acc:
			pass
		else:
			print '这是一个来自随机生成的棋子:' + chess
			return chess
