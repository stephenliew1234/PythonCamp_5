# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:44:30 2021

@author: iansu
"""
#文字型遊戲:猜數字(勻箴同學提供進階版本 ps.用2位玩家視角來猜)
import random

answer = random.randint(1,10)
guest1=input('請第一位玩家輸入名稱')
guest2=input('請第二位玩家輸入名稱')
print('請', guest1,'輸入你猜的數字')
guess1=input()
guess1=int(guess1)
print('請',guest2,'輸入你猜的數字')
guess2=input()
guess2=int(guess2)
if guess1 == answer:
    print(guest1,'真厲害！你贏了！')
else:
    print(guest1, "你猜錯了!正確答案:", answer)
if guess2 == answer:
    print(guest2,'真厲害！你贏了！')
else:
    print(guest2, "你猜錯了!正確答案:", answer)
