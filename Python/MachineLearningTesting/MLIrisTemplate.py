from sklearn.datasets import load_iris
iris = load_iris();
print(iris.feature_names);
print(iris.target_names);
print(iris.data [0]);
print(iris.target[0]);
for i in range(len(iris.data)):
    print ("Example %s: Label %s, features %s" % (i, iris.target[i], iris.data[i]));


