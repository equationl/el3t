import android
#coding=utf-8
droid = android.Android()

from layoutdata import *
from config import *
from function import *
from robot import *
from init import *

#...........
#EL3T.py....
#EL3T主程序..
#author:equationl(独孤方程)
#...........

#应用布局文件，添加menu
def main_show():
	#初始化默认变量
	global owner, playerchess, computerchess, allclickchess, listprompt
	owner = 'player'
	playerchess = []
	computerchess = []
	allclickchess = []
	listprompt = []
	droid.fullDismiss()
	droid.clearOptionsMenu()
	droid.fullShow(XML_GAME)
	droid.fullSetTitle('EL3T')
	set_list('游戏开始')
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
			showdialog(ABOUT)
		if e['name'] == 'exit':
			droid.fullDismiss()
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

#设置提示列表
def set_list(text):
	listprompt.insert(0, text)
	droid.fullSetList('list', listprompt)
	
#如果获胜后
def iswin(owner):
	showdialog('恭喜\n\t\t' + owner + '获得胜利！')
	
#如果平局后
def isdraw():
	showdialog('\t\t不错哦，平局耶，下次加油吧！')
	
#显示对话框
def showdialog(text):
	droid.dialogCreateAlert('提示',text)
	droid.dialogSetPositiveButtonText('继续')
	droid.dialogShow()
	response=droid.dialogGetResponse().result
	if response.has_key("canceled"):
		main_show()
	result=response["which"]
	if result=='positive': 
		main_show()


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

	set_xml('btn_' + i, 'background', 'file://' + IMAGEPATH + 'game_chess_' + colour + '.bmp')
	set_list('玩家下子:' + i)
	playaudio('stone.wav')
	#检查是否获胜
	if Check_Win(playerchess, i).check() == 'yes':
		iswin('player')
	if check_draw(allclickchess) == 'yes':
		isdraw()
		
		
	robot(i)
	
#电脑玩家主函数
def robot(i):
	sc = Robot(allclickchess, i).shouldclick()
	set_xml('toptext', 'text', '玩家(黑)下子')
	computerchess.append(sc)
	allclickchess.append(sc)
	colour = 'white'
	global owner
	owner = 'player'

	set_xml('btn_' + sc, 'background', 'file://' + IMAGEPATH + 'game_chess_' + colour + '.bmp')
	set_list('电脑下子:' + sc)
	playaudio('stone.wav')
	if Check_Win(computerchess, sc).check() == 'yes':
		iswin('computer')
	if check_draw(allclickchess) == 'yes':
		isdraw()

install()

main_show()