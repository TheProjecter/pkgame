#-*-coding:utf-8-*-
from Dice import Dice
from Message import *
import random

class Attack(object):
    def __init__(self, sender):
        self.name = u'推击'
        self.world = sender.world
        self.sender = sender

    def __call__(self):
        target = self.sender.target
        value = self.sender.str * 10

        hit = Dice(self.sender.dex).Roll()
        volt = Dice(target.dex).Roll()
        hits = hit - volt #hit = volt

        if hits > 0 :
            harm = target.BeHurt(value * hits/hit+1)
            self.world.PostMessage(AttackMsg(self, self.sender, target, harm))
        else:
            self.world.PostMessage(TextMsg(u'%s闪过了%s的推击，发动反推!'%(target.name, self.sender.name)))
            AntiAttack(target)()

    def checked(self):
        return True


class AntiAttack(object):
    def __init__(self, sender):
        self.name = u'反推'
        self.world = sender.world
        self.sender = sender

    def __call__(self):
        target = self.sender.target
        value = self.sender.str * 5

        hit = Dice(self.sender.dex).Roll()
        volt = Dice(target.dex).Roll()
        hits = hit - volt #hit = volt

        if hits > 0 :
            harm = target.BeHurt(value * hits/hit+1)
            self.world.PostMessage(AttackMsg(self, self.sender, target, harm))
        else:
            self.world.PostMessage(TextMsg(u'%s闪过了%s的反推!'%(target.name, self.sender.name)))
 
    def checked(self):
        return True

class AboilKiss(object):
    __cooldown__ = 2
    def __init__(self, sender):
        self.name = u'烈焰红唇'
        self.world = sender.world
        self.sender = sender
        self.cooldown = 0

    def __call__(self):
        self.cooldown = AboilKiss.__cooldown__
        target = self.sender.target

        #感情
        reins = Dice(self.sender.cha).Roll()
        #理智
        sence = Dice(target.int).Roll()

        self.world.PostMessage(TextMsg(u'%s抱住%s狂吻!'%(self.sender.name, target.name)))
        if reins > sence:
            harm = target.BeHurt(Dice(self.sender.cha).Roll(Dice(target.wis).Roll()))
            self.world.PostMessage(AttackMsg(self, self.sender, target, harm))
            cure = self.sender.BeCure(harm*Dice(self.sender.wis).Roll()/target.cha)
            self.world.PostMessage(CureMsg(self, self.sender, self.sender, cure))
        else:
            self.world.PostMessage(TextMsg(u'%s理智的拒绝了%s的烈焰红唇!'%(target.name, self.sender.name)))

    def checked(self):
        if self.cooldown == 0:
            return True
        else:
            self.cooldown -= 1
            return False

class Bluff(object):
    __cooldown__ = 2
    def __init__(self, sender):
        self.name = u'甜言蜜语'
        self.world = sender.world
        self.sender = sender
        self.cooldown = 0

    def __call__(self):
        self.cooldown = AboilKiss.__cooldown__
        target = self.sender.target

        bluff = Dice(self.sender.cha).Roll()
        sence = Dice(target.wis).Roll()
        
        self.world.PostMessage(TextMsg(u'%s对%s露出迷人的微笑，甜蜜的说……'%(self.sender.name, target.name)))
        if bluff > sence:
            harm = target.BeHurt(Dice(self.sender.int).Roll(bluff - sence))
            self.world.PostMessage(AttackMsg(self, self.sender, target, harm))
        else:
            self.world.PostMessage(TextMsg(u'%s机智的识破了%s的甜言蜜语!'%(target.name, self.sender.name)))

    def checked(self):
        if self.cooldown == 0:
            return True
        else:
            self.cooldown -= 1
            return False
        
class RandPick(object):
    __cooldown__ = 2
    def __init__(self, sender):
        self.name = u'拾取'
        self.world = sender.world
        self.sender = sender
        self.cooldown = 0

    def __call__(self):
        item = random.choice([item for item in self.world.items if item.enable])(self.sender)
        self.sender.items.append(item)
        self.world.PostMessage(TextMsg(u'%s拾取了%s!'%(self.sender.name, item.name)))

    def checked(self):
        re = len([item for item in self.world.items if item.enable]) > 0 and self.cooldown == 0
        if self.cooldown > 0:
            self.cooldown -= 1
        return re
