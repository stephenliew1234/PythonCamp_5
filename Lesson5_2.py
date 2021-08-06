# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:16:58 2021

@author: iansu
"""
#猜數字2代 -- 一直猜到對
import random  #先去圖書館借random模組來使用

answer = random.randint(1, 10)  #設定隨機1~10的其中一個答案
guess = input("請猜數字:")  #讓使用者猜數字
guess = int(guess)  #把input進來的字串轉成數字

while answer != guess:  #判斷因為猜的答案錯誤所以會一直執行
    print("你猜錯了QQ")
    guess = input("請猜數字:")
    guess = int(guess)
print("你猜對了")  #當答案正確則會跳到這行
    