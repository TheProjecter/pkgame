#-*-coding:utf-8-*-
import random
from Message import *
from Actions import *
from Dice import Dice

class Player(object):
    def __init__(self, world, name):
        self.world  = world
        self.name   = name
        self.skills = []
        self.buff = []
        self.debuff = []
        self.items = []
        self.states = {u'正常':self.OnNomal, u'被推倒':self.OnDown}
        self.state = u'正常'

    def FinallyCreate(self):
        self.hp     = self.con * 10
        self.mana   = self.int * 10
        self.skills = [Attack(self), AboilKiss(self), Bluff(self), RandPick(self)]

    def BeHurt(self, value):
        if self.hp > value:
            self.hp -= value
            return value
        else:
            re = self.hp
            self.hp = 0
            self.state = u'被推倒'
            return re

    def BeCure(self, value):
        if self.con * 10 > value + self.hp:
            self.hp += value
            return value
        else:
            re = self.hp
            self.hp = self.con * 10
            re = self.hp - re
            return re

    def OnNomal(self):
        random.choice(self.readyskills + self.readyitems)()

    def OnDown(self):
        self.world.PostMessage(TextMsg(u'%s倒地不起，行动不能，唯有将头偏向一边，默默地流下屈辱泪水。'%self.name))

    def OnCall(self):
        self.buff = [buff for buff in self.buff if buff.checked()]
        self.debuff = [debuff for debuff in self.debuff if debuff.checked()]

        self.readyskills = [s for s in self.skills if s.checked()]
        self.readyitems = [i for i in self.items if i.checked()]
        
        self.items = [item for item in self.items if item.count > 0]

        for d in self.debuff:
            d.checked()

        for b in self.buff:
            b.checked()
            
        self.states[self.state]()


def CreateByDice(world, name):
    dice        = Dice(6)
    re 		= Player(world, name)
    re.str	= dice.Roll(4)	#strength
    re.dex	= dice.Roll(4)	#dexterity
    re.con 	= dice.Roll(4)	#constitution
    re.int	= dice.Roll(4)	#intelligence
    re.wis	= dice.Roll(4)	#wisdom
    re.cha	= dice.Roll(4)	#charisma
    re.FinallyCreate()
    return re
