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
            for player in self.players:
                self.PostMessage(TextMsg(u'%s hp：%s'%(player.name, player.hp)))

            for player in self.players:
                player.OnCall()
            
        for winner in [p for p in self.players if p.hp > 0]:
            self.PostMessage(TextMsg(u'%s成功的推倒了对手，获得了胜利!'%winner.name))

    def PostMessage(self, msg):
        try:
            self.interface.PrintMsg[msg.name](msg)
        except KeyError:
            pass
