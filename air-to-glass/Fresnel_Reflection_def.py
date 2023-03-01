
#Fresnel-Reflection_def.py

import numpy as np
import math


def proc1(param=0.01,m=512):

    #steptheta1 = 0.163036; # degree
    steptheta1 = 0.18; # degree

    theta1col = np.zeros((m,1)); # aoi. Angle Of Incidence
    theta2col = np.zeros((m,1))

    rscol = np.zeros((m,1))
    rpcol = np.zeros((m,1))
    
    tscol = np.zeros((m,1))
    tpcol = np.zeros((m,1))

    PTscol = np.zeros((m,1)); # PowerTrans
    
    PRscol = np.zeros((m,1)); # PowerReflection

    PTpcol = np.zeros((m,1)); # Phase of Trans E

    PRpcol = np.zeros((m,1)); # Phase of Refleced E

    # n2 must be higher than n1 because this code is assuming air to glass incidence.

    n1 = 1
    n2 = 1.5


    for ii in range(m):

        theta1 = ii * steptheta1
        theta1col[(ii)] = theta1

        costheta1=math.cos(math.pi*theta1/180)
        
        
        theta2 = math.asin((n1/n2)*math.sin(math.pi*theta1/180))*(180/math.pi)
        theta2col[(ii)] = theta2

        costheta2 = math.cos(math.pi*theta2/180)
        
        # S Polarization

        rs = (n1*costheta1-n2*costheta2)/(n1*costheta1+n2*costheta2)
        rscol[(ii)] = rs

        PRs = (np.abs(rs))**2
        PRscol[(ii)]=PRs
        
        ts = (2*n1*costheta1)/(n1*costheta1+n2*costheta2)
        tscol[(ii)] = ts

        PTs = (n2/n1)*(costheta2/costheta1)*(np.abs(ts))**2
        PTscol[(ii)]=PTs

        # P Polarization

        rp = (n2*costheta1-n1*costheta2)/(n2*costheta1+n1*costheta2)
        rpcol[(ii)] = rp

        PRp = (np.abs(rp))**2
        PRpcol[(ii)]=PRp

        tp = (2*n1*costheta1)/(n2*costheta1+n1*costheta2)
        tpcol[(ii)] = tp

        PTp = (n2/n1)*(costheta2/costheta1)*(np.abs(tp))**2      
        PTpcol[(ii)]=PTp


        #Erphase = cmath.phase(Er)
        #Erphasecol[(ii)] = Erphase
        
        #Trans
        #conjEt = Et.conjugate()
        #PT = abs(Et)**2
        #PTetacol[(ii)]=PT

        #Etphase = cmath.phase(Et)
        #Etphasecol[(ii)] = Etphase         

    return theta1col, theta2col, rscol, tscol, rpcol, tpcol, PRscol, PTscol, PRpcol, PTpcol


