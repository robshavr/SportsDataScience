from ipywidgets.widgets import widget
import matplotlib.widgets as w
import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as sha
from pylab import rcParams
from ipywidgets import *


class Model:

    def __init__(self, VO2max=58.6, vLamax=0.5, RunningEco=11.95, Ks1=0.25, Ks2=1.2, VolRel=0.45):

        self.VO2max = VO2max
        self.vLamax = vLamax
        self.RunningEco = RunningEco

        self.VO2ss = np.arange(1, VO2max, 0.01)

        # Define Constants
        self.Ks1 = Ks1 ** 2                # Range: 0.2 - 0.3
        self.Ks2 = Ks2 ** 3                 # Range: 1.0 - 1.3
        self.VolRel = VolRel            # Range: 0.40 - 0.45, depends on individual body

        # Calculated values
        self.ADP = self.calc_ADP()
        self.vLass = self.calc_vLass()
        self.LaComb = self.calc_LaComb()
        self.vLanet = self.calc_vLanet()

    # ==============================[ update Values ]===============================
    def update(self, VO2max=58.6, vLamax=0.5, RunningEco=11.95, Ks1=0.25, Ks2=1.2, VolRel=0.45):
        # update the inital values
        self.VO2max = VO2max
        self.vLamax = vLamax
        self.RunningEco = RunningEco

        self.Ks1 = Ks1 ** 2
        self.Ks2 = Ks2 ** 3
        self.VolRel = VolRel

        # calculate the other values again
        self.calc_ADP()
        self.calc_vLass()
        self.calc_LaComb()
        self.calc_vLanet()

    # ===============================[ Calculation functions ]================================
    def calc_ADP(self):
        self.ADP = np.sqrt((self.Ks1 * self.VO2ss) / (self.VO2max - self.VO2ss))
        return self.ADP

    def calc_vLass(self):
        self.vLass = 60 * self.vLamax / (1 + ( self.Ks2 / self.ADP ** 3))
        return self.vLass

    def calc_LaComb(self):
        self.LaComb = (0.01576 / self.VolRel) * self.VO2ss
        return self.LaComb

    def calc_vLanet(self):
        self.vLanet = abs(self.vLass - self.LaComb)
        return self.vLanet

    # ================================[ Plotting The values ]=====================================
    def plot_lactate(self):

        # calculate the crossing point (AT) between gross lactate production and combustion
        line1 = sha.LineString(np.column_stack((self.vLass, self.VO2ss)))
        line2 = sha.LineString(np.column_stack((self.LaComb, self.VO2ss)))
        VO2AT = line1.intersection(line2)

        # speed at anaerobic threshold
        sAT = VO2AT.y / self.RunningEco 
        print(self.vLass)
        # percentage of VO2max
        pcVO2maxAT = VO2AT.y / self.VO2max
        
        # print to console
        print(f'AT is at {round(sAT,2)} m/s, {round(pcVO2maxAT*100,1)}% of VO2max')
            
        # convert VO2ss into velocity (m/s)
        v = self.VO2ss / self.RunningEco
        
        # plot all lactate curves
        plt.plot(v, self.vLanet)
        plt.plot(v, self.vLass)
        plt.plot(v, self.LaComb)
        
        plt.legend(['Lack of Pyruvate | Lactate Acummulation', 
                    'Gross Lactate Formation', 
                    'Potential Lactate Removal'])
        
        # set limits for interactive visualisation
        plt.ylim( 0, 8 )
        plt.xlim( 0, 6 )
            
        # vertical line at AT
        
        plt.axvline(x=sAT)
        plt.show()
    
    def slider(self):
        # Slider only works for jupyter notebooks
        slider = interact(self.update, 
            VO2max = widgets.FloatSlider(value=55, min=40, max=80,step=0.5),
            vLamax = widgets.FloatSlider(value=0.5, min=0.2, max=1.5,step=0.01),
            RunningEco = widgets.FloatSlider(value=11.95, min=10, max=15,step=0.05),
            Ks1 = widgets.FloatSlider(value=0.25 , min=0.2, max=0.3,step=0.01),
            Ks2 = widgets.FloatSlider(value=1.2, min=1, max=1.3,step=0.01),
            VolRel = widgets.FloatSlider(value=.45, min=.42, max=.45,step=0.01))
        
        
