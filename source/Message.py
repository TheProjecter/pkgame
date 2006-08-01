#-*-coding:utf-8-*-

class TextMsg(object):
    def __init__(self, text):
        self.name = u'文本'
        self.template = u'%s'
        self.text = text

class AttackMsg(object):
    def __init__(self, action, sender, target, effect):
        self.name = u'攻击'
        self.template = u'%s的%s给%s造成了%s点杀伤。'
        self.action = action
        self.sender = sender
        self.target = target
        self.effect = effect

class CureMsg(object):
    def __init__(self, action, sender, target, effect):
        self.name = u'治疗'
        self.template = u'%s的%s为%s治疗了%s点生命。'
        self.action = action
        self.sender = sender
        self.target = target
        self.effect = effect
        
class BuffMsg(object):
    def __init__(self, action, sender, target, effect):
        self.name = u'buff'
        self.template = u'%s的%s为%s带来了%s的效果。'
        self.action = action
        self.sender = sender
        self.target = target
        self.effect = effect

class UnBuffMsg(object):
    def __init__(self, buff, owner):
        self.name = u'unbuff'
        self.template = u'%s失去了%s效果。'
        self.buff = buff
        self.owner = owner

class DebuffMsg(object):
    def __init__(self, action, sender, target, effect):
        self.name = u'debuff'
        self.template = u'%s对%s释放%s，造成了%s的效果。'
        self.action = action
        self.sender = sender
        self.target = target
        self.effect = effect

class UnDeBuffMsg(object):
    def __init__(self, debuff, owner):
        self.name = u'undebuff'
        self.template = u'%s从%s中恢复过来。'
        self.debuff = debuff
        self.owner = owner

class PickMsg(object):
    def __init__(self, owner, item):
        self.name = u'pick'
        self.template = u'%s捡起了%s!'
        self.owner = owner
        self.item = item
