from sklearn import tree

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 63, 40], [190, 90, 47], [177, 70,40], [159, 55, 37], [171, 75, 42], [180, 80, 42]] 

y = ['m', 'f', 'f', 'f', 'm', 'm', 'm', 'f', 'm', 'm']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[190, 70, 43]])
print prediction