from enum import Enum
import pandas as pd
#
#
# class TopicType(Enum):
#     BINARY_CLASSIFICATION = "Binary Classification"
#     MULTI_CLASS_CLASSIFICATION = "Multi-Class Classification"
#     REGRESSION = "Regression"
#
#     def __str__(self):
#         return self.name
#
#
# # for name,value in TopicType.__members__.items():
# #     print(value)

# #     print(value.value)
#
#
#
#
# # print(type(TopicType.__members__.keys()))
#
# print(TopicType.__members__.keys().__contains__("MULTI_CLASS_CLASSIFICATION"))


# list=[1,2]

# print(list[0])

# print(type({"TEST": 0.1, "TRAIN": 0.8, "VALIDATE": 0.1}))
# print(type({"TEST": 0.1, "TRAIN": 0.8, "VALIDATE": 0.1}.__str__()))


class OperationType(Enum):
    FILL_MISSING = 'Set Missing Value',\
                   'Set Missing Value to "[Custom Value]<#43A047>"',\
                   'Set Missing Value in [{target}]<#AAAAAA> with [{value}]<#43a047>'
    ENCODE_COLUMN = 'Value to column',\
                    'for each unique value in [{target}]<#AAAAAA>',\
                    'Convert each unique value from ([{target}]<#AAAAAA>) into a column'
    DELETE_COLUMN = 'Delete Column',\
                    'Delete [{target}]<#AAAAAA>',\
                    'Delete [{target}]<#AAAAAA>'
    RENAME_COLUMN = 'Rename',\
                    'Rename [{target}]<#AAAAAA> to "[Custom Value]<#43a047>"',\
                    'Rename [{target}]<#AAAAAA> to [{value}]<#43a047>'
    CREATE_COLUMN_BY_LOG = 'Create a new column',\
                           '[Log]<#0A45B5>([{target}]<#AAAAAA>, "[10]<#43A047>")', \
                           'Create LOG_[{target}]<#AAAAAA> from LOG([{target}]<#AAAAAA>, [{value}]<#43a047>)'
    CREATE_COLUMN_BY_LN = 'Create a new column',\
                          '[Ln]<#0A45B5>([{target}]<#AAAAAA>)',\
                          'Create LN_[{target}]<#AAAAAA> from LN([{target}]<#AAAAAA>)'
    CREATE_COLUMN_BY_NORMALIZATION = 'Create a new column', \
                          '[Normalization]<#0A45B5>([{target}]<#AAAAAA>, "[0,1]<#43A047>")', \
                           'Create NOR_[{target}]<#AAAAAA> from Normalization([{target}]<#AAAAAA>)'

    def display(self):
        return self.value[0]

    def action(self, target=None):
        return self.value[1].format(target=target)

    def detail(self, target=None, value=None):
        return self.value[2].format(target=target, value=value)

    @staticmethod
    def get_by_name(name):
        if name in OperationType.__members__.keys():
            return OperationType[name]
        return None


pd.read_excel()