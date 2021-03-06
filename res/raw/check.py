import android
#coding=utf-8
droid = android.Android()

#.............
#check.py.....
#EL3T检测函数库.
#author:equationl(独孤方程)
#.............


#........检测是否获胜类........
class Check_Win:
	def __init__(s, allchess, isclickchess):
		s.allchess = allchess
		s.isclickchess = isclickchess
			
		
 	#判断输赢
	def check(s):
		intop_reasult = Check_Win(s.allchess, s.isclickchess).intop()
		among_reasult = Check_Win(s.allchess, s.isclickchess).among()
		if intop_reasult == 'no' and among_reasult == 'no':
			return 'no'
		if intop_reasult != 'no' and among_reasult == 'no':
			return intop_reasult
		else:
			return 'yes'
		
	#如果点击的是一个顶点
	def intop(s):
		ic = s.isclickchess
		
		#顶点在正上
		if ic == '303' or ic == '203' or ic == '103':
			if Check_Win(s.allchess, s.isclickchess ).intop_top() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_top()
			
		#顶点在正下
		if ic == '301' or ic == '201' or ic == '101':
			if Check_Win(s.allchess, s.isclickchess ).intop_below() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_below()
			
		#顶点在正左
		if ic == '303' or ic == '302' or ic == '301':
			if Check_Win(s.allchess, s.isclickchess ).intop_left() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_left()
			
		#顶点在正右
		if ic == '103' or ic == '102' or ic== '101':
			if Check_Win(s.allchess, s.isclickchess ).intop_right() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_right()
		
		#顶点在左斜上
		if ic == '303':
			if Check_Win(s.allchess, s.isclickchess ).intop_lefttop() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_lefttop()
		
		#顶点在右斜上
		if ic == '103':
			if Check_Win(s.allchess, s.isclickchess).intop_righttop() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_righttop()
		
		#顶点在左斜下
		if ic == '301':
			if Check_Win(s.allchess, s.isclickchess).intop_leftbelow() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_leftbelow()
		
		#顶点在右斜下
		if ic == '101':
			if Check_Win(s.allchess, s.isclickchess ).intop_rightbelow() != 'no':
				return Check_Win(s.allchess, s.isclickchess).intop_rightbelow()
				
		return 'no'
			
			
	#如果点击的是中间
	def among(s):
		ic = s.isclickchess
		#向上下延伸
		if ic == '302' or ic == '202' or ic == '102':
			if Check_Win(s.allchess, s.isclickchess).among_uad() == 'yes':
				return 'yes'
			
		#向左右延展
		if ic == '203' or ic == '202' or ic == '102':
			if Check_Win(s.allchess, s.isclickchess).among_lar() == 'yes':
				return 'yes'
		return 'no'
			
			
			
#..........点击顶点函数集(公用)..........
	def intop_top(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) - 1)
			else:
				return 'no'
		return 'yes'
		
	def intop_below(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) + 1)
			else:
				return 'no'
		return 'yes'
		
	def intop_left(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) - 100)
			else:
				return 'no'
		return 'yes'
		
	def intop_right(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) + 100)
			else:
				return 'no'
		return 'yes'
		
	def intop_lefttop(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) - 101)
			else:
				return 'no'
		return 'yes'

	def intop_righttop(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) + 99)
			else:
				return 'no'
		return 'yes'

	def intop_leftbelow(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) - 99)
			else:
				return 'no'
		return 'yes'

	def intop_rightbelow(s):
		icc = s.isclickchess
		ac = s.allchess
		for i in range(0, 3, 1):
			if icc in ac:
				icc = str(int(icc) + 101)
			else:
				return 'no'
		return 'yes'

		
	
	#........点击中间函数集.........
	
	def among_uad(s):
		icc = s.isclickchess
		ac = s.allchess
		if icc in ac:
			if str(int(icc) + 1) in ac:
				if str(int(icc) - 1) in ac:
					return 'yes'
		return 'no'
			
	def among_lar(s):
		icc = s.isclickchess
		ac = s.allchess
		if icc in ac:
			if str(int(icc) + 100) in ac:
				if str(int(icc) - 100) in ac:
					return 'yes'
		return 'no'
#.............END.............		
			
			
#..........检测威胁类............

class Check_Threaten:
	def __init__(s, isclickchess, allclickchess):
		#allclickchess.append(isclickchess)
		s.isclickchess = isclickchess
		s.allclickchess = allclickchess
		
	def check(s):
		ic = s.isclickchess
		ac = s.allclickchess
		
		if ic == '303' or ic == '203' or ic == '103':
			if Check_Threaten(ic, ac).top_function('-', 1) != 'no':
				return Check_Threaten(ic, ac).top_function('-', 1)
				
		if ic == '301' or ic == '201' or ic == '101':
			if Check_Threaten(ic, ac).top_function('+', 1) != 'no':
				return Check_Threaten(ic, ac).top_function('+', 1)
		
		if ic == '303' or ic == '302' or ic == '301':
			if Check_Threaten(ic, ac).top_function('-', 100) != 'no':
				return Check_Threaten(ic, ac).top_function('-', 100)
				
		if ic == '103' or ic == '102' or ic == '101':
			if Check_Threaten(ic, ac).top_function('+', 100) != 'no':
				return Check_Threaten(ic, ac).top_function('+', 100)

		if ic == '303':
			if Check_Threaten(ic, ac).top_function('-', 101) != 'no':
				return Check_Threaten(ic, ac).top_function('-', 101)
				
		if ic == '103':
			if Check_Threaten(ic, ac).top_function('+', 99) != 'no':
				return Check_Threaten(ic, ac).top_function('+', 99)

		if ic == '301':
			if Check_Threaten(ic, ac).top_function('-', 99) != 'no':
				return Check_Threaten(ic, ac).top_function('-', 99)

		if ic == '101':
			if Check_Threaten(ic, ac).top_function('+', 101) != 'no':
				return Check_Threaten(ic, ac).top_function('+', 101)
				
		if ic == '202':
			if str(int(ic) - 101) in ac:
				return str(int(ic) + 101)
			if str(int(ic) + 101) in ac:
				return str(int(ic) - 101)
			if str(int(ic) -99) in ac:
				return str(int(ic) + 99)
			if str(int(ic) +99) in ac:
				return str(int(ic) - 99)

		return 'no'

	def top_function(s, operator, number):
		ic = s.isclickchess
		ac = s.allclickchess
		
		if operator == '+':
			if ic in ac:
				ic = str(int(ic) + number)
				if ic in ac:
					return str(int(ic) + number)
			return 'no'
		
		if operator == '-':
			if ic in ac:
					ic = str(int(ic) - number)
					if ic in ac:
						return str(int(ic) - number)
			return 'no'
		

#print Check_Threaten('303', ['303', '202']).check()