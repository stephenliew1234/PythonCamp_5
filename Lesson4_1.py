# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:14:43 2021

@author: iansu
"""
#文字型遊戲:猜數字
import random  #載入隨機變數模組

answer = random.randint(1, 10)  #隨機選一個數字在1~10之間
guess = input("請猜一個數字:")  #請使用者輸入數字
guess = int(guess)  #把input輸入的字串型態轉成數字型態
if answer == guess:  #判斷是否為猜對
    print("你猜對了!!!GOOD")
else:  #如果猜錯則執行16行程式碼
    print("你猜錯了!!哈哈!! 正確答案是:", answer)