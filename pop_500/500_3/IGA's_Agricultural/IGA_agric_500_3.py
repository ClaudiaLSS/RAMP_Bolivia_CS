# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:28:24 2022

@author: pietr
"""
from core import User, np
User_list = []


###### IGA's  AGRICULTURAL ######

#Definig users IRRIGATION WATER


IW = User("Irrigation Water", 9)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)
