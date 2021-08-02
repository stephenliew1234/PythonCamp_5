# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:11:22 2021

@author: iansu
"""
#小挑戰 -- 讓使用者輸入半徑來讓電腦輸出周長及面積

radius = input('請輸入圓的半徑: ') #讓使用者輸入半徑並儲存在 radius變數裡
radius = float(radius) #把input輸入的str轉換成float並儲存在 radius變數裡

#圓周長公式:半徑*2*3.14
circumference = 2 * 3.14 * radius #計算圓周長並儲存在 circumference變數裡

#園面積公式:半徑*半徑*3.14
area = 3.14 * radius * radius #計算圓面積並儲存在 area變數裡

print('周長是', circumference) #輸出周長到螢幕
print('面積是', area) #輸出面積到螢幕