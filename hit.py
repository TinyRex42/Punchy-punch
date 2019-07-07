#Pretty much constructors for different hit objects, and such. I'm planning on having the game compile .txt files to actually generate stuff
#Though in this case it will be generated by other parts of the game
class hit(object):
    def __init__(self, tags, effect, dat, power=100):
        self.tags=tags
        self.effect=effect
        self.power=power
        self.live=True
        self.dat=dat #stuff the effect function call will need
    def weaken(self, per):
        self.power-=per
        if self.power<=0:
            self.live=False
            self.set_dis_why("Blocked below 0%")
    def set_dis_why(self, why):
        self.why=why
    def dis(self):
        self.live=False
    def dispelled(self):
        return not self.live
    def dis_ex(self):
        return self.why
    def resolve(self):
        self.effect(self.dat, self.power)