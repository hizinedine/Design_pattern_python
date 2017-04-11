__author__ = 'diw220'

class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.op1+self.op2

class OperationFactory:
    def CreateOperation(self):
        temp = Operation()
        return temp

class OperationAddFactory(OperationFactory):
    def CreateOperation(self):
        temp = OperationAdd()
        return temp

if __name__ == "__main__":
    op = OperationAddFactory()
    opadd = op.CreateOperation()
    opa = input("a: ")
    opb = input("b: ")

    opadd.op1 = opa
    opadd.op2 = opb
    print opadd.GetResult()