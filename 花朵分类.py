import random
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB


def readExcel():
    excel_path = './iris.xlsx'
    excel_file = pd.read_excel(excel_path).values
    return excel_file

def gaussian_learn(new_array,difference_array,array=None):
    a = 1
    iris_dic = {'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}
    iris_train = np.array([i[:-1] for i in new_array])
    type_train = np.array([iris_dic[i[4]] for i in new_array])
    clf = GaussianNB()
    clf.fit(iris_train,type_train)
    for i in difference_array:
        iris_test = np.array([i[:-1]])
        predict = clf.predict(iris_test)
        if predict[0] == iris_dic[i[-1]]:
            a += 1
    predict_name = '无'
    if array is not None:
        predict = clf.predict(np.array([array]))[0]
        for k,v in iris_dic.items():
            if v == predict:
                predict_name = k

    return a / len(difference_array) , predict_name

def changeArray(filename):
    all_iris_list = [ list(i) for i in filename]
    new_array = random.sample(all_iris_list,int(0.6*len(filename)))
    difference_array = [i for i in all_iris_list if i not in new_array]
    return new_array,difference_array

def p_learn():
    a = 0
    for i in range(100):
        excel_file = readExcel()
        new_array, difference_array = changeArray(excel_file)
        P_learn, iris_name = gaussian_learn(new_array, difference_array)
        a += P_learn
    return a / 100


def main():
    a = [5,3.4,1.5,0.3]
    excel_file = readExcel()
    new_array, difference_array = changeArray(excel_file)
    P_learn,iris_name = gaussian_learn(new_array, difference_array,a)
    print('learn',p_learn(),'iris_type',iris_name)

if __name__ == '__main__':
    main()