# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:01:19 2024

@author: 15834
"""

import win32com.client as com
import time
import os
import csv
import shutil
import traceback
from cherry_model import AntiBully
import numpy as np
import math
import pandas as pd
import ctypes
import utils
import planner
#%%
def planning(ego_attributes,pre_attributes,y_des):
    x0 = (float(ego_attributes[5]) + float(ego_attributes[7]))/2
    x1 = (float(pre_attributes[5]) + float(pre_attributes[7]))/2
    v0 = float(ego_attributes[3])
    v1 = float(pre_attributes[3])
    y0 = (float(ego_attributes[6]) + float(ego_attributes[8]))/2
    heading = math.atan((float(ego_attributes[8]) - float(ego_attributes[6]))/(float(ego_attributes[7]) - float(ego_attributes[5])))
    u,f = planner.MPCplanner(x0, v0, y0, heading,
                             x1, -15, v1, y_des, 0.1, 10,
                             10, 1, 10, 1, 100)
    heading = heading + float(ego_attributes[3])*f*0.1/4
    print(u,f)
    return u,heading        
    
#%%    
if __name__ == '__main__':
    #com接口初始化
    vissim_com = com.Dispatch("Vissim.Vissim")
    vissim_com.LoadNet(r'\cherry.inpx')
    vissim_com.Graphics.SetAttValue('Quickmode',False)
    Sim = vissim_com.Simulation
    simulation_time = 0
    hasvehicle = False
    speed_ego, speed_ag = [],[]
    pos_ego, pos_ag = [], []
    y_ego, y_ag = [],[]
    while simulation_time <= 25:
        Sim.RunSingleStep()
        simulation_time = vissim_com.Simulation.SimulationSecond
        if simulation_time > 3 and hasvehicle == False:
            egoVehicle = vissim_com.Net.Vehicles.AddVehicleAtLinkPosition(630, 1,  2,  5, 10*3.6, True)#(vehicle_type, link, lane, xcoordinate, desired_speed, interaction)
            preVehicle = vissim_com.Net.Vehicles.AddVehicleAtLinkPosition(630, 1,  1,  50, 18*3.6, True)#(vehicle_type, link, lane, xcoordinate, desired_speed, interaction)
            egoNo = int(egoVehicle.AttValue('No'))
            hasvehicle = True   
        if hasvehicle == True:
            ego_attributes= [egoVehicle.AttValue('No'), egoVehicle.AttValue('VehType'),egoVehicle.AttValue('Pos'),egoVehicle.AttValue('Speed'),egoVehicle.AttValue('Acceleration'),
                            egoVehicle.AttValue('CoordFrontX'),egoVehicle.AttValue('CoordFrontY'),egoVehicle.AttValue('CoordRearX'),egoVehicle.AttValue('CoordRearY'),egoVehicle.AttValue('Lane')]
            pre_attributes= [preVehicle.AttValue('No'), preVehicle.AttValue('VehType'),preVehicle.AttValue('Pos'),preVehicle.AttValue('Speed'),preVehicle.AttValue('Acceleration'),
                            preVehicle.AttValue('CoordFrontX'),preVehicle.AttValue('CoordFrontY'),preVehicle.AttValue('CoordRearX'),preVehicle.AttValue('CoordRearY'),preVehicle.AttValue('Lane')]
            speed_ego.append(float(ego_attributes[3]))
            speed_ag.append(float(pre_attributes[3]))
            pos_ego.append((float(ego_attributes[5]) + float(ego_attributes[7]))/2)
            pos_ag.append((float(pre_attributes[5]) + float(pre_attributes[7]))/2)
            y_ego.append((float(ego_attributes[6]) + float(ego_attributes[8]))/2)
            y_ag.append(1.75-3.5)
            if simulation_time < 10:
                u,f = planning(ego_attributes,pre_attributes,1.75)
            else:
                u,f = planning(ego_attributes,pre_attributes,-1.75)
            vissim_com.Net.Vehicles.ItemByKey(egoNo).SetAttValue('acc_com_uda',u)
            vissim_com.Net.Vehicles.ItemByKey(egoNo).SetAttValue('angle_com_uda',f)
        

