#-*-coding:utf-8-*-
from Message import *
from Dice import Dice


class ManBook(object):
    enable = True
    def __init__(self, owner):
        self.name = u'《男人的挚爱》'
        self.owner = owner
        self.world = owner.world
        self.count = 1

    def __call__(self):
        self.count -= 1
        target = self.owner.target
        #冲动
        urge = Dice(target.wis).Roll()
        #理智
        sence = Dice(target.int).Roll()

        self.world.PostMessage(TextMsg(u"%s大声朗读男女通杀的神秘书籍《男人的挚爱》（你猜这是什么书？哦呵呵呵……）！"%self.owner.name))
        if urge > sence:
            self.world.PostMessage(TextMsg(u"%s听后无比冲动，鼻血狂喷！"%target.name))
            harm = target.BeHurt(target.wis*urge)
            self.world.PostMessage(AttackMsg(self, self.owner, target, harm))
        else:
            self.world.PostMessage(TextMsg(u"%s设法另自己冷静了下来。"%target.name))
            
    def checked(self):
        return True
