#-*-coding:utf-8-*-

import Message
import GameWorld

class Interface(object):
    def __init__(self):
        self.GameWorld = GameWorld.PKField(self)
        self.PrintMsg = {u'文本':self.PrintTextMsg, u'攻击':self.PrintAttackMsg,
                         u'治疗':self.PrintCureMsg, u'buff':self.PrintBuffMsg,
                         u'unbuff':self.PrintBuffMsg, u'debuff':self.PrintDeBuffMsg,
                         u'undebuff':self.PrintUnBuffMsg, u'pick':self.PrintPickMsg}
        
        name = raw_input('请输入第一个玩家名字：').decode('GBK')
        self.GameWorld.AddPlayerByName(name)
        name = raw_input('请输入第二个玩家名字：').decode('GBK')
        self.GameWorld.AddPlayerByName(name)
        
        for p in self.GameWorld.players:
            self.PrintCharCard(p)
        
    def Play(self):
        self.GameWorld.Play()

    def PrintCharCard(self, player):
        print u"--->玩家：%s"%player.name
        print u"    力量：%s"%player.str
        print u"    敏捷：%s"%player.dex
        print u"    体质：%s"%player.con
        print u"    智力：%s"%player.int
        print u"    感知：%s"%player.wis
        print u"    魅力：%s"%player.cha


    def PrintTextMsg(self, msg):
        print msg.text

    def PrintAttackMsg(self, msg):
        print msg.template%(msg.sender.name, msg.action.name, msg.target.name, msg.effect)
        
    def PrintCureMsg(self, msg):
        print msg.template%(msg.sender.name, msg.action.name, msg.target.name, msg.effect)

    def PrintBuffMsg(self, msg):
        print msg.template%(msg.sender.name, msg.action.name, msg.target.name, msg.effect)

    def PrintUnBuffMsg(self, msg):
        print msg.template%(msg.owner.name, msg.buff.name)

    def PrintDeBuffMsg(self, msg):
        print msg.template%(msg.sender.name, msg.action.name, msg.target.name, msg.effect)

    def PrintUnBuffMsg(self, msg):
        print msg.template%(msg.owner.name, msg.debuff.name)

    def PrintPickMsg(self, msg):
        print msg.template%(msg.owner.name, msg.item.name)

if __name__=='__main__':
    game = Interface()
    game.Play()
