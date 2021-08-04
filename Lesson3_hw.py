# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:27:45 2021

@author: iansu
"""

#課後挑戰
math = input("請輸入數學成績:")  #讓使用者輸入數學成績
math = int(math)  #把數學成績從字串轉成數字
eng = input("請輸入英文成績:")  #讓使用者輸入英文成績
eng = int(eng) #把英文成績從字串轉成數字
if math >= 90 and eng >= 90:  #判斷如果兩科成績都要90分以上，得到獎品
    print("你得到獎品了 Good!")
elif math <= 60 and eng <= 60:  #判斷如果兩科成績都低於60，得到處罰
    print("你不及格要處罰 Nooooo!")
elif math <= 60 or eng <= 60:  #判斷如果其中一科成績低於60，要再加油
    print("要再加油喔!!")