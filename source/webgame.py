#coding=utf-8

#pkgame web interface
# author: Albert Lee
# date: 2006-08-10
import web


import Message
import GameWorld
from sys import getfilesystemencoding
import codecs
sysencoding = getfilesystemencoding()

class Interface(object):
    def __init__(self):
        pass

    def setPlayers(self, players):
        
        self.GameWorld = GameWorld.PKField(self)
        self.PrintMsg = {u'文本':self.PrintTextMsg, u'攻击':self.PrintAttackMsg,
                         u'治疗':self.PrintCureMsg, u'buff':self.PrintBuffMsg,
                         u'unbuff':self.PrintBuffMsg, u'debuff':self.PrintDeBuffMsg,
                         u'undebuff':self.PrintUnBuffMsg, u'pick':self.PrintPickMsg}

        count = len(players)
        for player in players:
            if player != "":
                self.GameWorld.AddPlayerByName(codecs.decode(player, 'utf-8'))

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
  '/btfight', 'btfight',
)



class view:
    def GET(self):
        print """
        <html>
        <head><title>PKGame</title>
        <META CONTENT="text/html; charset=utf-8" HTTP-EQUIV="Content-Type" />
        </head>
        <body>
        <h2>PkGame</h2>

        <form method="post" action="btfight">
        玩家1：<input type="text" name="user1"/><br/>
        玩家2：<input type="text" name="user2"/><br/>
        <input type="submit" value="开战"/>
        </form>

        <hr/>
        <h2>变态多人型</h2>
        <form method="post" action="btfight">
        玩家1：<input type="text" name="user1"/><br/>
        玩家2：<input type="text" name="user2"/><br/>
        玩家3：<input type="text" name="user3"/><br/>
        玩家4：<input type="text" name="user4"/><br/>
        玩家5：<input type="text" name="user5"/><br/>
        玩家6：<input type="text" name="user6"/><br/>
        玩家7：<input type="text" name="user7"/><br/>
        玩家8：<input type="text" name="user8"/><br/>
        玩家9：<input type="text" name="user9"/><br/>
        <input type="submit" value="开战"/>
        </form>
        
        </body>
        </html>

        """

class btfight:
    def POST(self):
        print '''
        <html>
        <head><title>PKGame</title>
        <META CONTENT="text/html; charset=utf-8" HTTP-EQUIV="Content-Type" />
        </head>
        <body>
        <pre>'''
        i = web.input()
        game = Interface()
        game.setPlayers(i.values())
        game.Play()
        print '</pre></body></html>'
        
        
web.internalerror = web.debugerror

if __name__ == '__main__': web.run(urls, web.reloader)
