class Rule():
    """This class defines a rule"""
    def __init__(self,name):
        self.name = name
        self.datasets = []
    def add_dataset(self,dataset):
        self.datasets.append(dataset)
    def __str__(self):
        return "Rule %s"%(self.name)

class DataSet():
    """This is a dataset"""
    def __init__(self,name):
        self.name = name
        self.conditions = []
    def add_condition(self,condition):
        self.conditions.append(condition)
    def __str__(self):
        return "Condition is {name}".format(name=self.name)

class Condition():
    """Condition"""
    def __init__(self,attribute):
        self.attribute = attribute
        self.condition = None
    def __str__(self):
        return "Condition for attribute %s"%(self.attribute)

class ListCondition(Condition):
    """This takes a list of values to filter"""
    def __init__(self,attribute,values_list):
        Condition.__init__(self,attribute)
        self.values = list(values_list)
    def __str__(self):
        return "Condition for attribute %s with value %s"%(self.attribute,self.values)

class ValueCondition(Condition):
    """This takes exact one value to compare """
    def __init__(self,attribute,value):
        Condition.__init__(self,attribute)
        self.value = value
    def __str__(self):
        return "Condition for attribute %s with value %s"%(self.attribute,str(self.value))

if __name__ == '__main__':
    pass

