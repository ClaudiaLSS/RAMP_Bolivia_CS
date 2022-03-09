# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:29:06 2022

@author: pietr
"""
'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''
## 53%

from core import User, np
User_list = []

###### IGA's  AGRICULTURAL ######

#Definig users IRRIGATION WATER


IW = User("Irrigation Water", 18)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)


#Definig users LOWLANDS AGRO-PRODUCTIVE UNIT

LAU = User("Lowlands agro-productive unit", 4)
User_list.append(LAU)

#Appliances

LAU_GD = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_GD.windows([420,1080],[0,0],0.35)

LAU_VW = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.82)
LAU_VW.windows([420,1140],[0,0],0.35)

LAU_BT = LAU.Appliance(LAU,1,370,2,900,0.2,180)
LAU_BT.windows([360,930],[1080,1440],0.35)


