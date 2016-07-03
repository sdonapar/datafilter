import pandas as pd
from rule import *

class FilteredDataFrame():
    def __init__(self,dataframe,rule):
        self.dataframe = dataframe
        self.rule = rule
        self.final_condition = None

    def _apply_condition(self,condition):
        if isinstance(condition,ListCondition):
            return self.dataframe[condition.attribute].isin(condition.values)
        elif isinstance(condition,ValueCondition):
            return self.dataframe[condition.attribute] == condition.value
        
    def _get_dataset(self,dataset):
        ds_final_condition = None
        for condition in dataset.conditions:
            if (ds_final_condition is not None):
                result = self._apply_condition(condition)
                ds_final_condition =  result & ds_final_condition
            else:
                ds_final_condition = self._apply_condition(condition)
        return ds_final_condition

    def apply_rule(self):
        for dataset in self.rule.datasets:
            if (self.final_condition is None):
                self.final_condition = self._get_dataset(dataset)
            else:
                self.final_condition = self._get_dataset(dataset) | self.final_condition
        return self.dataframe[self.final_condition]

if __name__ == '__main__':
    from rule import Rule,DataSet,ListCondition,ValueCondition
    data = [['a',1,'10'],['b',2,20],['c',3,30]]
    df = pd.DataFrame(data=data,columns=['col1','col2','col3'])
    ds1 = DataSet("first")
    ds1.add_condition(ValueCondition('col1','a'))
    ds1.add_condition(ListCondition('col2',[1,2]))
    ds2 = DataSet("second")
    ds2.add_condition(ValueCondition('col1','c'))
    ds2.add_condition(ValueCondition('col3',30))
    rule = Rule("test rule")
    rule.add_dataset(ds1)
    rule.add_dataset(ds2)
    fdf = FilteredDataFrame(dataframe=df,rule=rule)
    print(fdf.apply_rule())