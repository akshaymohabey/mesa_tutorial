# Import Dependencies
import mesa

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

    def __init__(self):
        self.sugar = Sugar()
        self.spice = Spice()
        self.trader = Trader()


model = SugarscapeG1mt()
