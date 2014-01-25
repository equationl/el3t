import android
#coding=utf-8
droid = android.Android()

from layoutdata import *
from config import *
from function import *

#...........
#EL3T.py....
#EL3T主程序..
#...........

#应用布局文件，添加menu
def main_show():
	#初始化默认变量
	global owner, playerchess, computerchess, allclickchess
	owner = 'player'
	playerchess = []
	computerchess = []
	allclickchess = []
	droid.fullDismiss()
	droid.clearOptionsMenu()
	droid.fullShow(XML_GAME)
	droid.addOptionsMenuItem('重来','refresh','None','ic_menu_info_details')
	droid.addOptionsMenuItem('信息', 'information', None, None)
	droid.addOptionsMenuItem('退出','exit','None','ic_menu_close_clear_cancel')
	
	#监听
	event()

def event():
	while True:
		e=droid.eventWait().result
		if e['name'] == 'refresh':
			main_show()
		if e['name'] == 'information':
			pass
		if e['name'] == 'exit':
			quit() 
		if e["name"]=="click":
			id=e["data"]["id"]
			for i in ALLCHESS:
				if id == 'btn_' + i:
					add_chess(i)
					



#.......其他函数......

#设置xml组件函数

def set_xml(id, property, value):
	droid.fullSetProperty(id,property,value)


#下子处理函数
def add_chess(i):
	if owner == 'player':
	 	if check_click(i, allclickchess) == 'yes':
	 		playaudio('undo.wav')
	 		return 'no'
	 	set_xml('toptext', 'text', '电脑(白)下子')
		playerchess.append(i)
		allclickchess.append(i)
		colour = 'black'
		global owner
		owner = 'computer'
	elif owner == 'computer':
	 	if check_click(i, allclickchess) == 'yes':
	 	 	playaudio('undo.wav')
	 		return 'no'
	 	set_xml('toptext', 'text', '玩家(黑)下子')
		computerchess.append(i)
		allclickchess.append(i)
		colour = 'white'
		owner = 'player'

	set_xml('btn_' + i, 'background', 'file://' + IMAGEPATH + 'game_chess_' + colour + '.bmp')
	playaudio('stone.wav')


main_show()
