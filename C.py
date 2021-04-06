a = [31,28,31,30,31,30,31,31,30,31,30,31]#普通年份
b = [31,29,31,30,31,30,31,31,30,31,30,31]#闰年
c = [1,2,3,4,5,6,7,8,9,10,11,12]
e = 5
g = 0
h = 0
for years in range(2000,2021):
	if years%4 == 0:#因为2000年为闰年，就不再判考虑百年份能否被400整除
		for mos in c:#循环月份
			for day in range(1,b[mos-1]+1):#范围为对应年份列表中对应的月份天数
				f = e%7+1
				e += 1
				if day == 1 and f == 1:
					h += 2
				elif day == 1 and f != 1:
					h += 2
				elif day != 1 and f == 1:
					h += 2
				elif day !=1 and f != 1:
					h += 1
				print("现在是",years,"年",mos,"月",day,"日","星期",f,"已经跑了",h,"公里")
	elif years%4 != 0:
		for mos2 in c:
			for day in range(1,a[mos2-1]+1):
				f = e%7+1
				e += 1
				if day == 1 and f == 1:
					h += 2
				elif day == 1 and f != 1:
					h += 2
				elif day != 1 and f == 1:
					h += 2
				elif day !=1 and f != 1:
					h += 1
				print("现在是",years,"年",mos2,"月",day,"日","星期",f,"已经跑了",h,"公里")

