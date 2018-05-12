import numpy as np
from mesa import Agent, Model
from mesa.datacollection import DataCollector
from mesa.space import NetworkGrid
from mesa.time import SimultaneousActivation


class PoliticalAgent(Agent):
    def __init__(self, unique_id, model, authenticity, ideal_point):
        super().__init__(unique_id, model)

        self.authenticity = authenticity
        self.ideal_point = ideal_point

        self.social_network = None
        self.action = None

    def step(self):
        pass

    def advance(self):
        pass


class NetworkModel(Model):
    def __init__(self, G, seed=24):
        super().__init__(seed)

        self.grid = NetworkGrid(G)
        self.schedule = SimultaneousActivation(self)

    def step(self):
        pass
