from enum import Enum

import pandas as pd



# df = pd.read_csv("out2.csv");

# df.value_counts()

class TopicType(Enum):
    BINARY_CLASSIFICATION = "Binary Classification"
    MULTI_CLASS_CLASSIFICATION = "Multi-Class Classification"
    MULTI_LABEL_CLASSIFICATION = "Multi-Label Classification"
    REGRESSION = "Regression"

    def __str__(self):
        return self.name

    # @staticmethod
    # def get_by_name(name):
    #     if name in TopicType.__members__.keys():
    #         return TopicType[name]
    #     return None

    @staticmethod
    def get_by_value(value):
        # print(TopicType.__members__.)
        for item in TopicType.__members__.values():
            # print(item.value)
            # print(item.name)
            if item.value == value:
                return item.name
            # return TopicType.name
        return None



# print(TopicType.get_by_name("MULTI_LABEL_CLASSIFICATION"))
print(TopicType.get_by_value("Multi-Label Classification"))