X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
regr = svm.SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,coef0=1)
regr.fit(X, y)