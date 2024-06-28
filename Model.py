# Import Dependencies
import mesa
import numpy as np
import matplotlib.pyplot as plt

# Resource Classes

class Sugar(mesa.Agent):
    '''
    Sugar:
    - Contains an amount of Sugar
    - Grows one amount of Sugar at each turn
    '''

    def __init__(self):
        print("I am Sugar")

class Spice(mesa.Agent):
    '''
    Spice:
    - Contains an amount of Spice
    - Grows one amount of Spice at each turn    
    '''
    
    def __init__(self):
        print("I am Spice")

# Trader Class

class Trader(mesa.Agent):
    '''
    Trader
    - has a metabolism for Sugar and Spice
    - harvest and trades Sugar and Spice to survive and thrive
    '''

    def __init__(self):
        print("I am Trader")

# Model Class

class SugarscapeG1mt(mesa.Model):
    '''
    A model class to manage Sugarscape with Traders (G1mt)
    from Growing Artificial Societies
    '''

    def __init__(self,width=50,height=50):
        
        # Initiate width and height of Sugarscape
        self.width = width
        self.height = height

        # Initite Mesa Grid Class
        self.grid = mesa.space.MultiGrid(self.width,self.height,torus=False)

        # Read in landscape file from supplementary material
        sugar_distribution = np.genfromtxt("sugar-map.txt")
        spice_distribution = np.flip(sugar_distribution)

        plt.imshow(sugar_distribution,origin='lower')
        plt.show()

        # plt.imshow(spice_distribution,origin='lower')
        # plt.show()

        # print(sugar_distribution.shape)
        # print(sugar_distribution[30][15])


        # self.sugar = Sugar()
        # self.spice = Spice()
        # self.trader = Trader()


model = SugarscapeG1mt()
