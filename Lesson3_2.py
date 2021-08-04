# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:17:04 2021

@author: iansu
"""
#挑戰--校長的獎學金
math = input("請輸入數學成績:")  #讓使用者輸入數學成績
math = int(math)  #把數學成績從字串轉成數字
eng = input("請輸入英文成績:")  #讓使用者輸入英文成績
eng = int(eng) #把英文成績從字串轉成數字
if math >= 90 and eng >= 90:  #判斷如果兩科成績都要90分以上,則發獎金
    print("你得到獎學金了")
elif math == 100 or eng == 100:  #判斷如果其中一科有100分,則發獎金
    print("你得到獎學金了")
else:  #剩下的則是沒有獎學金的
    print("QQ你沒有獎學金")