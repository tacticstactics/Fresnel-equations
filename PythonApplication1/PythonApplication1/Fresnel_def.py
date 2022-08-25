
#Fresnel-equations_def.py

import numpy as np
import math
import cmath

def proc1(param=0.01,m=512):

    global c
    c = 2.99792458E+14 # um / s


    steptheta1 = 0.18; # degree

    theta1col = np.zeros((m,1)); # aoi. Angle Of Incidence

    PTscol = np.zeros((m,1)); # PowerTrans
    
    PRscol = np.zeros((m,1)); # PowerReflection

    PTpcol = np.zeros((m,1)); # Phase of Trans E

    PRpcol = np.zeros((m,1)); # Phase of Refleced E
       
    #Signalcol = np.ones(m, dtype=complex);#*2

    # PRe1 must be higher than PRe2 because this is assuming air to glass incidence.

    n1 = 1;
    n2 = 1.5;

    


    for ii in range(m):

        theta1 = ii * steptheta1
        theta1col[(ii)] = theta1

        costheta1=math.cos(3.14*theta1/180)
               
        
        theta2 = math.asin(n1*math.sin((3.14*theta1/180)*180/3.14))

        costheta2 = math.cos(3.14*theta2/180)

        rs = (n1*costheta1-n2*costheta2)/(n1*costheta1+n2*costheta2)
        ts = (2*n1*costheta1)/(n1*costheta1+n2*costheta2)

        #Er = re1+(te1*te2*re2)*np.exp(1j*sigma)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma)+re2**10*np.exp(1j*5*sigma));
        #Et = (te1*te2)*(1+re2**2*np.exp(1j*1*sigma)+re2**4*np.exp(1j*2*sigma)+re2**6*np.exp(1j*3*sigma)+re2**8*np.exp(1j*4*sigma)+re2**10*np.exp(1j*5*sigma));
        

        #Reflect
        PRs = (rs)**2
        PRscol[(ii)]=PRs

        PTs = (ts)**2
        PTscol[(ii)]=PTs


        #Erphase = cmath.phase(Er)
        #Erphasecol[(ii)] = Erphase
        
        #Trans
        #conjEt = Et.conjugate()
        #PT = abs(Et)**2
        #PTetacol[(ii)]=PT

        #Etphase = cmath.phase(Et)
        #Etphasecol[(ii)] = Etphase     


    return theta1col, PTscol, PRscol, PTpcol, PRpcol


