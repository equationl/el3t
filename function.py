import android
#coding=utf-8
droid = android.Android()

from config import *
import random

#............
#function.py.
#EL3T函数库...
#author:equationl(独孤方程)
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
			return chess
			
#检测是否为平局
def check_draw(allclickchess):
	for i in ALLCHESS:
		if i not  in allclickchess:
			return 'no'
	return 'yes'