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

class Pan(object):
    enable = True
    def __init__(self, owner):
        self.name = u'平底锅'
        self.owner = owner
        self.world = owner.world
        self.count = 1

    def __call__(self):
        self.count -= 1
        target = self.owner.target

        self.world.PostMessage(TextMsg(u'一声巨响，当！'))
        harm = target.BeHurt(50)
        self.world.PostMessage(AttackMsg(self, self.owner, target, harm))

    def checked(self):
        return True

class Sausage(object):
    enable = True
    def __init__(self, owner):
        self.name = u'香肠'
        self.owner = owner
        self.world = owner.world
        self.count = 10

    def __call__(self):
        target = self.owner.target

        self.world.PostMessage(TextMsg(u'%s一边用香肠暴打%s，一边狂吃香肠！'%(self.owner.name, target.name)))
        times = Dice(self.count).Roll()
        for i in xrange(times):
            hit = Dice(self.owner.dex).Roll()
            volt = Dice(target.dex).Roll()
            if hit > volt:
                self.world.PostMessage(TextMsg(u'%s用香肠暴打%s，香肠碎片四处飞溅！'%(self.owner.name, target.name)))
                harm = target.BeHurt(self.owner.str)
                self.world.PostMessage(AttackMsg(self, self.owner, target, harm))
            else:
                self.world.PostMessage(TextMsg(u'%s抓住%s的香肠啃了一口！'%(target.name, self.owner.name)))
                cure = target.BeCure(target.wis)
                self.world.PostMessage(CureMsg(self, self.owner, target, cure))

        self.world.PostMessage(TextMsg(u'%s吃掉了剩下的香肠！'%self.owner.name))
        cure = self.owner.BeCure(target.wis * (self.count - times))
        self.world.PostMessage(CureMsg(self, self.owner, self.owner, cure))
        self.count = 0

    def checked(self):
        return True
