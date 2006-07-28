#-*-coding:utf-8-*-
import random

class Dice(object):
    def __init__(self, faces):
        self.min = 1
        self.max = faces 

    @staticmethod
    def make(minPoint, maxPoint):
        re = Dict(MaxPoint)
        re.min = minPoint

    def Roll(self, times = 1):
        re = 0
        for i in xrange(times):
            re += random.randint(self.min, self.max)
        return re

    
