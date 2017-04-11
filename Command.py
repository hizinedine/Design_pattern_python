__author__ = 'diw220'
class Barbucer:
    def MakeMutton(self):
        print "Mutton"
    def MakeChickenWing(self):
        print "Chicken Wing"
class Newcommand:
    def Ncd(self):
        print "new command"
class Command:
    def __init__(self,temp):
        self.receiver=temp
    def ExecuteCmd(self):
        pass
class Cnw(Command):
    def ExecuteCmd(self):
        self.receiver.Ncd()
class BakeMuttonCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeMutton()

class ChickenWingCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()

class Waiter:
    def __init__(self):
        self.order =[]
    def SetCmd(self,command):
        self.order.append(command)
        print "Add Order"
    def Notify(self):
        for cmd in self.order:
            #self.order.remove(cmd)
            #lead to a bug
            cmd.ExecuteCmd()


if __name__ == "__main__":
    barbucer=Barbucer()
    newcommand=Newcommand()
    cmd=BakeMuttonCmd(barbucer)
    cmd2=ChickenWingCmd(barbucer)
    cmd3=Cnw(newcommand)
    girl=Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.SetCmd(cmd3)
    girl.Notify()
