from sklearn.datasets import load_iris
from sklearn import tree
from io import StringIO
import pydotplus
import graphviz
dot_data = StringIO()
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
