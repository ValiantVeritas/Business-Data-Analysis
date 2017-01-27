# classifiers: http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

# accuracy scoring: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
from sklearn.metrics import accuracy_score

#_________________________________________________

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...

# get classifiers: http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html

#1
clf1 = GaussianNB()
#2
clf2 = KNeighborsClassifier(n_neighbors=3)
#3
clf3 = SVC()

clf4 = MLPClassifier()


#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#_________________________________________________

# CHALLENGE - ...and train them on our data

clf = clf.fit(X, Y)
prediction = clf.predict( X ) #prediction = clf.predict( [[190, 70, 43]] )

#1
clf1 = clf1.fit(X, Y)
prediction1 = clf1.predict( X )
#2
clf2 = clf2.fit(X, Y)
prediction2 = clf2.predict( X )
#3
clf3 = clf3.fit(X, Y)
prediction3 = clf3.predict( X )

clf4 = clf4.fit(X, Y)
prediction4 = clf4.predict( X )

#_________________________________________________

# CHALLENGE - compare their results!

# get scores: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html

#print prediction
#print prediction1
#print prediction2
#print prediction3

Y_true = Y

score = accuracy_score(Y_true, prediction)
score1 = accuracy_score(Y_true, prediction1)
score2 = accuracy_score(Y_true, prediction2)
score3 = accuracy_score(Y_true, prediction3)
score4 = accuracy_score(Y_true, prediction4)
#print score
#print score1
#print score2
#print score3

#best_score = max(score,score1,score2,score3)
#print("Best score: \n  " + str(best_score))

classifier_names = {'tree': score, 'GaussianNB': score1, 'KNeighborsClassifier': score2, 'SVC': score3, 'MLPClassifier': score4}
print classifier_names
print score 
print score2
print score3
print score4
#best_scoring_classifiers = [name for name in classifier_names if classifier_names[name] == best_score]
#print("Best scorer(s): ")
#for best_scorers in best_scoring_classifiers: print("  "+best_scorers)

