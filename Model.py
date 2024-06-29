# Import Dependencies
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt
import itertools

# Resource Classes

class Sugar(mesa.Agent):
    def __init__(self,unique_id,model, pos, max_sugar):
        super().__init__(unique_id, model)
        self.pos = pos
        self.amount = max_sugar
        self.max_sugar = max_sugar

class Spice(mesa.Agent):
    def __init__(self, unique_id, model, pos, max_spice):
        super().__init__(unique_id,model)
        self.pos = pos
        self.amount = max_spice
        self.max_spice = max_spice

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

    def __init__(self,width=50,height=50, initial_population = 200,
                 endowment_min = 25, endowment_max=50, metabolism_min=1,
                 metabolism_max=5, vision_min=1, vision_max=5):
        # Initiate width and height of Sugarscape
        self.width = width
        self.height = height

        # Inititate population attributes
        self.initial_population = initial_population
        self.endowment_min = endowment_min
        self.endowment_max = endowment_max


        # Initite Mesa Grid Class
        self.grid = mesa.space.MultiGrid(self.width,self.height,torus=False)

        # Initiate scheduler
        self.schedule = mesa.time.RandomActivationByType(self)

        # Read in landscape file from supplementary material
        sugar_distribution = np.genfromtxt("sugar-map.txt")
        spice_distribution = np.flip(sugar_distribution, 1)


        agent_id = 0
        for _,(x,y) in self.grid.coord_iter():
            max_sugar = sugar_distribution[x,y]
            if max_sugar > 0:
                sugar = Sugar(agent_id, self, (x,y), max_sugar)
                self.grid.place_agent(sugar,(x,y))
                self.schedule.add(sugar)
                print(self.schedule.agents_by_type[Sugar][agent_id])
                agent_id += 1
            
            max_spice = spice_distribution[x,y]
            if max_spice > 0:
                spice = Spice(agent_id,self, (x,y), max_spice)
                self.grid.place_agent(spice, (x,y))
                self.schedule.add(spice)
                print(self.schedule.agents_by_type[Spice][agent_id])
                agent_id += 1

#Calling Model
model = SugarscapeG1mt()