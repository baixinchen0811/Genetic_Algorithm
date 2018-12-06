# from sklearn import svm
#
# X = [[0, 0], [1, 1], [1, 0]]  # training samples
# y = [0, 1, 1]  # training target
# clf = svm.SVC()  # class
# clf.fit(X, y)  # training the svc model
# result = clf.predict([2,2])  # predict the target of testing samples


# coding=gbk
from sklearn import datasets
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data[0])
print(len(digits.data))
print(len(digits.target))


clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-2:]))
data = np.reshape(digits.data[5],(8,8))
new_im = Image.fromarray(data)
# 显示图片
new_im.show()
# loadImage()