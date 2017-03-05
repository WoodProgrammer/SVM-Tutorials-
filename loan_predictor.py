import pandas as pd
from collections import Counter
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pylab as plt

svm=SVC()

cnt=Counter()
raw_data=pd.read_csv("test_data.csv")
main_cols=["credit_policy","purpose","int.rate","installment","log.annual.inc","dti","fico","days.with.cr.line","revol.bal","revol.util","inq.last.6mths","delinq.2yrs","pub.rec","paid_stat"]

datas = pd.DataFrame(raw_data, columns = main_cols)


for  i in datas['purpose']:
    cnt[i] += 1
k=0
t={}
for i in cnt.keys():
    t[i]=k
    k+=1

datas['purpose']=datas.purpose.map(t)
main_cols2=["credit_policy","purpose","int.rate","installment","log.annual.inc","dti","fico","days.with.cr.line","revol.bal","revol.util","inq.last.6mths","delinq.2yrs","pub.rec"]

main_datas=datas[main_cols2]
real_class=datas["paid_stat"]
#test_data=[1,0,0.1496,194.02,10.71441777,4,667,3180.041667,3839,76.8,0,0,1]

X_train,X_test,y_train,y_test=train_test_split(main_datas,real_class,random_state=1)
svm.fit(X_train,y_train)
print X_train
predicted_class=svm.predict(X_test)

#print predicted_class
print accuracy_score(y_test,predicted_class)

###DATA VISUALITION.
x=datas.loc[datas['purpose'] == t['small_business']]

y1=x.loc[x['paid_stat']==1]
y2=x.loc[x['paid_stat']==0]

#x['paid_sta'].hist()
x.hist()
plt.show()
