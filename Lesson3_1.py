# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 09:43:26 2021

@author: iansu
"""
#挑戰--列出分數等級
score = input("請輸入成績?")  #讓使用者輸入成績
score = int(score)  #把成績從字串轉成數字

if score >= 90:  #如果大於等於90輸出A
    print('A')
elif score >= 80:  #其他如果大於等於80輸出B
    print('B')
elif score >= 70:  #其他如果大於等於70輸出C
    print('C')
elif score >= 60:  #其他如果大於等於60輸出D
    print('D')
else:  #剩下都是低於60輸出E
    print('E')