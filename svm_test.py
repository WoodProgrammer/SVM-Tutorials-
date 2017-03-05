from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
def test_accuracy(datas_predicted_y,datas_real_Y):
    point= 0
    border=4
    for i in range(border):
        if datas_predicted_y[i]==datas_real_Y[i]:
            point+=10

    return 100-(border*10-point)



X=np.array([[1,2],[1,3],[1,4],[1,5]])
y=np.array([1,1,1,2])
svm=SVC()
svm.fit(X,y)

y_pred=[]

#prediction=svm.predict(X[i])
#print prediction
print X[0]
for i in range(4):
    y_pred.append(svm.predict(X[i]))
    print svm.predict(X[i])


print confusion_matrix(y,y_pred)
