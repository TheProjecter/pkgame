#coding=utf-8

#pkgame web interface
# author: Albert Lee
# date: 2006-08-10
import web


import Message
import GameWorld
from sys import getfilesystemencoding

sysencoding = getfilesystemencoding()

class Interface(object):
    def __init__(self, user1, user2):
        self.GameWorld = GameWorld.PKField(self)
        self.PrintMsg = {u'文本':self.PrintTextMsg, u'攻击':self.PrintAttackMsg,
                         u'治疗':self.PrintCureMsg, u'buff':self.PrintBuffMsg,
                         u'unbuff':self.PrintBuffMsg, u'debuff':self.PrintDeBuffMsg,
                         u'undebuff':self.PrintUnBuffMsg, u'pick':self.PrintPickMsg}

        count = 2

        self.GameWorld.AddPlayerByName(user1)
        self.GameWorld.AddPlayerByName(user2)
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



urls = (
  '/', 'view',
  '/fight', 'fight',
  
)

import codecs

class view:
    def GET(self):
        print """
        <html>
        <head><title>PKGame</title>
        <META CONTENT="text/html; charset=utf-8" HTTP-EQUIV="Content-Type" />
        </head>
        <body>
        <h2>PkGame</h2>

        <form method="post" action="fight">
        玩家1：<input type="text" name="user1"/><br/>
        玩家2：<input type="text" name="user2"/><br/>
        <input type="submit" value="开战"/>
        </form>
        </body>
        </html>

        """
class fight:
    def POST(self):
        print '<pre>'
        i = web.input()
        u1 = codecs.decode(i.user1, 'utf-8')
        u2 = codecs.decode(i.user2, 'utf-8')
        game = Interface(u1, u2)
        game.Play()
        print '</pre>'
        
web.internalerror = web.debugerror

if __name__ == '__main__': web.run(urls, web.reloader)
