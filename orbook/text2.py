import random
from abc import abstractmethod

class Lifeentity:
    def __init__(self,name,hotpoint,magicpoint):

        # 参数说明：name,hotpoint,magicpoint分别代表名字、生命值、魔法值
        self.__name = name
        self.__hotpoint = hotpoint
        self.__magicpoint = magicpoint

    @property
    def name(self):
        return self.__name

    @property
    def hotpoint(self):
        return self.__hotpoint

    @property
    def magicpoint(self):
        return self.__magicpoint

    @hotpoint.setter
    def hotpoint(self,hotpoint):
        self.__hotpoint=hotpoint
        return self.__hotpoint


    @abstractmethod
    def nor_attack(self):
        pass

    def display(self):
        return self.__name,self.__hotpoint,self.__magicpoint

    @property
    def is_live(self):
        return self.__hotpoint

class Ultraman(Lifeentity):
    def __init__(self,name,hotpoint,magicpoint):
        super.__init__(self,name,hotpoint,magicpoint)


    def nor_attack(self,Monster_hotpoint):
        Monster_hotpoint-=random.randint(15,25)
        return Monster_hotpoint

    def magic_attack(self,Monster_hotpoint):
        Monster_hotpoint -= random.randint(20, 30)
        self.__magicpoint -= 40
        return self.__magicpoint, Monster_hotpoint

    def super_attack(self,Monster_hotpoint):
        Monster_hotpoint = Monster_hotpoint*0.25
        self.__magicpoint -= 40
        return self.__magicpoint, Monster_hotpoint

    def resume(self):
        self.__magicpoint+=random.randint(1,10)
        return self.__magicpoint


class Monster(Lifeentity):
    def __init__(self,name,hotpoint,magicpoint):
        super.__init__(self,name,hotpoint,magicpoint)

    def nor_attack(self,Ultraman_hotpoint):
        Ultraman_hotpoint-=random.randint(10,20)
        return Ultraman_hotpoint

if __name__=='__main__':
    U1=Ultraman('迪迦',100,100)
    U2=Ultraman('赛文',100,100)
    M1=Monster('哥尔赞',200,100)
    M2=Monster('小怪兽',150,100)
    Ultra_attack1=[U1.nor_attack(M1.hotpoint),U1.super_attack(M1.hotpoint),U1.magic_attack(M1.hotpoint)]
    while True:
        if M1.is_live and U1.is_live:
            random.choice(Ultra_attack1)
            M1.nor_attack(U1.hotpoint)
            Ul_te=U1.display()
            Mon_te=M1.display()
            if Ul_te.is_live and not Mon_te.is_live:
                print('奥特曼胜')
                break
            else:
                print('怪兽打败了奥特曼')
                break

























