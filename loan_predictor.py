import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svm=SVC()
datas=pd.read_csv("test_data.csv")
#print datas.head()
#for i in datas["purpose"]:
#datas['purpose']=datas2["purpose"].astype("int")


datas['purpose']=datas.purpose.map({'debt_consolidation':0,'credit_card':1,'all_other':2,'home_improvement':3,'major_purchase':4,"small_business":5})


#print datas['purpose']

#print datas.head()

main_datas=datas[datas.keys()]
real_class=datas['paid_stat']
#print main_class

def run_tester():
    svm.fit(main_datas,real_class)
    #test_data=[1,0,0.1496,194.02,10.71441777,4,667,3180.041667,3839,76.8,0,0,1]
    predicted_class=svm.predict(main_datas)
    return accuracy_score(real_class,predicted_class)
#print
print run_tester()
