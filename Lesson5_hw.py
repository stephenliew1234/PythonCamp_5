# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:40:20 2021

@author: iansu
"""

#猜數字回家挑戰 -- 告知大小並且只能猜五次
import random  #先去圖書館借random模組來使用

answer = random.randint(1, 20)  #設定隨機1~20的其中一個答案
guess = input("請猜數字:")  #讓使用者猜數字
guess = int(guess)  #把input進來的字串轉成數字
i = 1 #紀錄遊玩次數
while answer != guess and i < 5:  #判斷因為猜的答案錯誤和猜的次數少於五所以會重複執行
    print("你猜錯了QQ")
    if answer > guess:  #判斷猜的答案太小
        print("太小了")
    elif answer < guess: #判斷猜的答案太大
        print("太大了")
    guess = input("請猜數字:")  #再猜一次
    guess = int(guess)
    i = i + 1  #次數加一

if answer == guess:  #最後判斷是猜贏還是因為次數不夠所以才跳出
    print("你猜對了!!", "你猜了", i, "次")  #當答案正確則會跳到這行
else:
    print("QQ猜五次都沒對!!", "答案是:", answer)  #次數不夠猜