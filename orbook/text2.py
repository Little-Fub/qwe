from  random import  randint, randrange
from abc import abstractmethod

class Lifeentity:
    __slots__ = ('_name', '_hp')
    def __init__(self,name,hp):

        # 参数说明：name,hp,mp分别代表名字、生命值、魔法值
        self._name = name
        self._hp = hp
        #self.mp = mp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp >=0 else 0

    @property
    def alive(self):
        return self._hp>0



    @abstractmethod
    def nor_attack(self,other):
        pass



class Ultraman(Lifeentity):
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def nor_attack(self,other):
        other.hp-=randint(15,25)


    def magic_attack(self,others):
        if self._hp >= 40:
            self._hp -= 40
            for temp in others:
                temp.hp -= randint(20, 30)
            return True
        return False

    def super_attack(self,other):
        if self._hp >=50:
            self._hp -= 50
            injury = other.hp * 0.75
            injury = injury if injury >= 50 else 50
            other.hp -=injury
            return True
        else:
            self.nor_attack(other)
            return False

    def resume(self):
        self._mp+=randint(1,10)
        return self._mp

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Monster(Lifeentity):
    __slots__ = ('_name', '_hp')
    def nor_attack(self,other):
        other.hp-=randint(10,20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self.name + \
               '生命值: %d\n' % self.hp

def is_any_alive(Monsters):
    """判断有没有小怪兽是活着的"""
    for Monster in Monsters:
        if Monster.alive > 0:
            return True
    return False


def select_alive_one(Monsters):
    monsters_len = len(Monsters)
    while True:
        index = randrange(monsters_len)
        Monster = Monsters[index]
        if Monster.alive > 0:
            return Monster
def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('哥尔赞', 300)
    m2 = Monster('露比', 800)
    m3 = Monster('小怪兽', 600)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.nor_attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.super_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.nor_attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()


























