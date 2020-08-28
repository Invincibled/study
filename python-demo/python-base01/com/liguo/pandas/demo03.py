import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.sum

data = np.array([[150,50],
                [152,52],
                [160,55],
                [164,57],
                [165,58],
                [168,59],
                [170,60],
                [171,61],
                [173,61],
                [173,61],
                [176,63],
                [177,64],
                [180,67],
                [183,70],
                [184,71]], np.int32)


x = data[:,0:-1]#从第0列开始到倒数第2列停止
y = data[:,-1] #取出最后一列

#print(np.shape(x), np.shape(y))

print(x)
print(y)

# plt.scatter(x,y)
# plt.show()




model = LinearRegression().fit(x,y)
#print(model.predict([[169]]))  #注意model.predict()中要预测的数据跟训练数据x的shape保持一致

print(model.coef_)#coef_：回归系数(斜率)
#对于线性回归问题计算得到的feature的系数。
#如果输入的是多目标问题，则返回一个二维数组(n_targets, n_features)；
#如果是单目标问题，返回一个一维数组(n_features,)。

print(model.intercept_)#intercept_：截距项

print(model.score(x, y))# 返回预测的决定系数R^2;
#其结果等于1-(((y_true - y_pred) **2).sum() / ((y_true - y_true.mean()) ** 2).sum())


plt.scatter(x, y)
plt.plot(x, model.predict(x))
plt.show()

