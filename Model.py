# Import Dependencies
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

# Resource Classes

class Sugar(mesa.Agent):
   
    def __init__(self,unique_id,model,pos,max_sugar):
        super().__init__(unique_id,model)
        self.pos = pos
        self.amount = max_sugar
        self.max_sugar = max_sugar

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
        spice_distribution = np.flip(sugar_distribution, 1)

        agent_id = 0
        # for _, (x,y) in self.grid.coord_iter():
        #     max_sugar = sugar_distribution[x,y]

        #     if max_sugar > 0:
        #         sugar = Sugar(agent_id, self, (x,y), max_sugar)
        #         # self.grid.place_agent(sugar,(x,y))
        #         agent_id += 1
        #         print(agent_id, max_sugar, (x,y))

            # print(_, (x,y))

        # for _, (x,y) in self.grid.coord_iter():
        #     print(int(sugar_distribution[x,y]),(x,y))

#Calling Model
model = SugarscapeG1mt()
