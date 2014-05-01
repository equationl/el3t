import android
#coding=utf-8
droid = android.Android()

from os.path import exists
from os import makedirs
from os import access
import os
from filedata import *
from config import *

#...............
#init.py........
#EL3T初始化函数库.
#author:equationl(独孤方程)
#...............

def install():

#检测并创建程序文件夹
	if not exists(IMAGEPATH):
		makedirs(IMAGEPATH)
	if not exists(AUDIOPATH):
		makedirs(AUDIOPATH)

#检测并生成程序资源
	for i in IMAGEDATA:
		if not access(IMAGEPATH + i[0],os.F_OK):
			f = open(IMAGEPATH + i[0], 'w')
			f.write(i[1].decode('hex'))
			f.close()

	for i in AUDIODATA:
		if not access(AUDIOPATH + i[0],os.F_OK):
			f = open(AUDIOPATH + i[0], 'w')
			f.write(i[1].decode('hex'))
			f.close()
