#-*-coding:utf-8-*-
import Player
from Dice import Dice
from Message import *
import time
import Items

class PKField(object):
    def __init__(self, interface):
        self.interface = interface
        self.players = []
        self.items = [Items.ManBook, Items.Pan, Items.Sausage]

    def AddPlayerByName(self, name):
        self.players.append(Player.CreateByDice(self, name))

    def Play(self):
        l = len(self.players)

        
        for i in xrange(l):
            self.players[i].target = self.players[(i+1)%l]
            
        
        while len([p for p in self.players if p.hp > 0]) > 1:
            
            #roll first
            fl = [(p, Dice(p.dex).Roll()) for p in self.players if p.hp > 0]
            fl.sort(key = lambda x : x[1])
            l = len(fl)
            for i in xrange(l):
                fl[i][0].ChooseTarget(fl) #target = fl[(i+1)%l][0]
                fl[i][0].OnCall()

            for i in xrange(l) :
                player = fl[i][0]
                self.PostMessage(TextMsg(player.name + ' hp: ' + str(player.hp)))

            
        for winner in [p for p in self.players if p.hp > 0]:
            self.PostMessage(TextMsg(u'%s成功的推倒了%s，获得了胜利!'%(winner.name, winner.target.name)))

    def PostMessage(self, msg):
        try:
            self.interface.PrintMsg[msg.name](msg)
        except KeyError:
            pass
